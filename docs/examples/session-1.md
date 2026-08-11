# Example Session 1 — Auth bug (verbose)

User enables chess and asks to fix a recurring auth failure.

```
User: /chess
Agent: ♟ Chess mode ON. Three Selves active.

User: /chess verbose
User: fix the auth bug again — token still invalid
```

Internal blocks (shown because verbose):

```
[P] C:code:0.94|⚠:2s4|✓:1s2|🔄:1s3|👻:0|🔁:1s2|⚡:0|L:auth-token-bug|A:use-jwt
[F] C:code:0.50|⚠:1s4r3|✦:0|🔗:3b5c|🎯:+1g201|L:keep-thin|A:add-guard
[B] r:+2|m:0|c:0.33|d:0|s:3|h:0|fr:2|fo:0|fd:3|fc:+1|LEAN→slow-down
```

Present response shape:

> Before acting, verify token expiry check. Risk: repeating the same auth-token path that failed twice.

History append:

```json
{"t":5,"cat":"code","c":0.94,"sig":"🔄","s":3,"ctx":"auth-token-bug","fix":"none","ts":"2026-08-11T12:00:00.000Z"}
```
