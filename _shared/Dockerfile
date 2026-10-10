FROM docker.io/pandoc/latex@sha256:bd7641edf35bb8fad1316bacdac15fcc15f4d8d4f89051da2edcace15a6366d8

# Add Unicode-capable fonts so box-drawing and symbol-heavy code blocks render in PDF.
RUN apk add --no-cache \
    fontconfig \
    ttf-dejavu \
    font-noto \
    font-noto-cjk \
    nodejs \
    npm \
    chromium \
  && npm install -g @mermaid-js/mermaid-cli@11.17.0 \
  && fc-cache -f

ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser
