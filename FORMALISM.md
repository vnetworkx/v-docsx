# Formalism

This document gives a stricter mathematical framing for the protocol.

## 1. Sets and mappings

Let:

- `V` be the set of all valid vectors
- `W` be the set of wallets
- `S` be the set of vector spaces
- `R` be the set of records
- `O` be the set of operations
- `C` be the set of certification contexts

A state transition may be expressed as:

`f_op: (σ, ctx) -> (σ', r)`

where:

- `σ` is the current state
- `ctx` is the operation context
- `σ'` is the next state
- `r` is the newly produced record

## 2. State tuple

A canonical vector state may be modeled as:

`σ = (v, w, s, cert, proj, meta, chain)`

Where:

- `v` = vector value
- `w` = wallet or custody binding
- `s` = active space
- `cert` = certification state
- `proj` = projection state
- `meta` = metadata
- `chain` = prior record chain

## 3. Validity predicate

Define:

`Valid(σ, ctx) -> {true, false}`

A state is valid only if:

- its type is recognized
- its component domain is respected
- its ownership or custody is valid
- its certification state is acceptable for the intended action
- its record chain is intact
- its zero-vector constraints are satisfied

## 4. Operation predicate

Define:

`Permitted(op, σ, ctx) -> {true, false}`

An operation is permitted only if all preconditions hold.

## 5. Transition relation

Define the canonical transition relation:

`σ --op/ctx--> σ'`

This relation is partial. If preconditions fail, the transition is undefined and the operation MUST be rejected.

## 6. Conservation for explicit-cost operations

For an operation with drain and settlement, use:

`v_after = T_op(v_before, ctx) - D(ctx) + S(ctx)`

where:

- `T_op` is the type-specific transition function
- `D` is the explicit drain term
- `S` is the settlement term

This identity is conceptual. A concrete implementation MUST define exact component-wise behavior.

## 7. Zero preservation

A valid operation `F` is zero-preserving if:

`F(0) = 0`

for all zero vectors in the supported domain.

Any type that cannot satisfy this property MUST declare the exception explicitly.

## 8. Component-wise operations

For component-wise transfer and projection, each component MAY be transformed independently:

`x'_i = g_i(x_i, parameters)`

The family `{g_i}` MUST be deterministic and fully specified.

## 9. Certification math

A vector is certified when:

`AuthRatio(v, ctx) >= Θ(ctx)`

where:

- `AuthRatio(v, ctx) ∈ [0, 1]`
- `Θ(ctx) ∈ [0, 1]`

## 10. Record function

Define a canonical record function:

`rec: (σ, op, ctx, σ') -> r`

A valid record MUST capture:

- pre-state
- post-state
- operation
- parameters
- proof reference
- certification result
- record linkage

## 11. Proof obligations

A compliant implementation SHOULD be able to prove or demonstrate:

- pre-state validity
- post-state validity
- record correctness
- replay equivalence
- settlement uniqueness
- non-duplication of origin claims

## 12. Canonical serialization

Let `Serialize(R)` be the canonical byte representation of a record.

Then for any valid record `R`:

- `Serialize(R)` MUST be unique for that record definition
- `Hash(Serialize(R))` MUST be stable across compliant implementations
- equivalent logical records MUST produce equivalent canonical encodings

## 13. Extensible formal rule

A future vector type MAY define its own norm, projection rule, or settlement law, provided that:

- the type definition is explicit
- compatibility is versioned
- historical records remain interpretable

## 14. Human-readable summary

The formal model says the same thing as the rulebook:

- state must be valid
- operations must be permitted
- every change must be recorded
- hidden mutation is forbidden
- ambiguous math is not allowed
