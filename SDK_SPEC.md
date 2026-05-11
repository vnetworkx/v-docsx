# SDK Specification

**Status:** Canonical interface contract  
**Version:** 1.1

## 1. Purpose

SDKs provide safe, typed access to the Vector Network. They are client interfaces only and MUST NOT replace kernel validation.

## 2. Supported SDK families

Recommended SDK families:

- Python
- TypeScript / JavaScript
- Rust
- Java
- Go
- Swift
- Kotlin

A deployment MAY add other SDKs if they conform to the same operation contracts.

## 3. SDK responsibilities

An SDK MUST support:

- node connection
- wallet initialization
- signing
- request construction
- operation submission
- query retrieval
- record inspection
- proof verification
- error decoding

An SDK MUST NOT:

- mutate state locally as authoritative truth
- bypass certification
- infer hidden protocol behavior
- store private keys in shared network state

## 4. Core interface model

Every SDK SHOULD expose the same conceptual modules:

- `wallet`
- `auth`
- `operations`
- `queries`
- `records`
- `protocol`
- `types`
- `errors`

## 5. Canonical request shape

A submitted operation MUST be representable as:

```text
OperationRequest = {
  protocol_version,
  space_id,
  operation,
  params,
  actor_pk,
  signature,
  proof?,
  client_version,
  idempotency_key?
}
```

## 6. Canonical response shape

A successful response SHOULD include:

```text
OperationResponse = {
  accepted: true,
  record_id,
  prev_hash,
  state_before,
  state_after,
  certified,
  auth_ratio,
  timestamp,
  receipt,
  canonical_hash
}
```

An unsuccessful response SHOULD include:

```text
OperationError = {
  accepted: false,
  error_code,
  message,
  recoverable,
  operation,
  context,
  canonical_hash?
}
```

## 7. Network contract

SDKs MUST:

- submit operations only to compatible protocol versions
- verify canonical response hashes where available
- surface rejected operations clearly
- preserve operation ordering requirements when requested
- expose deterministic serialization utilities

## 8. Safety contract

An SDK MUST perform client-side checks for:

- required fields
- obvious type mismatches
- missing signatures
- missing proofs
- invalid zero-vector normalization attempts

Client-side checks are advisory. The kernel remains authoritative.

## 9. Conformance tiers

### Tier 1: Read-only
- query
- record inspection
- protocol metadata

### Tier 2: Signed client
- wallet binding
- certified query access
- request signing
- deterministic serialization

### Tier 3: Full client
- all core operations
- proof submission
- record verification
- event subscriptions

## 10. Recommended module mapping

| Module | Responsibility |
|---|---|
| wallet | key handling, signing, recovery |
| auth | certification, proof helpers |
| operations | create, certify, transfer, drain, project, reconstruct, query, record |
| queries | state reads and history reads |
| records | hash-linked history access |
| protocol | versions, feature flags, compatibility |
| errors | typed failure handling |
| types | canonical request/response shapes |
