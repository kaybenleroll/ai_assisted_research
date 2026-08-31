# Hermes Agent Server: A Long-Form, Operations-First Primer

---

*Long-form edition · 22 August 2026*

---

## Why This Primer Exists

Hermes Agent is easy to misclassify. It is described as a personal AI assistant, a coding agent, a messaging bot, a desktop application, an OpenAI-compatible server, and a self-improving agent runtime. All of those descriptions point at real parts of the project, but they do not describe the same process. The most expensive operational mistakes come from treating the commands as interchangeable.

This primer resolves that ambiguity first. `hermes gateway` is the long-running messaging gateway. The OpenAI-compatible API server is an HTTP interface that normally listens on `127.0.0.1:8642` when enabled and is normally started alongside the gateway. `hermes serve` is the headless JSON-RPC/WebSocket backend used by Hermes Desktop and remote desktop-style clients; it is commonly reached on port `9119`. These are related Hermes surfaces, but starting one does not automatically start the others.

The official project is [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), documented at [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/docs/). This document describes the upstream project as of 22 August 2026. Hermes changes quickly, so treat command help and the linked upstream pages as the authority when a local installation disagrees with an example here.

### What This Primer Covers

You will learn what Hermes Agent is and is not, how its processes fit together, how to install and configure it, where it keeps state, how providers, models, memory, skills, profiles, and terminal backends work, and how to operate it safely. You will also get runnable examples for the three server surfaces, Docker and Podman deployment patterns, backup and recovery runbooks, and a comparison with OpenClaw.

The emphasis is on the operational boundary: what receives input, what chooses a model, what can execute commands, what persists, and what must be protected.

### What This Primer Is Not

