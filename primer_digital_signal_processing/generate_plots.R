# Deterministic, base-R figures for the digital signal processing primer.
# Run from any directory with:
#   Rscript --vanilla primer_digital_signal_processing/generate_plots.R

set.seed(20260915)

script_arg <- grep("^--file=", commandArgs(), value = TRUE)
script_path <- if (length(script_arg)) sub("^--file=", "", script_arg[1]) else "generate_plots.R"
script_dir <- normalizePath(dirname(script_path), mustWork = FALSE)
figure_dir <- file.path(script_dir, "figures")
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

cat("Generating DSP figures with base R...\n")

blue <- "#1769AA"
orange <- "#D95F02"
red <- "#C0392B"
ink <- "#222222"
grid_gray <- "#D9DDE2"
muted <- "#5B6570"

save_png <- function(filename, width, height, draw) {
  path <- file.path(figure_dir, filename)
  grDevices::png(path, width = width, height = height, res = 200,
                 pointsize = 10, type = "cairo-png", bg = "white")
  tryCatch(draw(), finally = grDevices::dev.off())
  size <- file.info(path)$size
  if (is.na(size) || size <= 0) stop("PNG was not written: ", path)
  cat(sprintf("  %-24s %d bytes (%d x %d px)\n", filename, size, width, height))
  invisible(path)
}

expected_pngs <- list(
  sampling_aliasing.png = c(width = 800L, height = 560L),
  dft_windowing.png = c(width = 800L, height = 580L),
  stft_tradeoff.png = c(width = 800L, height = 760L)
)

read_be32 <- function(bytes, start) {
  sum(as.numeric(bytes[start:(start + 3L)]) * c(256^3, 256^2, 256, 1))
}

check_png <- function(filename, expected) {
  path <- file.path(figure_dir, filename)
  if (!file.exists(path) || file.info(path)$size <= 0) {
    stop("PNG is missing or empty: ", path)
  }
  bytes <- readBin(path, what = "raw", n = 26L)
  signature <- as.raw(c(137, 80, 78, 71, 13, 10, 26, 10))
  if (length(bytes) < 26L || !identical(bytes[1:8], signature) ||
      rawToChar(bytes[13:16]) != "IHDR") {
    stop("Not a valid PNG/IHDR file: ", path)
  }
  width <- read_be32(bytes, 17L)
  height <- read_be32(bytes, 21L)
  bit_depth <- as.integer(bytes[25L])
  colour_type <- as.integer(bytes[26L])
  if (width != expected[["width"]] || height != expected[["height"]]) {
    stop(sprintf("Unexpected dimensions for %s: got %dx%d, expected %dx%d",
                 filename, width, height, expected[["width"]], expected[["height"]]))
  }
  if (bit_depth != 8L || !(colour_type %in% c(2L, 6L))) {
    stop(sprintf("Unexpected PNG format for %s: bit depth %d, colour type %d",
                 filename, bit_depth, colour_type))
  }
  cat(sprintf("  %-24s %d bytes (%d x %d px, PNG-8-bit-%s)\n",
              filename, file.info(path)$size, width, height,
              if (colour_type == 2L) "RGB" else "RGBA"))
}

if ("--check" %in% commandArgs(trailingOnly = TRUE)) {
  cat("Checking DSP figure artifacts...\n")
  for (filename in names(expected_pngs)) check_png(filename, expected_pngs[[filename]])
  cat("All DSP figure artifacts passed.\n")
  quit(save = "no", status = 0)
}

panel_title <- function(main, sub = NULL) {
  title(main = main, sub = sub, col.main = ink, col.sub = muted,
        font.main = 2, cex.main = 1.05, cex.sub = 0.78, mgp = c(2, 0.3, 0))
}

