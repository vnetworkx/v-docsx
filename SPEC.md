# Vector Network Protocol Specification
## Master Rulebook

**Document status:** Canonical draft specification  
**Scope:** Vector state, wallet ownership, certification, projection, reconstruction, drain, origin, records, language, SDKs, and visualization  
**Audience:** Researchers, developers, auditors, protocol designers, and implementers

---

## 1. Purpose

Vector Network is a decentralized state system in which each wallet holds a multidimensional vector of token values. The protocol defines how vectors are created, stored, transferred, projected, drained, reconstructed, certified, and recorded.

This specification is the normative source of truth for the protocol. Any implementation claiming compatibility with Vector Network MUST conform to this document and the versioned sub-specifications referenced herein.

---

## 2. Normative language

The following terms are normative:

- **MUST**: absolute requirement.
- **MUST NOT**: absolute prohibition.
- **SHOULD**: recommended behavior; valid exceptions may exist.
- **SHOULD NOT**: discouraged behavior.
- **MAY**: permitted behavior.

When this specification uses these terms, they describe required protocol behavior, not style guidance.

---

## 3. Canonical document map

The master specification is supported by the following canonical modules:

- `AUTHRATIO.md` — certification score model
- `CERTIFICATION.md` — certification state rules
- `OPERATIONS.md` — operation semantics
- `OPERATIONS_FINITE_TRANSITIONS.md` — finite allowed transitions
- `FORMALISM.md` — mathematical model
- `VECTOR_LANGUAGE_SPEC.md` — language grammar and semantics
- `VECTOR_LANGUAGE_REFERENCE.md` — language reference
- `SDK_SPEC.md` — SDK contract
- `SDK_FUNCTION_CONTRACTS.md` — function-level contract reference
- `VISUALIZATION_FRAMEWORK.md` — architecture and charts
- `EXAMPLES.md` — worked examples
- `RECORDS.md` — record rules
- `SECURITY.md` — security rules
- `STATE_MODEL.md` / `CANONICAL_STATE_MODEL.md` — canonical state structures

If a sub-document conflicts with this master specification, the master specification governs until a versioned override is defined.

---

## 4. Design goals

Vector Network is designed to satisfy the following goals:

1. Deterministic accounting.
2. Type awareness.
3. Owner control.
4. Auditability.
5. Restricted creation.
6. Composable operation.
7. Extensibility.
8. Safety at zero.
9. Explicit failure.
10. Replayable history.

---

## 5. Canonical entities

### 5.1 Vector
A vector is the fundamental state object.

A vector is defined as:

`v = (x1, x2, ..., xn)`

where each component `xi` is the quantity of the `i`-th vToken dimension.

### 5.2 Wallet
A wallet is a secure owner-bound container for one or more vectors according to the protocol's storage model.

A wallet MUST have:

- a public key or equivalent public identifier
- a private key never published on the shared ledger
- wallet metadata
- a verifiable ownership binding

### 5.3 Vector Space
A Vector Space is the state environment in which vectors exist, move, and are recorded.

### 5.4 Vector Record
Every state change MUST create an immutable record.

### 5.5 Certification
Certification is the validation process that determines whether a vector may participate in restricted network operations.

### 5.6 AuthRatio
AuthRatio is the composite validity score used by certification.

### 5.7 Projection and Reconstruction
Projection locks a portion of a vector into a rule environment. Reconstruction returns the projected portion after settlement.

### 5.8 Origin Engine
The Origin Engine creates new vectors through verified effort or an equivalent approved origin path.

### 5.9 Drain
Drain is a protocol-defined reduction, fee, or cost applied before or during certain operations.

---

## 6. System-wide invariants

The following invariants MUST hold for all valid states:

1. Record completeness.
2. Type consistency.
3. Ownership authenticity.
4. Accounting integrity.
5. Zero preservation.
6. Non-negative domain rule unless the type explicitly allows signed components.
7. Canonical ordering.
8. Defined drain.
9. Defined projection semantics.
10. Guarded normalization.
11. Reject on ambiguity.
12. Deterministic replays.

---

## 7. Required state fields

A compliant implementation MUST represent at minimum the following logical fields:

### Vector fields
- `vector_id`
- `components`
- `type_id`
- `space_id`
- `owner_wallet_id` or equivalent custody reference
- `certification_state`
- `creation_origin`
- `revision`
- `status`

### Wallet fields
- `wallet_id`
- `public_key`
- `wallet_metadata`
- `bound_vectors`
- `status`

### Record fields
- `record_id`
- `v_before`
- `v_after`
- `operation`
- `parameters`
- `certification`
- `timestamp`
- `proof`
- `space_id`
- `version`

---

## 8. Canonical operation set

The canonical core operation set is finite:

- `CREATE`
- `CERTIFY`
- `TRANSFER`
- `DRAIN`
- `PROJECT`
- `RECONSTRUCT`
- `QUERY`
- `RECORD`

This is the allowed core transition set for v1.

---

## 9. State transition rules

### 9.1 Create
Create produces a new origin-valid vector. It MUST be gated by origin validation.

### 9.2 Certify
Certify evaluates AuthRatio against the current threshold and records the result.

### 9.3 Transfer
Transfer moves value from one wallet or space to another.

### 9.4 Drain
Drain reduces transferable magnitude by a defined percentage, unit amount, or function.

### 9.5 Project
Project locks a defined fraction or component subset into a rule environment.

### 9.6 Reconstruct
Reconstruct restores projected value after settlement.

### 9.7 Query
Query reads network state and MUST NOT mutate ledger state.

### 9.8 Record
Record persists an immutable state transition entry.

---

## 10. Validation order

For any write operation, the kernel SHOULD verify in this order:

1. security and authentication
2. ownership authority
3. certification
4. type constraints
5. drain rules
6. settlement rules
7. state mutation
8. record creation

Any operation failing an earlier stage MUST abort without writing a success record.

---

## 11. Prohibited behaviors

A compliant implementation MUST NOT:

1. create value without authorized origin
2. mutate a vector without a record
3. perform projection or reconstruction without a defined settlement model
4. allow negative value where the vector type forbids it
5. normalize a zero vector without a guard
6. reuse a settlement claim more than once unless explicitly allowed
7. hide drain behavior in implicit side effects
8. treat uncertified vectors as certified
9. expose private keys in records
10. accept ambiguous component ordering
11. silently coerce incompatible vector types
12. permit record rewriting without versioned append-only governance
13. introduce new canonical core transitions without a versioned spec

---

## 12. Language, SDK, and visualization layers

The Vector Language, SDKs, and visualization systems are interface layers only.

They MUST:

- compile or map into kernel operations
- preserve canonical state semantics
- avoid hidden mutation
- respect versioning
- expose records and proofs faithfully

They MUST NOT:

- define alternate source-of-truth rules
- bypass certification or ownership checks
- fabricate values or records
- redefine the canonical transition set

---

## 13. Versioning

Every implementation MUST declare:

- `protocol_name`
- `protocol_version`
- `schema_version`
- `rule_version`
- `space_version`

Version negotiation MUST be explicit.

If two participants support different versions, the system MUST reject incompatible operations or apply a documented translation layer with a provable equivalence guarantee.

---

## 14. Conformance

A system is conformant only if it can:

- validate ownership
- represent vectors canonically
- create records immutably
- apply certification logic
- execute transfer, projection, reconstruction, drain, create, query, and record according to this specification
- detect and reject invalid states
- replay a valid ledger deterministically

---

## 15. Final rule

If a behavior is not explicitly allowed by this specification and it affects value, ownership, validation, or history, the safe default is to reject the operation until the behavior is formally specified.
