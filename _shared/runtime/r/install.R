lock <- readLines("/tmp/packages.lock", warn = FALSE)
lock <- lock[!grepl("^\\s*(#|$)", lock)]
fields <- strsplit(lock, "\\|", fixed = FALSE)
packages <- vapply(fields, `[[`, character(1), 1)
versions <- vapply(fields, `[[`, character(1), 2)
library_path <- Sys.getenv("R_LIBS_USER")
cran_repository <- Sys.getenv("R_REPOS_SNAPSHOT")
torch_repository <- "https://torch-cdn.mlverse.org/packages/cpu/0.17.0/"
dir.create(library_path, recursive = TRUE, showWarnings = FALSE)
.libPaths(c(library_path, .libPaths()))

native <- readLines("/tmp/native.lock", warn = FALSE)
native <- native[grepl("=", native) & !grepl("^\\s*#", native)]
native_values <- setNames(sub("^[^=]+=", "", native), sub("=.*$", "", native))

options(timeout = 600)
options(repos = c(torch = "https://torch-cdn.mlverse.org/packages/cpu/0.17.0/", CRAN = cran_repository))

for (i in seq_along(packages)) {
  package <- packages[[i]]
  version <- versions[[i]]
  repository <- if (package == "torch") torch_repository else cran_repository
  message(sprintf("Installing direct dependency %s %s from %s", package, version, repository))
  if (package == "torch") {
    install.packages(package, lib = library_path, repos = c(torch = torch_repository, CRAN = cran_repository))
  } else {
    install.packages(package, lib = library_path, repos = cran_repository)
  }
}

Sys.setenv(
  CUDA = "cpu",
  TORCH_URL = native_values[["libtorch_url"]],
  LANTERN_URL = native_values[["lantern_url"]]
)
torch::install_torch(timeout = 600)

installed <- installed.packages(lib.loc = library_path)
for (i in seq_along(packages)) {
  actual <- installed[packages[[i]], "Version"]
  stopifnot(actual == versions[[i]])
}
message("Installed direct dependencies:")
print(installed[packages, "Version", drop = FALSE])