# -----------------------------------------------------------------------------
# 1. Sampling and aliasing: two analogue candidates, one observed sequence.
# A cosine is used so f and (fs - f) have exactly the same samples.
# -----------------------------------------------------------------------------
save_png("sampling_aliasing.png", 800, 560, function() {
  old_par <- par(no.readonly = TRUE)
  on.exit(par(old_par), add = TRUE)
  par(mfrow = c(1, 3), mar = c(4.0, 3.7, 3.2, 1.0),
      oma = c(0, 0, 2.2, 0), mgp = c(2.1, 0.65, 0), las = 1)

  fs <- 10000
  sample_t <- (0:15) / fs
  sample_y <- cos(2 * pi * 3000 * sample_t)
  t_dense <- seq(0, max(sample_t), length.out = 4000)
  y_lim <- c(-1.2, 1.2)

  plot_candidate <- function(freq, colour, subtitle) {
    plot(t_dense * 1000, cos(2 * pi * freq * t_dense), type = "l",
         lwd = 1.6, col = colour, xlim = range(sample_t * 1000), ylim = y_lim,
         xlab = "time (ms)", ylab = "amplitude", axes = FALSE)
    abline(h = 0, col = grid_gray)
    axis(1, col = muted, col.axis = ink)
    axis(2, at = c(-1, 0, 1), col = muted, col.axis = ink)
    box(col = muted)
    segments(sample_t * 1000, 0, sample_t * 1000, sample_y,
             col = "#22222255", lwd = 0.8)
    points(sample_t * 1000, sample_y, pch = 21, bg = "white", col = ink,
           cex = 0.9, lwd = 1.2)
    panel_title(sprintf("%d kHz candidate", freq / 1000), subtitle)
  }

  plot_candidate(3000, blue, "analogue curve + 10 kHz samples")
  text(0.8, 1.02, "sample values", col = ink, cex = 0.75)
  plot_candidate(7000, orange, "analogue curve + same markers")
  text(0.8, 1.02, "same samples", col = ink, cex = 0.75)

  plot(NA, xlim = c(0, 10), ylim = c(0, 1.28), xlab = "analogue frequency (kHz)",
       ylab = "interpretation", axes = FALSE)
  axis(1, at = 0:10, col = muted, col.axis = ink)
  axis(2, at = c(0.34, 0.92), labels = c("sampled", "candidates"),
       las = 1, col = muted, col.axis = ink)
  box(col = muted)
  abline(v = 5, lty = 2, col = muted)
  text(5, 1.19, "Nyquist = 5 kHz", col = muted, cex = 0.77)
  segments(c(3, 7), 0.92, c(3, 7), 1.08, lwd = 2,
           col = c(blue, orange))
  points(c(3, 7), c(0.92, 0.92), pch = 16, col = c(blue, orange), cex = 1.1)
  text(3, 1.14, "3 kHz", col = blue, cex = 0.78)
  text(7, 1.14, "7 kHz", col = orange, cex = 0.78)
  segments(7, 0.34, 3, 0.34, col = red, lwd = 1.5,
           lty = 2, lend = "butt")
  arrows(7, 0.34, 3, 0.34, length = 0.08, angle = 18,
         code = 3, col = red, lwd = 1.5)
  points(3, 0.34, pch = 16, col = red, cex = 1.1)
  text(5, 0.49, "7 kHz aliases to 3 kHz", col = red, cex = 0.82)
  text(5, 0.16, "one sequence only", col = ink, cex = 0.70)
  panel_title("aliasing interpretation", "not a reconstruction claim")
  mtext("10 kHz sampling: one sequence, two analogue candidates",
        outer = TRUE, line = 0.55, cex = 0.82, font = 2, col = ink)
})

# -----------------------------------------------------------------------------
# 2. DFT and windowing: on-bin and off-bin tones in a 1-second record.
# -----------------------------------------------------------------------------
one_sided_amplitude <- function(signal, window) {
  n <- length(signal)
  X <- fft(signal * window)
  keep <- seq_len(n %/% 2 + 1)
  a <- Mod(X[keep]) * 2 / sum(window)
  a[1] <- Mod(X[1]) / sum(window)
  if (n %% 2 == 0) a[length(a)] <- Mod(X[n / 2 + 1]) / sum(window)
  a
}

