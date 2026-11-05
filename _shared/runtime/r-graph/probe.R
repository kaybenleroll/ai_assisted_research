.libPaths(c(Sys.getenv("R_LIBS_USER"), .libPaths()))
stopifnot(getRversion() == "4.5.3")

library(igraph)
library(tidygraph)
library(ggraph)
library(dplyr)
library(ggplot2)

stopifnot(packageVersion("igraph") == "2.3.0")
stopifnot(packageVersion("tidygraph") == "1.3.1")
stopifnot(packageVersion("ggraph") == "2.2.2")
stopifnot(packageVersion("dplyr") == "1.2.1")

g <- make_graph(c(1, 2, 2, 3, 4, 5), directed = FALSE, n = 5)
L <- as.matrix(laplacian_matrix(g, normalization = "unnormalized", sparse = FALSE))
stopifnot(max(abs(L - t(L))) < 1e-12)
stopifnot(max(abs(L %*% rep(1, vcount(g)))) < 1e-12)

tg <- as_tbl_graph(g) |>
  activate(nodes) |>
  mutate(component = group_components())
stopifnot(nrow(as.data.frame(tg, active = "nodes")) == 5)

message(sprintf(
  "primer-r-graph-probe: R=%s igraph=%s tidygraph=%s ggraph=%s dplyr=%s",
  getRversion(), packageVersion("igraph"), packageVersion("tidygraph"),
  packageVersion("ggraph"), packageVersion("dplyr")
))
