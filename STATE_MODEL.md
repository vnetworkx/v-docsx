# State Model

This document defines the mathematical model for Vector Network.

## 1. Vector definition

A vector is written as:

`v = (x1, x2, ..., xn)`

where `n` is the dimension and `xi` is the value of the `i`-th component.

## 2. Component domain

The component domain is declared by vector type.

Default rule:
- `xi` MUST be a non-negative real number, integer, or fixed-point quantity.
- A type MAY permit signed values only if the type definition explicitly allows them.
- A type MAY require discrete units.
- A type MUST specify rounding behavior if fractions are not allowed.

## 3. Zero vector

The zero vector is:

`0 = (0, 0, ..., 0)`

Properties:
- It is the additive identity in the default model.
- It MUST remain zero under zero-preserving operations.
- Normalization of the zero vector is undefined and MUST be guarded.

## 4. Magnitude

Magnitude is the total value of a vector.

Default magnitude rule:

`|v| = sum(xi)`

If a vector type defines another valuation function, that function MUST be published as part of the type metadata.

## 5. Direction or composition

The direction of a vector is its proportional composition across dimensions.

For a non-zero vector, the normalized composition may be expressed as:

`d(v) = (x1 / |v|, x2 / |v|, ..., xn / |v|)`

This quantity is undefined when `|v| = 0`.

## 6. Type system

A vector type declares:
- allowed component domains
- normalization rule
- drain rule compatibility
- projection compatibility
- reconstruction semantics
- certification thresholds
- conversion permissions

A vector type MUST be immutable for a given historical record. A type MAY be deprecated, but historical records MUST remain readable.

## 7. State transitions

A state transition is a function:

`T: State_before -> State_after`

For a valid transition:
- preconditions MUST hold
- postconditions MUST hold
- record generation MUST occur
- authority MUST be valid

## 8. Conservation model

Let:
- `before` be the vector state prior to an operation
- `after` be the vector state after an operation
- `drain` be the explicit cost
- `gain` be any authorized positive settlement outcome
- `loss` be any authorized negative settlement outcome

For a conservative operation class, the following identity SHOULD hold:

`|after| = |before| - drain + gain - loss`

The exact law depends on the operation type. Projection and reconstruction MUST define their own settlement law, and that law MUST be used consistently.

## 9. Split and merge

A split partitions a vector into two or more vectors.

A merge combines multiple vectors into one vector.

Rules:
- The sum of constituent values MUST be preserved unless explicit drain or settlement applies.
- The resulting type MUST be valid.
- All resulting records MUST reference the source record set.

## 10. Migration

Migration moves a vector from one space to another.

Rules:
- source space rules MUST be satisfied
- target space rules MUST be satisfied
- compatibility rules MUST be explicit
- records MUST retain traceability across spaces

## 11. Immutability and revision

Vector state is append-only from the perspective of records.

A vector MAY acquire a new revision after a transition, but the previous revision MUST remain recoverable through the record chain.

## 12. Implementation note

A practical implementation MAY store:
- sparse component maps for high-dimensional vectors
- dense arrays for fixed-dimension types
- packed fixed-point values for deterministic arithmetic

Any storage choice MUST preserve canonical serialization.
