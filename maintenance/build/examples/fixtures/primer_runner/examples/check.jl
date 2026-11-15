@assert 2 + 2 == 4
@assert ENV["EXAMPLE_OUT"] == "/out"
write(joinpath(ENV["EXAMPLE_OUT"], "julia.txt"), "checked\n")
