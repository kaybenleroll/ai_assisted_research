re <- 1000 * 0.020 * 1.0e-3 / 1.0e-3
pressure_drop <- 12 * 1.0e-3 * 0.20 * 0.020 / (1.0e-3)^2
flow_rate <- 0.020 * 20.0e-3 * 1.0e-3

stopifnot(isTRUE(all.equal(re, 20, tolerance = 1e-12)))
stopifnot(isTRUE(all.equal(pressure_drop, 48, tolerance = 1e-12)))
stopifnot(isTRUE(all.equal(flow_rate, 4.0e-7, tolerance = 1e-12)))
cat(sprintf("Re_h=%.12g pressure_drop_pa=%.12g flow_rate_m3_s=%.12g\n", re, pressure_drop, flow_rate))
