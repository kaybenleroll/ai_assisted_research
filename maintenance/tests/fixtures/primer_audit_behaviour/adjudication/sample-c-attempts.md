# Sample C trial setup attempts

On 27 November 2026 the non-blind fallback protocol was frozen at commit
`0edccb0aa4cdc1dad4ed59ca490d5326c34216c2`. The three fixture files, the key
and the audit skill matched the SHA-256 pins in that protocol. Neither fixture
nor key was changed. The key was already accessible on GitHub; the runtime
shared the host network and no restricted-egress control was established.

Two disposable bubblewrap boundaries mounted the fixture and guidance
read-only, a private temporary filesystem and a read-only authentication file.
The host home, key and operator files were not mounted. Each canary confirmed
that the key's host path and a host-only sentinel were unreadable, and that the
three fixture files and skill matched their pinned hashes. This tests those
filesystem paths, not network isolation or absence of other access paths.

The operator started fresh unnamed-guidance and manually directed Codex CLI
0.172.0 sessions, `gpt-6.1-terra` at medium effort, ephemeral and with the
CLI read-only sandbox. Both used the exact prompts in the protocol. JSONL
events were captured privately. The first pair exited zero, but both reviewers
reported that their command tool could not start because the version-matched
`codex-code-mode-host` executable was missing. Neither read the inputs.

After adding the version-matched CLI helper executables and repeating both
filesystem canaries, a fresh pair again exited zero. Both recorded failed
command executions: the inner read-only sandbox could not create a nested user
namespace. Neither reviewer read the fixture; the manual reviewer also tried
available resource catalogues without obtaining the files. These are setup
failures, not audit results, selection evidence, or adjudicable findings.

Automatic approval review rejected a proposed invocation with the CLI inner
sandbox disabled: the review stated that this would broaden permissions and
expose the mounted authentication file beyond the approved read-only reviewer
boundary, and directed against a workaround or indirect execution. One parallel
invocation had already started; it was immediately interrupted with exit 130,
before any completed reviewer message or tool event. It is not a trial result.

A normal read-only CLI session without the outer filesystem boundary would
leave the key and prior calibration material available locally as well as on
the network. It would not preserve the intended independent fixture control;
the existing sample-B evidence already demonstrates the limits of such an
uncontrolled comparison. No further trial was run. Raw temporary event files
are private and are not durable evidence. No claims are made about native
activation, delivered tool payloads, finding accuracy or truncation recovery.
