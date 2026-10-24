const h = 1.0e-3
const width = 20.0e-3
const length = 0.20
const mu = 1.0e-3
const rho = 1000.0
const mean_speed = 0.020

re = rho * mean_speed * h / mu
pressure_drop = 12.0 * mu * length * mean_speed / h^2
flow_rate = mean_speed * width * h

@assert isapprox(re, 20.0; rtol=1e-12)
@assert isapprox(pressure_drop, 48.0; rtol=1e-12)
@assert isapprox(flow_rate, 4.0e-7; rtol=1e-12)
println("Re_h=$(re) pressure_drop_pa=$(pressure_drop) flow_rate_m3_s=$(flow_rate)")
