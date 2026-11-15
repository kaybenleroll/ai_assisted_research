stopifnot(2 + 2 == 4)
stopifnot(Sys.getenv("EXAMPLE_OUT") == "/out")
writeLines("checked", file.path(Sys.getenv("EXAMPLE_OUT"), "r.txt"))
