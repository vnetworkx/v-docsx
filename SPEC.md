# Vector Network Protocol Specification
## Master Rulebook

**Document status:** Draft specification  
**Scope:** Vector state, wallet ownership, certification, projection, reconstruction, drain, origin, and immutable records  
**Audience:** Researchers, developers, auditors, protocol designers, and implementers

---

## 1. Purpose

Vector Network is a decentralized state system in which each wallet holds a multidimensional vector of token values. The protocol defines how vectors are created, stored, transferred, projected, drained, reconstructed, certified, and recorded.

This specification is the normative source of truth for the protocol. Any implementation claiming compatibility with Vector Network MUST conform to this document.

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

## 3. Design goals

Vector Network is designed to satisfy the following goals:

1. **Deterministic accounting** — all valid state transitions are reproducible from the record stream.
2. **Type awareness** — every vector and operation is interpreted through declared metadata.
3. **Owner control** — only the wallet owner or a protocol-authorized delegate may initiate owner-bound actions.
4. **Auditability** — all state transitions create immutable records.
5. **Restricted creation** — new vectors are only created through verified origin rules.
6. **Composable operation** — projection, reconstruction, and drain rules MUST preserve accounting integrity.
7. **Extensibility** — future vector types, domains, and rules MAY be added without breaking earlier valid records.
8. **Safety at zero** — zero vectors remain zero under all valid operations that mathematically permit zero-preservation.
9. **Explicit failure** — invalid operations MUST fail with a defined error state and MUST NOT silently mutate value.
10. **Research readability** — the specification MUST remain precise enough for academic and implementation use.

---

## 4. Canonical entities

### 4.1 Vector
A vector is the fundamental state object.

A vector is defined as:

`v = (x1, x2, ..., xn)`

where each component `xi` is the quantity of the `i`-th vToken dimension.

A vector MUST have:
- a finite dimension `n > 0`
- a canonical ordering of components
- a declared type
- a valid ownership association or protocol-visible custody state

A vector MAY also contain metadata fields such as:
- `vector_id`
- `type_id`
- `origin_ref`
- `certification_state`
- `space_id`
- `revision`
- `checksum`

The vector magnitude is the aggregate value across all components, as defined by the active token valuation rule for the vector type. If no alternative valuation rule is declared, magnitude is the simple sum of all non-negative components.

### 4.2 vWallet
A vWallet is a secure owner-bound container for exactly zero or more vectors according to the protocol's storage model.

A wallet MUST have:
- a public key or equivalent public identifier
- a private key never published on the shared ledger
- wallet metadata
- a verifiable ownership binding

A wallet MAY be able to:
- send vectors
- receive vectors
- project vectors
- reconstruct projected vectors
- drain vectors according to protocol rules
- participate in certification workflows

### 4.3 Vector Space
A Vector Space is the global or local state environment in which vectors exist, move, and are recorded.

A Vector Space MUST define:
- a unique `space_id`
- a parameter set
- a record ordering rule
- a validity policy
- a state transition model

A Vector Space MAY be:
- global
- domain-specific
- shard-specific
- application-specific
- cross-linked with other spaces

### 4.4 Vector Network
The Vector Network is the complete connected system of Vector Spaces, vWallets, vTokens, vContracts, validators, records, and protocol rules.

The network governs:
- cross-space movement
- validation
- certification
- programmable transitions
- immutable history

### 4.5 Vector Record
Every state change MUST create an immutable record.

A record captures:
- pre-state
- post-state
- operation
- parameters
- certification data
- timestamp
- proof or proof reference

### 4.6 Certification
Certification is the validation process that determines whether a vector may participate in restricted network operations.

A vector is certified when its AuthRatio meets or exceeds the applicable threshold for the active vector type and operation class.

### 4.7 AuthRatio
AuthRatio is a composite validity score computed from:
- magnitude validity
- composition validity
- ownership proof validity
- optional type-specific validity dimensions

### 4.8 Vector Projection
Vector Projection is the process of committing part of a vector into a defined rule environment.

Projection MAY:
- lock value temporarily
- apply risk/reward logic
- produce gain or loss at settlement
- require certification

### 4.9 Vector Reconstruction
Vector Reconstruction returns the projected portion to the wallet after settlement.

Reconstruction MUST preserve accounting consistency between:
- the original vector
- the projected segment
- the settlement result
- the final wallet state

### 4.10 Vector Origin Engine
The Vector Origin Engine creates new vectors through verified effort.

Creation MUST be restricted to legitimate origin channels. Unrestricted minting is prohibited.

### 4.11 Vector Drain
Vector Drain is a protocol-defined reduction, fee, or cost applied before or during certain operations.

Drain MUST be explicit, parameterized, and recorded.

---

## 5. System-wide invariants

The following invariants MUST hold for all valid states:

1. **Record completeness** — every state mutation creates a record.
2. **Type consistency** — all operations respect the active type of the vector.
3. **Ownership authenticity** — owner-bound operations require valid proof.
4. **Accounting integrity** — vector value is neither created nor destroyed except by authorized origin or authorized burn-like logic.
5. **Zero preservation** — zero vectors remain zero under valid zero-preserving operations.
6. **Non-negative domain rule** — unless a vector type explicitly allows signed components, component values MUST NOT be negative.
7. **Canonical ordering** — component order MUST remain stable within a type.
8. **Defined drain** — drain MUST be declared before use.
9. **Defined projection semantics** — projection and reconstruction MUST have exact settlement semantics.
10. **Guarded normalization** — normalization is undefined for the zero vector and MUST be guarded.
11. **Reject on ambiguity** — uncertain or under-specified operations MUST fail closed.
12. **Deterministic replays** — valid records MUST reproduce the same end state when replayed in order.

