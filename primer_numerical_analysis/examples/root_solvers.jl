# Exercise the actual published scalar solvers, including failure paths.
source_text = read("primer_numerical_analysis.md", String)
section = split(source_text, "### Shared Example: Find Root"; limit=2)[2]
code = split(split(section, "```julia\n"; limit=2)[2], "\n```"; limit=2)[1]
include_string(Main, code, "published root solvers")
macro expect_error(expr)
    quote
      let failed = false
        try
            $(esc(expr))
        catch err
            failed = err isa ErrorException
        end
        @assert failed
      end
    end
end
@assert bisection(x -> x, 0., 1.) == 0.
@assert bisection(x -> x - 1, 0., 1.) == 1.
@assert abs(bisection(x -> 1e-20 * (x - .3), 0., 1.) - .3) < 1e-12
@assert abs(newton(x -> x*x-2, x -> 2*x, 1.)^2-2) < 1e-12
@assert newton(x -> x*x, x -> 2*x, 0.) == 0.
@expect_error bisection(x -> x*x-2, 0., 2.; max_iter=1)
@expect_error newton(x -> x*x-2, x -> 2*x, 1.; max_iter=1)
@expect_error bisection(x -> x*x+1, 0., 2.)
@expect_error bisection(x -> NaN, 0., 1.)
@expect_error newton(x -> x+1, x -> 0., 0.)
