# Formalism

This document gives a stricter mathematical framing for the protocol.

## 1. Sets and mappings

Let:
- `V` be the set of all valid vectors
- `W` be the set of wallets
- `S` be the set of vector spaces
- `R` be the set of records
- `O` be the set of operations

A state transition may be expressed as:

`f: (v, w, s, r*) -> (v', w', s', r')`

where `r*` is the prior record chain and `r'` is the newly produced record.

## 2. Validity predicate

Define:

`Valid(v, w, s) -> {true, false}`

A vector is valid only if:
- its type is recognized,
- its component domain is respected,
- its ownership or custody is valid,
- its certification state is acceptable for the intended action.

## 3. Operation predicate

Define:

`Permitted(op, v, w, s) -> {true, false}`

An operation is permitted only if all preconditions hold.

## 4. Conservation for explicit-cost operations

For an operation with drain and settlement, use:

`v_after = T(v_before) - drain + settlement`

where `T` is the type-specific transition function.

This is a conceptual identity. A concrete implementation MUST define exact component-wise behavior.

## 5. Zero preservation

A valid operation `F` is zero-preserving if:

`F(0) = 0`

for all zero vectors in the supported domain.

Any type that cannot satisfy this property MUST declare the exception explicitly.

## 6. Component-wise operations

For component-wise transfer and projection, each component MAY be transformed independently:

`x'i = g_i(xi, parameters)`

The family `{g_i}` MUST be deterministic and fully specified.

## 7. Proof obligations

A compliant implementation SHOULD be able to prove or demonstrate:

- pre-state validity
- post-state validity
- record correctness
- replay equivalence
- settlement uniqueness
- non-duplication of origin claims

## 8. Canonical serialization

Let `Serialize(R)` be the canonical byte representation of a record.

Then for any valid record `R`:

- `Serialize(R)` MUST be unique for that record definition
- `Hash(Serialize(R))` MUST be stable across compliant implementations
- equivalent logical records MUST produce equivalent canonical encodings

## 9. Extensible formal rule

A future vector type MAY define its own norm, projection rule, or settlement law, provided that:
- the type definition is explicit,
- compatibility is versioned,
- historical records remain interpretable.

## 10. Human-readable summary

The formal model says the same thing as the rulebook:
- state must be valid,
- operations must be permitted,
- every change must be recorded,
- hidden mutation is forbidden,
- ambiguous math is not allowed.