This is not a model benchmark, a complete catalog of every messaging adapter, or a replacement for provider documentation. Hermes Agent is not the same thing as the [Nous Hermes model family](https://huggingface.co/NousResearch); here, “Hermes” means the agent runtime and its server surfaces. It is also not a promise that a model can safely execute any action it proposes. Tool policy, filesystem permissions, network exposure, and human approval remain your responsibility.

## What Hermes Agent Is Used For

Hermes Agent is an open-source, tool-using agent runtime from Nous Research. It puts a model in a loop with tools, persistent instructions, session history, skills, and optional memory providers. You can use it interactively in a terminal, expose it through a desktop application, connect it to messaging platforms, or embed it behind an OpenAI-shaped HTTP client.

The important mental model is not “a chatbot with many frontends.” It is “one agent runtime with several ingress and control surfaces.” A Telegram message, a CLI prompt, an OpenAI-compatible request, and a Desktop chat can all reach an agent configured with the same profile, but each surface has a different protocol, lifecycle, authentication story, and set of assumptions about the caller.

### Jobs Hermes performs in practice

Hermes can draft and revise documents, inspect repositories, run development commands, search the web, use browser or computer-use tools, remember compact user preferences, follow procedural skills, and send results back through a messaging channel. A profile can be shaped into a coding assistant, research assistant, homelab operator, customer-support bot, or narrowly scoped internal worker.

The value increases when the task has continuity. A one-shot completion does not need session storage, a profile, or a gateway. A coding assistant that should remember repository conventions, use the same terminal workspace, and answer from Telegram does.

### What Hermes is not

Hermes is not a model server in the sense of Ollama, vLLM, or llama.cpp. It consumes providers and model endpoints; it does not replace the inference engine behind them. It can expose an OpenAI-compatible API, but that does not mean it serves model weights or becomes a general-purpose inference router with every provider model listed at `/v1/models`.

Hermes is not only a desktop UI. Desktop launches or connects to a headless `hermes serve` backend. The Electron/React surface is a client of that backend, not the agent runtime itself.

Hermes is not the messaging gateway. The gateway is one long-running process within the larger system. Running `hermes serve` will not connect Telegram or Discord; running `hermes gateway` will not make the Desktop JSON-RPC backend appear on port 9119.

Hermes is not a security boundary by itself. Model output is untrusted input. The terminal backend, OS account, container permissions, API bind address, messaging allowlists, and review gates determine the blast radius.

## The Three Server Surfaces You Must Keep Separate

Start with this table whenever you are diagnosing “the Hermes server.”

| Surface | Command/process | Protocol and usual port | Primary client | What it does not do |
|---|---|---|---|---|
| Messaging gateway | `hermes gateway` or `hermes gateway run` | Platform adapters; the API server may share this process | Telegram, Discord, Slack, WhatsApp, and other adapters | It is not the Desktop JSON-RPC backend |
| OpenAI-compatible API server | Enabled with `API_SERVER_ENABLED=true`; usually launched with the gateway | HTTP, usually `127.0.0.1:8642` | Open WebUI, LobeChat, curl, SDKs, automation | It is not a model-weight server and does not use the Desktop WS protocol |
| Headless backend | `hermes serve` | JSON-RPC over WebSocket plus HTTP support, commonly `127.0.0.1:9119` | Hermes Desktop and remote desktop-style clients | It does not configure or poll messaging platforms |

The [official API Server guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server/) documents the HTTP surface. The [Desktop guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/desktop.md) describes the headless `hermes serve` process and its `tui_gateway` JSON-RPC/WebSocket API. The [gateway internals guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/gateway-internals.md) describes the messaging process.

### A common failure sequence

Suppose Desktop says it cannot connect, but Telegram works. Do not restart the Telegram gateway repeatedly: inspect the `hermes serve` process, its port, its authentication, and the Desktop connection target. Conversely, if Desktop works but Telegram is silent, inspect `hermes gateway status`, platform credentials, pairing, and adapter logs. If Open WebUI reports connection refused on `8642`, check that the API server is enabled and that you did not start only `hermes serve`.

The port numbers are defaults and conventions, not a substitute for observing the process startup line. Profiles and container deployments can require distinct API ports. A Desktop backend may choose an available port when launched by the app. Always use the printed readiness line or the configured bind address as the final answer.

## How People Actually Use Hermes

### Pattern A: Single-user terminal agent

Start with the CLI or terminal UI on one machine, one profile, one provider, and the local terminal backend. This gives you a small failure surface while you learn how the agent uses tools, writes memory, and edits skills. It is the right place to establish a safe working directory and decide whether local execution is acceptable.

### Pattern B: Desktop client with a headless backend

Hermes Desktop provides a richer chat surface while `hermes serve` owns the agent runtime. The backend can be local or remote. A remote setup commonly runs `hermes serve` on a server reachable over a private network or VPN, while the desktop client connects to its JSON-RPC/WebSocket endpoint. Messaging remains separate: start a gateway independently if you also want Telegram or Discord.

### Pattern C: OpenAI-compatible application backend

The API server lets an existing OpenAI-shaped client use Hermes as an agent backend. This is useful for Open WebUI, LobeChat, internal tools, CI jobs, and small scripts. Unlike a plain model endpoint, the request can invoke Hermes tools, so the endpoint must be treated as an automation control plane, not just a text-generation URL.

### Pattern D: Multi-channel personal assistant

The gateway connects multiple adapters at once, routes platform messages into profile-scoped sessions, runs scheduled jobs, and delivers responses. It is convenient, but convenience increases the importance of allowlists, pairing, per-channel toolsets, and a deliberate terminal backend. A bot that can run shell commands is not safe merely because its chat channel is private.

### Pattern E: Role-separated profiles

Use a research profile, coding profile, and personal profile instead of overloading one memory and one personality. Profiles isolate API credentials, `SOUL.md`, skills, memory, sessions, cron jobs, and gateway state. They are also an operational boundary: never run two writers against the same Hermes home.

## Hermes Architecture in One Mental Model

Think in layers: client surface, transport, agent loop, provider, tools, and state.

The client surface is the CLI/TUI, Desktop, dashboard, messaging adapter, or API client. The transport layer turns that interaction into a local call, HTTP request, platform event, or JSON-RPC/WebSocket message. The agent loop assembles instructions and history, chooses a provider/model, asks for the next step, validates tool calls, executes approved tools, and repeats until it can answer. The provider layer handles model authentication and protocol differences. The tool layer includes terminal execution, web and browser capabilities, file operations, skills, memory, MCP integrations, and platform-specific actions. The state layer persists configuration, credentials, sessions, memory, skills, logs, and profile metadata.

This model prevents category errors. A malformed tool call is usually a provider/model or tool-schema issue, not a gateway-port issue. A message from an unknown Telegram user is an authorization issue, not a memory issue. A Desktop connection refusal is a backend lifecycle or network issue, not proof that the model provider is down.

### The process relationships

The normal relationships look like this:

```text
CLI / TUI             \\
Hermes Desktop         +--> agent runtime --> provider/model
OpenAI client -- HTTP /
Messaging platform ----> agent runtime --> tools and terminal backend
                         agent runtime --> profile-scoped state

hermes gateway  = messaging adapters + sessions + optional API server
hermes serve    = headless JSON-RPC/WebSocket backend for Desktop clients
```

The gateway and `serve` share runtime concepts and state conventions, but they are separate long-running surfaces. A server may run both, but do not infer that one command supervises the other unless your service manager or container definition explicitly does so.

## Installation and First Bring-Up

The supported installation path is documented in [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation). On non-Windows systems the installer expects Git; Linux installs may also need `curl` and `xz-utils`. The installer provisions its managed Python and Node-related dependencies rather than asking you to build a hand-maintained system environment.

Run the official installer from a shell you trust. If you prefer to inspect downloaded scripts before execution, fetch the script to a temporary file, read it, and then run it according to the upstream instructions.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

For a headless host that does not need browser automation, the official installer supports skipping the browser setup:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --skip-browser
```

Verify the launcher before configuring a provider:

```bash
hermes version
hermes doctor
```

The interactive setup wizard covers model, terminal, gateway, tool, and agent configuration. The Portal path is the shortest way to configure a provider plus the Nous tool gateway when you have a Portal account:

```bash
hermes setup --portal
```

For a more targeted setup, use the surface-specific commands:

```bash
hermes model
hermes config set terminal.backend docker
hermes gateway setup
hermes tools
```

A clean first run should establish four facts: which profile is active, which provider/model answers a simple prompt, where terminal commands execute, and which server surface you intend to keep running. Do not start with every messaging adapter and every optional tool enabled.

### Source checkout for development

If you are modifying Hermes itself, use the [repository's development instructions](https://github.com/NousResearch/hermes-agent) and its managed environment. A source checkout is not the same as a production installation: the installed launcher must use the project virtual environment, and updates may alter both Python and Node dependencies. Run `hermes doctor` after changes and pin the commit or image tag for reproducible deployments.

## Configuration and State Under `~/.hermes`

The default Hermes home is `~/.hermes`. A profile changes the effective home through `HERMES_HOME`; the same layout then appears under `~/.hermes/profiles/<name>/`. The [Configuration guide](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) gives the current directory map.

```text
~/.hermes/
|-- config.yaml       # non-secret behavior and model/tool settings
|-- .env              # API keys, bot tokens, and other secrets
|-- auth.json         # OAuth/provider credentials when used
|-- SOUL.md           # primary identity and operating instructions
|-- memories/         # MEMORY.md and USER.md
|-- skills/           # bundled, installed, and agent-created skills
|-- sessions/         # session data and transcripts
|-- state.db          # canonical SQLite session/state store where present
|-- cron/             # scheduled job definitions and state
|-- logs/             # agent, gateway, and error logs
|-- plugins/          # installed Hermes plugins
`-- profiles/         # named profile homes
```

The exact tree grows with enabled features. Desktop themes, desktop plugins, TUI widgets, browser caches, checkpoints, knowledge stores, and tool-specific state can also live below the Hermes home. Back up the actual home rather than relying on a hand-written list.

Keep the separation simple: secrets belong in `.env` or the platform's secret mechanism; ordinary behavior belongs in `config.yaml`. Set restrictive permissions on the home and `.env`:

```bash
chmod 700 ~/.hermes
chmod 600 ~/.hermes/.env ~/.hermes/auth.json 2>/dev/null || true
```

Do not confuse `HERMES_HOME` with the operating-system `HOME`. `HERMES_HOME` selects the Hermes profile and therefore its config, memory, sessions, skills, logs, and gateway state. Host terminal subprocesses normally retain the real OS user's `HOME` so `git`, `ssh`, `gh`, npm, cloud CLIs, Claude Code, and Codex can find existing credentials. Set `terminal.home_mode: profile` only when you intentionally want a separate subprocess home, and then initialize those credentials inside the profile home.

## Providers and Models

Hermes separates the agent runtime from the provider that supplies model inference. Providers can be hosted APIs, Nous Portal, OpenAI-compatible endpoints, local model servers, or provider-specific integrations. The exact provider list changes; use the [current model configuration guide](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models/) and `hermes setup model` for the live inventory.

The setup wizard is safer than guessing provider-specific YAML keys. A generic environment-based example looks like this:

```bash
cat >> ~/.hermes/.env <<'EOF'
OPENAI_API_KEY="replace-with-a-secret"
OPENAI_BASE_URL="https://api.example.test/v1"
EOF

hermes config set model.default "openai-compatible/model-name"
hermes doctor
```

For local OpenAI-compatible servers, keep the endpoint on loopback until you have deliberately designed authentication and network access. LM Studio commonly uses `http://127.0.0.1:1234/v1`; vLLM and SGLang often use an OpenAI-shaped endpoint configured through `OPENAI_BASE_URL`. A placeholder API key may still be required by the client library even when the local server ignores it.

Model selection affects more than prose quality. Tool-call formatting, context length, reasoning behavior, latency, cost, vision support, and provider rate limits all affect the agent loop. A model that looks good on a chat benchmark can still fail because it emits invalid tool arguments or loses the current working directory after a long tool trace.

### Provider fallback and model overrides

Configure a default model for normal work, then add a deliberate fallback policy if unattended operation matters. Test fallbacks by disabling the primary provider; do not assume a configured fallback is healthy just because its name parses.

OpenAI-compatible clients often send a hard-coded model such as `gpt-4o`. Hermes intentionally treats a bare model value conservatively on `/v1/chat/completions` and `/v1/responses`: unless direct model requests are enabled, the gateway can ignore that generic name and use its configured default. A request with an explicit Hermes provider, or Hermes-native run/session APIs, follows the documented routing rules. This avoids accidental provider bypass by clients that hard-code a model field.

The API server's `GET /v1/models` is intentionally minimal. It advertises the Hermes-facing model name that a frontend needs; it is not the complete provider/model picker. Hermes-aware clients can use `/api/model/options` for richer provider-aware metadata.

## Memory: Curated Continuity, Not an Infinite Transcript

Hermes has bounded built-in memory. The default memory files are `~/.hermes/memories/MEMORY.md` for durable agent notes and `USER.md` for user preferences. They are compact and injected as a snapshot at session start, not treated as an unlimited conversation transcript. The [Persistent Memory guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/) documents the current limits and controls.

```yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
  memory_char_limit: 2200
  user_char_limit: 1375
  write_approval: true
```

With `write_approval: true`, foreground interactive writes can ask for approval and non-interactive or messaging writes can be staged for review. This is useful when memory is valuable but an unattended agent must not silently turn a transient instruction into durable behavior.

Hermes also supports external memory provider plugins. The [Memory Providers guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers/) describes providers such as Honcho, Mem0, Hindsight, OpenViking, Holographic, RetainDB, ByteRover, and Supermemory. Only one external provider is active at a time, while built-in memory remains active alongside it. External memory creates another availability, privacy, and backup dependency; document where the data lives before enabling it.

Do not run two agent processes against one Hermes home. Both can write memory, and each can load the other's writes into its next system prompt. Use profiles for independent agents and an external memory provider when deliberate sharing is required.

## Skills: Procedural Knowledge with a Write Boundary

Skills are on-demand knowledge documents, normally `SKILL.md` files under `~/.hermes/skills/`. Hermes reads short descriptions cheaply and loads a skill's full procedure when the task needs it. This progressive disclosure pattern lets you add detailed workflows without injecting every instruction into every request.

The [Skills System guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) describes bundled, installed, external, and agent-created skills. External directories can be configured when a team maintains a shared skill tree:

```yaml
skills:
  external_dirs:
    - ~/.agents/skills
    - /home/shared/team-skills
```

External directories are not automatically read-only. If the Hermes process can write them, an agent-managed skill update can change them. For a higher-control profile, enable the skill write gate:

```yaml
skills:
  write_approval: true
```

Then review pending changes with the documented `/skills pending`, `/skills diff`, `/skills approve`, and `/skills reject` commands. Treat skill content as executable policy: a malicious or careless skill can tell the model to exfiltrate secrets, weaken a terminal boundary, or approve a dangerous workflow.

## Terminal Backends and Security

The terminal backend determines where commands execute. Hermes currently supports local, Docker, SSH, Modal, Daytona, Vercel Sandbox, and Singularity/Apptainer backends. The [Terminal Backend section of Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) is the reference for options and optional dependencies.

| Backend | Execution location | Isolation posture | Good default use |
|---|---|---|---|
| `local` | The Hermes host | None beyond the OS account | Personal development with trusted prompts |
| `docker` | A persistent container | Namespaces, caps, resource controls | Unattended or untrusted tool loops |
| `ssh` | A remote host | Network and account boundary | Keep the gateway away from the work machine |
| `modal` / `daytona` / `vercel_sandbox` | Managed cloud workspace | Provider-managed sandbox | Ephemeral or scalable execution |
| `singularity` | HPC container | Cluster-compatible containment | Shared research/HPC environments |

The local backend is convenient and dangerous because a successful tool call is a real host command. Set a narrow `terminal.cwd`, run Hermes as a non-root account, avoid mounting sensitive directories, and do not place broad cloud credentials in the process environment.

For a container backend, start with a deliberately limited configuration:

```yaml
terminal:
  backend: docker
  cwd: /workspace
  timeout: 180
  docker_image: python:3.12-slim
  docker_mount_cwd_to_workspace: false
  docker_run_as_host_user: true
  docker_network: false
  container_cpu: 2
  container_memory: 2048
```

The exact resource key names can evolve; check `hermes config` and the current guide before applying a large policy file. Mounting the current working directory into `/workspace` is an explicit access grant. Forwarding `GITHUB_TOKEN`, `NPM_TOKEN`, or cloud credentials is also an explicit access grant. Only forward variables the terminal workload actually needs.

SSH can provide a cleaner boundary than local execution:

```yaml
terminal:
  backend: ssh
  cwd: /srv/hermes-work
```

```dotenv
TERMINAL_SSH_HOST=agent-worker.example.internal
TERMINAL_SSH_USER=hermes
TERMINAL_SSH_KEY=~/.ssh/hermes_agent_key
```

The gateway host then holds messaging and provider credentials while the worker host holds the project files. This does not make the model trusted; it limits where a bad command can run.

### Security baseline

Use platform allowlists and pairing rather than `GATEWAY_ALLOW_ALL_USERS=true`. Keep API and dashboard listeners on loopback unless you have an authenticated reverse proxy or private network. Give every externally reachable API server a strong bearer key. Use dashboard authentication for a non-loopback bind; the current Docker documentation explicitly fails closed for an unauthenticated public dashboard, and the old insecure bypass is not a safe deployment mechanism.

Keep `.env`, `auth.json`, and backups private. Review skills and `SOUL.md` like code. Enable memory and skill write approval for unattended or multi-user deployments. Turn on tool-loop hard stops for gateways that cannot be watched interactively:

```yaml
tool_loop_guardrails:
  hard_stop_enabled: true
  hard_stop_after:
    exact_failure: 5
    idempotent_no_progress: 5
```

The model should never be the only approval layer for sending messages, deleting files, changing credentials, or modifying a deployment.

## Profiles: Separate Agents Without Separate Installs

A profile is an independent Hermes home. It gives a coding agent and a research agent different configuration, credentials, personality, skills, memory, sessions, cron jobs, and gateway state while sharing the installed runtime.

```bash
hermes profile create coder
hermes profile create researcher --description "Reads source and external docs, writes findings."

hermes -p coder setup model
hermes -p coder config set terminal.cwd /home/me/src
hermes -p coder chat

hermes -p researcher config set terminal.cwd /home/me/research
hermes -p researcher chat
```

The profile guide explains that profile commands use `HERMES_HOME` internally. The default profile is the root `~/.hermes`; named profiles live below `~/.hermes/profiles/`. `HOME` remains the OS account home by default, which is why two profiles can intentionally share normal CLI credentials unless you opt into `terminal.home_mode: profile`.

Profile gateways need distinct lifecycle and port planning. Inside the official Docker image, s6 supervises multiple profile gateways in one container. The API server still needs a distinct `API_SERVER_PORT` per profile if more than one profile exposes it. The headless `serve` backend can serve a profile selected by its client/session model; do not assume that it gives every API client a separate 8642 listener.

## Messaging with `hermes gateway`

The [Messaging Gateway guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging) describes a single background gateway that can connect configured adapters such as Telegram, Discord, Slack, WhatsApp, Signal, Matrix, email, Home Assistant, Microsoft Teams, and many others. The gateway owns platform connections, per-chat sessions, typing/streaming behavior where supported, scheduled jobs, and outbound delivery.

Configure adapters through the wizard:

```bash
hermes gateway setup
hermes gateway start
hermes gateway status
```

For debugging, run it in the foreground:

```bash
hermes gateway
```

For a user-level service on a long-lived host, use the documented install path and enable lingering if the service account must run after logout:

```bash
hermes gateway install
loginctl enable-linger "$USER"
hermes gateway restart
```

The exact environment variable depends on the platform. Keep tokens in `${HERMES_HOME:-~/.hermes}/.env`, and use platform-specific allowlists or pairing. `hermes send` is a useful distinction: for many bot-token platforms it can call the platform REST endpoint directly and exit, so an inbound gateway process is not always required for an outbound one-shot message.

Do not expose the gateway's platform credentials to a second container that shares the same home. Do not run two gateways against one profile. Session files, memory, and gateway state are designed for one active writer.

## The OpenAI-Compatible API Server on Port 8642

The API server is an HTTP adapter for applications that already speak the OpenAI format. It is not `hermes serve`, and it is not a replacement for `hermes gateway`. The current [API Server documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server/) describes Chat Completions, Responses, run lifecycle endpoints, health checks, approvals, steering, and model discovery.

Enable it in the profile's secrets/config environment and start the gateway process that hosts it:

```bash
cat >> ~/.hermes/.env <<'EOF'
API_SERVER_ENABLED=true
API_SERVER_KEY="replace-with-a-long-random-secret"
# API_SERVER_HOST=127.0.0.1 is the safe default
# API_SERVER_PORT=8642 is the normal default
EOF

hermes gateway
```

Test the endpoint from the same host:

```bash
curl http://127.0.0.1:8642/v1/chat/completions \
  -H "Authorization: Bearer replace-with-a-long-random-secret" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "hermes-agent",
    "messages": [{"role": "user", "content": "Reply with one short health check."}],
    "stream": false
  }'
```

The main compatibility routes include:

```text
POST /v1/chat/completions     OpenAI Chat Completions, including SSE streaming
POST /v1/responses            OpenAI Responses-style stateful requests
POST /v1/runs                 Start a Hermes-native run
GET  /v1/runs/{id}             Inspect a run
GET  /v1/runs/{id}/events      Stream run events
POST /v1/runs/{id}/approval    Resolve an approval pause
POST /v1/runs/{id}/steer       Inject guidance at a tool boundary
POST /v1/runs/{id}/stop        Stop a run
GET  /v1/models                Minimal advertised model list
GET  /health                   Cheap liveness check
GET  /health/detailed          Authenticated readiness information
```

The HTTP API can invoke terminal, file, web, memory, and skill tools. That makes an API key equivalent to permission to drive an agent, subject to the profile's tool and terminal policy. Keep the default bind at `127.0.0.1`, tunnel it over SSH when practical, and use a narrow CORS allowlist only for browser clients. If you bind `0.0.0.0`, require `API_SERVER_KEY`, put the service behind a private network or authenticated reverse proxy, and do not rely on CORS as authentication.

Port conflicts are especially common with profiles and containers. Give each API-enabled profile its own port, publish each port explicitly, and keep per-profile environment variables in the profile's own `.env` rather than setting one container-wide value for every profile.

## `hermes serve`: Desktop and Headless JSON-RPC/WebSocket Backend

`hermes serve` launches the headless backend used by Hermes Desktop and remote desktop-style clients. It serves the `tui_gateway` JSON-RPC/WebSocket protocol and related HTTP endpoints. Desktop launches this process locally by default or connects to a remote one when configured. It does not open the browser dashboard and does not configure messaging adapters.

Run it directly when you need a backend for a remote Desktop client or want to debug the backend independently of Electron:

```bash
hermes serve
```

On current installations the common listener is `127.0.0.1:9119`, but the process startup output is authoritative. A Desktop-managed backend may choose another available port and announces readiness in a line such as `HERMES_BACKEND_READY port=...`. Use `hermes serve --help` for the runtime flags supported by the installed version.

The web dashboard is a related but different client surface. `hermes dashboard` starts the browser dashboard backend and UI; `hermes serve` shares the server foundation but selects the headless path. A dashboard or `serve` backend does not start `hermes gateway`, and the messaging gateway does not make a Desktop WebSocket client available.

Treat a remote `serve` endpoint as an administrative agent backend. Protect it with the current dashboard/auth configuration, bind it to a private interface or VPN, and do not publish `9119` directly to the public internet. If a reverse proxy terminates TLS, preserve WebSocket upgrades and forward the authentication mechanism expected by the installed Hermes version.

## Docker and Podman Considerations

There are two different container questions:

1. **Run Hermes inside a container.** The official image stores the agent's mutable data under `/opt/data`, normally backed by a host `~/.hermes` mount.
2. **Use a container as the terminal backend.** Hermes itself runs on the host, while tool commands execute in a persistent sandbox container.

Confusing these leads to missing state or an accidentally unsandboxed terminal. The [official Docker guide](https://hermes-agent.nousresearch.com/docs/user-guide/docker/) covers both patterns.

### Run the official image

The official Docker image uses `nousresearch/hermes-agent`. Configure the mounted home first:

```bash
mkdir -p ~/.hermes
docker run --rm -it \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent setup
```

Run a supervised gateway with the API server port published:

```bash
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 127.0.0.1:8642:8642 \
  nousresearch/hermes-agent gateway run
```

To run the dashboard alongside the gateway, enable it and publish the common backend port:

```bash
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 127.0.0.1:8642:8642 \
  -p 127.0.0.1:9119:9119 \
  -e HERMES_DASHBOARD=1 \
  nousresearch/hermes-agent gateway run
```

The image is intended to be upgraded independently of `/opt/data`. Keep the image tag pinned for production rather than accepting an unreviewed `latest` update. The official image now supervises gateway services with s6; inspect `docker logs` and the mounted profile logs when debugging, and remember that two containers must never write the same Hermes home concurrently.

### Podman

Rootless Podman is a reasonable Docker-compatible runtime for the official image, but validate the exact image, networking, user namespace, and volume behavior in your environment. Use `podman` in place of `docker`, publish loopback addresses explicitly, and add `:Z` on SELinux systems when the host policy requires relabeling:

```bash
podman run -d \
  --name hermes \
  --replace \
  -v "$HOME/.hermes:/opt/data:Z" \
  -p 127.0.0.1:8642:8642 \
  nousresearch/hermes-agent gateway run
```

Rootless UID mapping can make a mounted directory appear owned by an unexpected host UID. Check `podman unshare`, the directory permissions, and the runtime user before blaming Hermes. If Hermes uses a container terminal backend, the configuration can select the runtime binary with the documented `HERMES_DOCKER_BINARY` override; test whether the installed Hermes version accepts Podman for every Docker-specific option you enable.

Do not assume a rootless container has access to the host Docker socket, GPU, audio devices, or browser sandbox. Grant those resources explicitly, and document the resulting security tradeoff. For a remote Desktop backend, publish or proxy the `serve` port separately from the API port; publishing `8642` does not make the JSON-RPC/WebSocket backend available.

### Compose shape

The official Docker example uses a persistent data volume and can expose both common ports:

```yaml
services:
  hermes:
    image: nousresearch/hermes-agent:latest
    container_name: hermes
    restart: unless-stopped
    command: gateway run
    ports:
      - "127.0.0.1:8642:8642"
      - "127.0.0.1:9119:9119"
    volumes:
      - "${HOME}/.hermes:/opt/data"
    environment:
      HERMES_DASHBOARD: "1"
```

For production, replace `latest` with a real release tag available from the project and test the upgrade before rollout. Do not copy `API_SERVER_KEY` into a committed Compose file; keep it in the mounted `.env` or your secret manager.

## Operations and Day-2 Diagnostics

Use the smallest diagnostic surface that answers the question:

```bash
hermes version
hermes doctor
hermes config show
hermes profile list
hermes gateway status
hermes logs --follow
```

For API clients, test liveness before testing a model:

```bash
curl -fsS http://127.0.0.1:8642/health
curl -fsS http://127.0.0.1:8642/v1/models \
  -H "Authorization: Bearer $API_SERVER_KEY"
```

For Desktop, verify the `hermes serve` process and the exact readiness port before inspecting model credentials. Check the desktop log and the backend log for authentication failures, WebSocket upgrade failures, stale process IDs, or a port already in use.

For a messaging incident, check in this order: platform token and adapter enablement, gateway process status, pairing/allowlist, session routing, provider health, then tool execution. For an API incident, check in this order: listener and bind address, bearer key, request path, concurrency cap, provider/model, then tool policy. For a tool incident, identify the terminal backend first; the same agent can be safe in Docker and dangerous on `local`.

Keep logs on persistent storage but treat them as sensitive. They can contain prompts, paths, provider errors, and operational metadata even when secrets are redacted. Rotate or retain them according to the privacy needs of your deployment.

Updates change both the runtime and bundled skills. Review the [CLI reference](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/cli-commands.md), take a backup before a major update, then run `hermes doctor` and a small tool-free prompt before re-enabling unattended gateways.

## Backups and Recovery

Hermes has two useful backup scopes. `hermes backup` captures the whole Hermes home, including profiles and credentials, while `hermes profile export` creates a portable single-profile archive with `.env` and `auth.json` excluded. The official [profile command reference](https://hermes-agent.nousresearch.com/docs/reference/profile-commands/) and [CLI reference](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/cli-commands.md) describe the current behavior.

### Full machine backup

The full backup is appropriate for disaster recovery or moving the installation. It contains secrets, so protect the archive like a password vault:

```bash
umask 077
hermes backup --output "$HOME/hermes-backup-$(date +%Y%m%d-%H%M%S).zip"
chmod 600 "$HOME"/hermes-backup-*.zip
```

The backup command uses SQLite's backup API for a consistent database snapshot. It excludes the Hermes source checkout and transient SQLite sidecars. Still, stop a gateway before a planned migration so no external adapter is delivering messages during the cutover.

```bash
hermes gateway stop
hermes backup --output /secure/location/hermes-full.zip
```

Restore only after installing a compatible Hermes runtime and preserving a copy of the destination home:

```bash
mv ~/.hermes ~/.hermes.before-restore
mkdir -p ~/.hermes
hermes import /secure/location/hermes-full.zip
hermes doctor
hermes profile list
```

The exact import confirmation and path behavior can change; read `hermes import --help` before an overwrite. Re-authenticate providers or messaging platforms if tokens were intentionally excluded or invalidated. Start one profile at a time and verify that the restored API bind and gateway adapters are not colliding with an old process.

### Profile handoff

For sharing a profile with another machine or person, prefer the credential-stripping export:

```bash
hermes profile export researcher \
  --output ./researcher-2026-08-22.tar.gz

hermes profile import ./researcher-2026-08-22.tar.gz \
  --name researcher-restored
```

Inspect archives before sharing them. Memory, sessions, user preferences, skills, and `SOUL.md` can contain private material even when API keys are removed. A profile distribution in a Git repository is a different mechanism: it versions a reviewed agent bundle while keeping each install's credentials and user data local.

### Recovery checklist

When Hermes fails after an update, preserve logs and the backup before deleting state. Check the installed version, run `hermes doctor`, validate YAML, confirm that the launcher points at the managed virtual environment, and test the provider with a minimal prompt. If the problem is profile-specific, create a temporary profile to separate runtime failure from corrupted state. Restore the original profile only after confirming which artifact is damaged.

## Hermes Agent Compared with OpenClaw

OpenClaw and Hermes appear in the same local-first assistant discussions because they can both sit between people, models, tools, and messaging channels. They are not identical products, and “Hermes” in this document is not a model family.

At a high level, [OpenClaw](https://github.com/openclaw/openclaw) is an assistant orchestration/control-plane platform organized around its gateway, channels, sessions, routing, tool policy, and provider integrations. Hermes Agent is an agent runtime from Nous Research that combines interactive clients, tools, skills, memory, profiles, messaging adapters, an OpenAI-compatible API server, and a Desktop/headless backend. Both can be deployed as a long-running personal or team assistant, but their command names, configuration layouts, protocols, and operational assumptions differ.

| Dimension | Hermes Agent | OpenClaw |
|---|---|---|
| Primary identity | Tool-using agent runtime with CLI/TUI, profiles, skills, memory, messaging, API, and Desktop backend | Assistant orchestration platform and gateway |
| Messaging process | `hermes gateway` | OpenClaw gateway and channel adapters |
| OpenAI-shaped integration | Optional API server, normally `8642` | Provider/API integrations according to OpenClaw configuration |
| Desktop/headless backend | `hermes serve`, JSON-RPC/WebSocket, commonly `9119` | OpenClaw's own control/UI surfaces and APIs |
| Durable state | `~/.hermes`, `HERMES_HOME`, profile directories, SQLite/session files, skills and memory | OpenClaw state/workspace/config layout |
| Terminal isolation | Local, Docker, SSH, Modal, Daytona, Vercel Sandbox, Singularity | OpenClaw execution and sandbox policy |
| Model role | Hermes routes to configured providers; it is not the Nous Hermes model | OpenClaw also routes to configured providers; it is not a model server |
| Main operational question | Which Hermes surface and profile is running, and where do tools execute? | Which gateway, channel, provider, session, and sandbox policy is active? |

### When Hermes is the better fit

Choose Hermes when you want the Nous Research agent runtime, its skill and memory model, profile isolation, terminal-backend choices, a native Desktop client, or a direct OpenAI-compatible agent endpoint. It is particularly attractive when the distinction between a model response and a tool-using, stateful agent is central to your application.

### When OpenClaw is the better fit

Choose OpenClaw when its gateway/channel orchestration, ecosystem integrations, routing model, sandbox controls, or existing deployment conventions match your needs. If your team already operates OpenClaw, replacing it with Hermes solely because both can receive chat messages is not a technical comparison; compare the control-plane features and recovery model you actually use.

### When they can be combined

They can occupy different layers: OpenClaw can be the outward channel/control plane while Hermes or another backend supplies agent behavior, or Hermes can expose an API that a separate application consumes. A combined deployment adds network, authentication, session, and duplicate-tool risks. Define which system owns identity, model selection, memory, terminal execution, and outbound messaging before connecting them. Do not let both systems independently answer the same channel or write the same state directory.

## Operational Reference

### Surface-selection checklist

```text
Need Telegram/Discord/Slack inbound messages?  Start and configure hermes gateway.
Need Open WebUI or curl over HTTP?             Enable the API server on 8642.
Need Hermes Desktop or remote JSON-RPC?        Run/connect to hermes serve, often 9119.
Need browser dashboard administration?         Use hermes dashboard with authentication.
Need command isolation?                         Configure terminal.backend, separately.
Need independent identity and memory?          Create a profile, not another process on one home.
```

### Hardening checklist

1. Keep `8642` and `9119` on loopback or a private network by default.
2. Require a strong API bearer key and use a narrow CORS allowlist for browser clients.
3. Configure dashboard authentication before any non-loopback bind.
4. Use gateway allowlists and pairing; do not enable all users casually.
5. Run as a non-root OS account.
6. Prefer Docker or SSH terminal execution for unattended agents.
7. Set a narrow `terminal.cwd` and avoid broad host mounts.
8. Keep secrets in `.env` or a secret manager, never in Git or Compose files.
9. Review agent-written skills and memory, enabling write approval when needed.
10. Back up before updates and verify restored profiles on a test path.

### Troubleshooting map

| Symptom | First place to look |
|---|---|
| Telegram/Discord does nothing | `hermes gateway status`, adapter token, pairing, allowlist |
| Open WebUI says connection refused | `API_SERVER_ENABLED`, bind/port, gateway process, container publish |
| API returns unauthorized | `API_SERVER_KEY`, profile `.env`, proxy headers, wrong port/profile |
| Desktop cannot connect | `hermes serve`, readiness port, WS upgrade, backend auth, VPN/reverse proxy |
| Tools run on the wrong machine | `terminal.backend`, `terminal.cwd`, `HERMES_HOME` vs `HOME` |
| Agent remembers too much or too little | memory limits, profile selection, external provider status |
| Skill change appears unexpectedly | bundled sync, external directory writability, skill write gate |
| Two profiles collide | duplicate API port, shared home, duplicate gateway process |
| Container loses everything after restart | missing `/opt/data` mount or wrong host path/permissions |

## Reference Links

- [Hermes Agent documentation](https://hermes-agent.nousresearch.com/docs/)
- [NousResearch/hermes-agent repository](https://github.com/NousResearch/hermes-agent)
- [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
- [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/)
- [Providers and models](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models/)
- [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)
- [OpenAI-compatible API Server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server/)
- [Desktop and remote backends](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/desktop.md)
- [Docker](https://hermes-agent.nousresearch.com/docs/user-guide/docker/)
- [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security)
- [Persistent Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/)
- [Memory Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers/)
- [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- [Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles/)
- [Profile command reference](https://hermes-agent.nousresearch.com/docs/reference/profile-commands/)
- [CLI command reference](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/cli-commands.md)
- [Gateway internals](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/gateway-internals.md)
- [OpenClaw repository](https://github.com/openclaw/openclaw)

## Closing Perspective

Hermes becomes easier to operate once you stop treating “the server” as one thing. The messaging gateway is for platform connections. The API server on `8642` is for OpenAI-shaped HTTP clients. `hermes serve`, commonly on `9119`, is for Desktop and headless JSON-RPC/WebSocket clients. Profiles and `~/.hermes` provide continuity, while terminal backends define where the agent's actions land.

The safest deployment is therefore explicit: one profile per independent agent, one clear owner for each channel, one documented terminal boundary, loopback-first network exposure, authenticated remote access, and a tested backup. The model can be capable, but the surrounding system must still make unsafe actions difficult and recoverable.
