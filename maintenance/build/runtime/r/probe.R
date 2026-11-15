.libPaths(c(Sys.getenv("R_LIBS_USER"), .libPaths()))
stopifnot(getRversion() == "4.5.3")

library(Matrix)
library(numDeriv)
library(torch)

stopifnot(packageVersion("torch") == "0.17.0")
stopifnot(packageVersion("Matrix") == "1.7.5")
stopifnot(packageVersion("numDeriv") == "2016.8.1.1")
stopifnot(trimws(readLines(system.file("build-version", package = "torch"), n = 1)) == "2.8.0+cpu")

stopifnot(isTRUE(all.equal(sum(c(1, 2, 3)^2), 14)))
matrix_result <- crossprod(Matrix(c(1, 2, 3), nrow = 3))
stopifnot(isTRUE(all.equal(as.numeric(matrix_result), 14)))

x <- torch_tensor(3, dtype = torch_float64(), requires_grad = TRUE)
y <- x^2
y$backward()
stopifnot(isTRUE(all.equal(as.numeric(x$grad), 6, tolerance = 1e-12)))

message(sprintf("primer-r-probe: R=%s torch=%s Matrix=%s numDeriv=%s", getRversion(), packageVersion("torch"), packageVersion("Matrix"), packageVersion("numDeriv")))
