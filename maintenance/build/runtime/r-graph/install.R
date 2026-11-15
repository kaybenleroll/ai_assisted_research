lock <- readLines("/tmp/graph-packages.lock", warn = FALSE)
lock <- lock[!grepl("^\\s*(#|$)", lock)]
fields <- strsplit(lock, "\\|", fixed = FALSE)
packages <- vapply(fields, `[[`, character(1), 1)
versions <- vapply(fields, `[[`, character(1), 2)
library_path <- Sys.getenv("R_LIBS_USER")
repository <- Sys.getenv("R_REPOS_SNAPSHOT")
dir.create(library_path, recursive = TRUE, showWarnings = FALSE)
.libPaths(c(library_path, .libPaths()))
options(timeout = 600)
options(repos = c(CRAN = repository))

for (i in seq_along(packages)) {
  message(sprintf("Installing graph dependency %s %s from %s", packages[[i]], versions[[i]], repository))
  install.packages(packages[[i]], lib = library_path, repos = repository)
}

installed <- installed.packages(lib.loc = library_path)
for (i in seq_along(packages)) {
  actual <- installed[packages[[i]], "Version"]
  stopifnot(actual == versions[[i]])
}
message("Installed graph packages:")
print(installed[packages, "Version", drop = FALSE])