save_png("dft_windowing.png", 800, 580, function() {
  old_par <- par(no.readonly = TRUE)
  on.exit(par(old_par), add = TRUE)
  par(mfrow = c(1, 3), mar = c(4.1, 3.8, 3.3, 1.0),
      oma = c(0, 0, 2.0, 0), mgp = c(2.1, 0.65, 0), las = 1)

  fs <- 1000
  N <- 1000
  t <- (0:(N - 1)) / fs
  signal <- cos(2 * pi * 50 * t) + 0.75 * cos(2 * pi * 50.5 * t)
  rect_window <- rep(1, N)
  hann_periodic <- 0.5 - 0.5 * cos(2 * pi * (0:(N - 1)) / N)
  freq <- (0:(N / 2)) * fs / N
  db <- function(a, floor_db = -100) pmax(20 * log10(pmax(a, 1e-12)), floor_db)

  # The DFT treats the record as periodic: the last sample wraps to the first.
  tail_index <- (N - 119):N
  plot(t[tail_index] * 1000, signal[tail_index], type = "l", col = blue, lwd = 1.15,
       xlim = c(880, 1000), ylim = c(-2, 2), xlab = "record time (ms)",
       ylab = "amplitude", axes = FALSE)
  abline(h = 0, col = grid_gray)
  axis(1, at = c(880, 920, 960, 1000), col = muted, col.axis = ink)
  axis(2, at = c(-2, -1, 0, 1, 2), col = muted, col.axis = ink)
  box(col = muted)
  points(c(t[N] * 1000, 1000), c(signal[N], signal[1]),
         pch = c(16, 1), col = red, cex = 0.85)
  segments(t[N] * 1000, signal[N], 1000, signal[1],
           col = red, lty = 2, lwd = 1.8)
  abline(v = c(t[N] * 1000, 1000), col = red, lty = 3)
  text(939, 1.55, sprintf("wrap jump = %.2f", abs(signal[N] - signal[1])),
       col = red, cex = 0.75)
  text(939, 1.25, "x[N−1] → x[0]", col = red, cex = 0.75)
  panel_title("record tail + wrap", "DFT periodic-boundary mismatch")

  # Both spectral panels use amplitude 1 as the common 0 dB reference.  Do
  # not renormalise each curve to its own peak: that would hide the fact that
  # the windowed estimates are being compared on one calibrated scale.
  rect_amp <- one_sided_amplitude(signal, rect_window)
  rect_db <- db(rect_amp)
  plot(freq, rect_db, type = "l", col = blue, lwd = 1.35,
       xlim = c(35, 66), ylim = c(-90, 5), xlab = "frequency (Hz)",
       ylab = "amplitude (dB re 1)", axes = FALSE)
  abline(h = seq(-80, 0, 20), col = grid_gray, lty = 3)
  axis(1, at = seq(35, 65, 5), col = muted, col.axis = ink)
  axis(2, at = seq(-80, 0, 20), col = muted, col.axis = ink)
  box(col = muted)
  abline(v = 50, col = blue, lty = 2)
  abline(v = 50.5, col = orange, lty = 2)
  text(50, -13, "50 Hz\n(on bin)", col = blue, cex = 0.72)
  text(53.8, -28, "50.5 Hz\n(off bin)", col = orange, cex = 0.72)
  arrows(50, -84, 51, -84, length = 0.08, angle = 18,
         code = 3, col = red, lwd = 1.4)
  text(50.5, -74, "Δf = 1 Hz\n(bin spacing, not resolution)",
       col = red, cex = 0.7)
  panel_title("rectangular DFT", "50 Hz + 50.5 Hz")

  off_bin <- cos(2 * pi * 50.5 * t)
  off_rect_db <- db(one_sided_amplitude(off_bin, rect_window))
  off_hann_db <- db(one_sided_amplitude(off_bin, hann_periodic))
  plot(freq, off_rect_db, type = "l", col = blue, lwd = 1.25,
       xlim = c(35, 66), ylim = c(-90, 5), xlab = "frequency (Hz)",
       ylab = "amplitude (dB re 1)", axes = FALSE)
  lines(freq, off_hann_db, col = orange, lwd = 1.25)
  abline(h = seq(-80, 0, 20), col = grid_gray, lty = 3)
  axis(1, at = seq(35, 65, 5), col = muted, col.axis = ink)
  axis(2, at = seq(-80, 0, 20), col = muted, col.axis = ink)
  box(col = muted)
  abline(v = 50.5, col = red, lty = 2)
  legend("topright", legend = c("rectangular", "periodic Hann"),
         col = c(blue, orange), lwd = 1.4, bty = "n", cex = 0.73)
  text(50.5, -15, "tone = 50.5 Hz", col = red, cex = 0.73)
  panel_title("window leakage", "off-bin tone, dB scale")
  mtext("N = 1000, fs = 1000 Hz; both spectra share 0 dB = amplitude 1",
        outer = TRUE, line = 0.43, cex = 0.73, font = 2, col = ink)
})

