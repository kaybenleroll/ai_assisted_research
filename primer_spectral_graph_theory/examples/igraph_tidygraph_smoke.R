library(igraph)
library(tidygraph)
library(ggraph)
library(dplyr)
library(ggplot2)

vertices <- data.frame(name = as.character(1:6))
edges <- data.frame(
  from = c("1", "2", "3", "4"),
  to = c("2", "3", "4", "5"),
  weight = c(1, 2, 1, 1)
)

g <- graph_from_data_frame(edges, directed = FALSE, vertices = vertices)
components <- components(g)
L <- as.matrix(laplacian_matrix(
  g,
  weights = E(g)$weight,
  normalization = "unnormalized",
  sparse = FALSE
))

stopifnot(components$no == 2)
stopifnot(max(abs(L - t(L))) < 1e-12)
stopifnot(max(abs(L %*% rep(1, vcount(g)))) < 1e-12)

tg <- as_tbl_graph(g) |>
  activate(nodes) |>
  mutate(
    component = components$membership,
    strength = strength(g, weights = E(g)$weight)
  )

output_dir <- Sys.getenv("EXAMPLE_OUT", unset = tempdir())
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
plot_path <- file.path(output_dir, "igraph-tidygraph-smoke.png")
png(plot_path, width = 900, height = 650, res = 120)
print(
  ggraph(tg, layout = "stress") +
    geom_edge_link(aes(width = weight), alpha = 0.35) +
    geom_node_point(aes(colour = factor(component), size = strength)) +
    theme_graph()
)
dev.off()
stopifnot(file.exists(plot_path), file.info(plot_path)$size > 0)
message(sprintf("igraph/tidygraph/ggraph smoke test passed: %s", plot_path))
