# R analytical companion for the knowledge-graph primer.
#
# Input boundary: run from the primer directory and read the entities and
# precomputed relations in examples/fixture.json. The relations are a
# deduplicated positive-claim projection, not the evidence store: negative
# claims are excluded, and polarity, dates, provenance and claim identity are
# unavailable to the graph. It is not an as-of-date view and cannot resolve
# conflicting claims or establish whether an edge is currently valid.

library(dplyr)
library(igraph)
library(tidygraph)

fixture <- jsonlite::fromJSON("examples/fixture.json")
entities <- fixture$entities |> select(id, label, type)
relations <- fixture$relations |> select(source, target, type, weight)

graph <- graph_from_data_frame(
  relations,
  directed = TRUE,
  vertices = entities |> rename(name = id)
)

# Tidygraph makes node-level transformations explicit and composable. Compute
# the component labels explicitly with igraph so the result does not depend on
# an interactive tidygraph context helper.
component_membership <- components(graph, mode = "weak")$membership
tidy_graph <- as_tbl_graph(graph) |>
  activate(nodes) |>
  mutate(
    degree_total = centrality_degree(mode = "all"),
    in_component = component_membership
  )

stopifnot(igraph::vcount(graph) == nrow(entities))
stopifnot(igraph::ecount(graph) == nrow(relations))
stopifnot(all(tidy_graph |> activate(nodes) |> pull(degree_total) >= 0))

# igraph supplies directed shortest paths and weakly connected components.
path <- shortest_paths(
  graph,
  from = "policy:travel-v1",
  to = "org:northbridge",
  weights = E(graph)$weight,
  mode = "out",
  output = "vpath"
)$vpath[[1]]
path_labels <- V(graph)$label[as.integer(path)]
weak_components <- components(graph, mode = "weak")

stopifnot(identical(path_labels, c("Northbridge Travel Policy v1", "Atlas", "Northbridge")))
stopifnot(weak_components$no == 3L)

cat("ANALYTICAL RESULT: directed shortest path from Travel Policy v1 to Northbridge\n")
cat("  ", paste(path_labels, collapse = " -> "), "\n", sep = "")
cat("  Total path cost: ", sum(E(graph, path = path)$weight), "\n", sep = "")
cat("  Weakly connected components: ", weak_components$no, "\n", sep = "")

# Keep the transformed table available for inspection in an interactive run.
node_summary <- tidy_graph |>
  activate(nodes) |>
  as_tibble() |>
  select(name, label, type, degree_total, in_component)
print(node_summary)