# -----------------------------------------------------------------------------
# 3. STFT time-frequency trade-off for a short two-tone burst.
# -----------------------------------------------------------------------------
stft <- function(signal, fs, window_length, hop, nfft) {
  window <- 0.5 - 0.5 * cos(2 * pi * (0:(window_length - 1)) / window_length)
  starts <- seq.int(1, length(signal) - window_length + 1, by = hop)
  frame_time <- (starts - 1 + (window_length - 1) / 2) / fs
  freq <- (0:(nfft / 2)) * fs / nfft
  amplitude <- matrix(0, nrow = length(freq), ncol = length(starts))
  for (j in seq_along(starts)) {
    ind <- starts[j]:(starts[j] + window_length - 1)
    # Base R's fft() has no length argument; append zeros for the requested FFT size.
    X <- fft(c(signal[ind] * window, rep(0, nfft - window_length)))
    a <- Mod(X[seq_len(nfft / 2 + 1)]) * 2 / sum(window)
    a[1] <- Mod(X[1]) / sum(window)
    a[length(a)] <- Mod(X[nfft / 2 + 1]) / sum(window)
    amplitude[, j] <- a
  }
  list(time = frame_time, freq = freq, amplitude = amplitude, window = window)
}

save_png("stft_tradeoff.png", 800, 760, function() {
  old_par <- par(no.readonly = TRUE)
  on.exit(par(old_par), add = TRUE)
  par(mfrow = c(2, 2), mar = c(3.5, 3.7, 3.1, 1.0),
      oma = c(0, 0, 3.0, 0), mgp = c(2.0, 0.6, 0), las = 1)

  fs <- 16000
  duration <- 1
  t <- (0:(fs * duration - 1)) / fs
  burst <- as.numeric(t >= 0.45 & t < 0.55)
  signal <- burst * (sin(2 * pi * 500 * t) + 0.9 * sin(2 * pi * 600 * t))
  short <- stft(signal, fs, window_length = 256, hop = 32, nfft = 2048)
  long <- stft(signal, fs, window_length = 1024, hop = 128, nfft = 2048)
  global_peak <- max(c(short$amplitude, long$amplitude))
  to_db <- function(a) pmax(20 * log10(pmax(a / global_peak, 1e-12)), -80)
  short_db <- to_db(short$amplitude)
  long_db <- to_db(long$amplitude)
  colours <- grDevices::colorRampPalette(c("#081D58", "#225EA8", "#41B6C4",
                                             "#A1DAB4", "#FFFFCC"))(161)
  draw_spectrogram <- function(obj, z, title_text) {
    keep <- obj$freq <= 1200
    time_keep <- obj$time >= 0.35 & obj$time <= 0.65
    image(x = obj$time[time_keep], y = obj$freq[keep], z = t(z[keep, time_keep]),
          col = colours, zlim = c(-80, 0), useRaster = TRUE,
          xlim = c(0.35, 0.65), ylim = c(0, 1200),
          xlab = "time (s)", ylab = "frequency (Hz)", axes = FALSE)
    axis(1, at = seq(0.35, 0.65, 0.05), col = muted, col.axis = ink)
    axis(2, at = seq(0, 1200, 200), col = muted, col.axis = ink)
    box(col = muted)
    abline(v = c(0.45, 0.55), col = "white", lty = 2, lwd = 1.1)
    abline(h = c(500, 600), col = "white", lty = 2, lwd = 0.8)
    text(0.59, 1130, "shared scale\n−80 to 0 dB", col = ink, cex = 0.62,
         adj = c(1, 1))
    panel_title(title_text)
  }

  plot(t, signal, type = "l", col = blue, lwd = 0.8,
       xlim = c(0.40, 0.60), ylim = c(-2, 2), xlab = "time (s)",
       ylab = "amplitude", axes = FALSE)
  abline(h = 0, col = grid_gray)
  axis(1, at = seq(0.40, 0.60, 0.05), col = muted, col.axis = ink)
  axis(2, at = c(-2, -1, 0, 1, 2), col = muted, col.axis = ink)
  box(col = muted)
  abline(v = c(0.45, 0.55), col = red, lty = 2, lwd = 1.1)
  text(0.50, 1.55, "500 + 600 Hz burst", col = red, cex = 0.82)
  text(0.45, -1.72, "onset", col = red, cex = 0.67, pos = 2)
  text(0.55, -1.72, "offset", col = red, cex = 0.67, pos = 4)
  panel_title("waveform: 0.45–0.55 s burst")

  draw_spectrogram(short, short_db,
                   "short: 256 samples (16 ms)\ntime focus (~125 Hz)")
  draw_spectrogram(long, long_db,
                   "long: 1024 samples (64 ms)\nfrequency focus (~31 Hz)")

  short_frame <- which.min(abs(short$time - 0.50))
  long_frame <- which.min(abs(long$time - 0.50))
  short_frame_db <- to_db(short$amplitude[, short_frame])
  long_frame_db <- to_db(long$amplitude[, long_frame])
  keep_short <- short$freq <= 1200
  keep_long <- long$freq <= 1200
  plot(short$freq[keep_short], short_frame_db[keep_short], type = "l",
       col = blue, lwd = 1.3, xlim = c(350, 750), ylim = c(-80, 2),
       xlab = "frequency (Hz)", ylab = "amplitude (dB re common peak)", axes = FALSE)
  lines(long$freq[keep_long], long_frame_db[keep_long], col = orange, lwd = 1.3)
  abline(h = seq(-80, 0, 20), col = grid_gray, lty = 3)
  axis(1, at = seq(350, 750, 50), col = muted, col.axis = ink)
  axis(2, at = seq(-80, 0, 20), col = muted, col.axis = ink)
  box(col = muted)
  abline(v = c(500, 600), col = red, lty = 2)
  legend("topright", legend = c("256 samples", "1024 samples"),
         col = c(blue, orange), lwd = 1.4, bty = "n", cex = 0.72)
  text(500, -15, "500", col = red, cex = 0.68)
  text(600, -15, "600", col = red, cex = 0.68)
  panel_title("frame spectra near 0.50 s")

  mtext("STFT time-frequency trade-off",
        outer = TRUE, line = 1.45, cex = 0.9, font = 2, col = ink)
  mtext("short windows localise time; long windows separate frequency",
        outer = TRUE, line = 0.43, cex = 0.78, col = muted)
})

cat("Done: exactly three requested PNG outputs were generated.\n")
