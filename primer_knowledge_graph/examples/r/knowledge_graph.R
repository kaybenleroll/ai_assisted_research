# Self-contained R companion for the knowledge-graph primer.
#
# Interchange contract for integration with the Python fixture:
# use the same entity identifiers and the positive-claim projection from
# examples/fixture.json. Claims carrying negative polarity remain in the
# evidence store but are not edges in this analytical projection.

library(dplyr)
library(igraph)
library(tidygraph)

entities <- tibble::tibble(
  id = c("org:northbridge", "project:atlas", "project:orion",
         "policy:travel-v1", "policy:travel-v2", "person:morgan-lee",
         "person:alex-kim-1", "person:alex-kim-2"),
  label = c("Northbridge", "Atlas", "Orion", "Northbridge Travel Policy v1",
            "Northbridge Travel Policy v2", "Morgan Lee", "Alex Kim", "Alex Kim"),
  type = c("organisation", "project", "project", "policy_version",
           "policy_version", "person", "person", "person")
)

relations <- tibble::tibble(
  source = c("policy:travel-v1", "policy:travel-v1", "project:atlas",
             "policy:travel-v2", "project:orion"),
  target = c("project:atlas", "person:morgan-lee", "org:northbridge",
             "project:atlas", "org:northbridge"),
  type = c("applies_to", "owned_by", "belongs_to", "applies_to", "belongs_to"),
  weight = c(1, 1, 1, 1, 1)
)

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
