# Exercise the actual published scalar solvers, including failure paths.
source_text <- paste(readLines('primer_numerical_analysis.md', warn = FALSE), collapse = '\n')
section <- strsplit(source_text, '### Shared Example: Find Root', fixed = TRUE)[[1]][2]
code <- strsplit(strsplit(section, '```r\n', fixed = TRUE)[[1]][2], '\n```', fixed = TRUE)[[1]][1]
eval(parse(text = code))
stopifnot(bisection(function(x) x, 0, 1) == 0,
          bisection(function(x) x - 1, 0, 1) == 1,
          abs(bisection(function(x) 1e-20 * (x - .3), 0, 1) - .3) < 1e-12,
          abs(newton(function(x) x*x-2, function(x) 2*x, 1)^2-2) < 1e-12,
          newton(function(x) x*x, function(x) 2*x, 0) == 0)
expect_error <- function(expr) stopifnot(inherits(tryCatch({force(expr); NULL}, error = identity), 'error'))
expect_error(bisection(function(x) x*x-2, 0, 2, max_iter=1))
expect_error(newton(function(x) x*x-2, function(x) 2*x, 1, max_iter=1))
expect_error(bisection(function(x) x*x+1, 0, 2))
expect_error(bisection(function(x) NaN, 0, 1))
expect_error(newton(function(x) x+1, function(x) 0, 0))