---

## 6. Required state fields

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

## 7. Operation classes

The protocol recognizes the following core operation classes:

- `TRANSFER`
- `PROJECTION`
- `RECONSTRUCTION`
- `DRAIN`
- `CERTIFICATION_CHECK`
- `ORIGIN_VALIDATION`
- `ORIGIN_CREATE`
- `BURN` if a particular deployment introduces a permitted irreversible reduction rule
- `FREEZE`
- `UNFREEZE`
- `MERGE`
- `SPLIT`
- `MIGRATE`
- `ANNOTATE`
- `REVOKE_CERTIFICATION`

An implementation MAY support additional operations only if they do not violate this specification and they are versioned clearly.

---

## 8. Operation ordering

For operations that affect a vector, a compliant system MUST execute the following logical stages where applicable:

1. Authenticate the initiator.
2. Verify ownership or custody authority.
3. Check certification and type eligibility.
4. Validate parameters.
5. Apply drain, if required and explicitly defined.
6. Execute the operation.
7. Validate post-state invariants.
8. Record the transition immutably.

Any operation failing an earlier stage MUST abort without writing a success record.

---

## 9. State transition rules

### 9.1 Transfer
Transfer moves value from one wallet or space to another.

Transfer MUST:
- preserve total transferable value after permitted drain
- preserve vector type compatibility unless conversion is explicitly defined
- create a record
- require valid authority

### 9.2 Projection
Projection locks a defined fraction or component subset into a rule environment.

Projection MUST:
- define lock scope
- define settlement rule
- define duration or settlement condition if applicable
- record projected value separately from free value
- preserve accounting consistency

### 9.3 Reconstruction
Reconstruction restores projected value after settlement.

Reconstruction MUST:
- reference a prior projection
- apply settlement result exactly once unless the projection type allows multiple stages
- reject double-settlement
- update vector state atomically
- record the result

### 9.4 Drain
Drain reduces transferable magnitude by a defined percentage, unit amount, or function.

Drain MUST:
- be declared before application
- be deterministic for the active parameter set
- state whether it is absolute, proportional, or hybrid
- be included in the record

### 9.5 Certification check
Certification checks whether a vector is allowed to participate in restricted operations.

The result MUST be one of:
- `CERTIFIED`
- `UNCERTIFIED`
- `SUSPENDED`
- `REVOKED`
- `PENDING`

### 9.6 Origin validation
Origin validation confirms whether a new vector is legitimately created.

Origin validation MUST verify:
- source legitimacy
- work proof or procedural proof
- parameter compliance
- uniqueness or non-duplication where required

---

## 10. Prohibited behaviors

A compliant implementation MUST NOT:

1. create value without authorized origin,
2. mutate a vector without a record,
3. perform projection or reconstruction without a defined settlement model,
4. allow negative value where the vector type forbids it,
5. normalize a zero vector without a guard,
6. reuse a settlement claim more than once unless explicitly allowed,
7. hide drain behavior in implicit side effects,
8. treat uncertified vectors as certified,
9. expose private keys in records,
10. accept ambiguous component ordering,
11. silently coerce incompatible vector types,
12. permit record rewriting without versioned append-only governance.

---

## 11. Extensibility rules

Vector Network is designed for growth. Future extensions MUST obey the following:

- New vector types MUST declare their component semantics.
- New operations MUST define preconditions, postconditions, and record shape.
- New spaces MUST declare their local rules and compatibility layer.
- New certification signals MUST map into the AuthRatio framework or a documented successor.
- Any breaking change MUST introduce a new protocol version.
- Deprecated behavior MAY remain readable for historical replay, but MUST NOT be used as a default for new state transitions.

---

## 12. Versioning

Every implementation MUST declare:
- `protocol_name`
- `protocol_version`
- `schema_version`
- `rule_version`
- `space_version`

Version negotiation MUST be explicit.

If two participants support different versions, the system MUST:
- reject incompatible operations, or
- apply a documented translation layer with a provable equivalence guarantee.

---

## 13. Conformance

A system is conformant only if it can:

- validate ownership
- represent vectors canonically
- create records immutably
- apply certification logic
- execute transfer, projection, reconstruction, and drain according to this specification
- detect and reject invalid states
- replay a valid ledger deterministically

A partial implementation MUST identify the subset of operations it supports and MUST NOT claim full compliance.

---

## 14. Educational interpretation

For learning purposes:

- A vector is the state.
- A wallet is the owner-bound container.
- A space is the environment.
- A record is the history.
- Certification is the permission layer.
- Projection is the controlled lock-and-settle process.
- Reconstruction is the controlled return process.
- Drain is the explicit cost model.
- Origin is the restricted creation gate.

These interpretations are pedagogical and do not replace the normative definitions above.

---

## 15. Final rule

If a behavior is not explicitly allowed by this specification and it affects value, ownership, validation, or history, the safe default is to reject the operation until the behavior is formally specified.
