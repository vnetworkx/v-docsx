# AuthRatio Specification

**Status:** Canonical protocol module  
**Applies to:** Certification, restricted operations, drain offsets, revocation logic  
**Version:** 1.1

## 1. Purpose

AuthRatio is the protocol's normalized validity score for deciding whether a vector may participate in restricted actions.

It is a deterministic scalar in the closed interval:

`AuthRatio(v) ∈ [0, 1]`

A higher score indicates stronger protocol confidence in the vector's current validity for the active operation class and space policy.

## 2. Score inputs

### 2.1 Mandatory base factors

Every AuthRatio computation MUST include the following base factors:

- `M` = magnitude validity
- `C` = composition validity
- `O` = ownership proof validity

### 2.2 Optional extension factors

A deployment MAY include additional scored factors:

- `A` = age of vector
- `I` = origin confidence
- `H` = historical integrity
- `T` = space trust level
- `B` = behavior reputation
- `P` = proof depth

Any optional factor used in computation MUST be documented, versioned, and bounded to `[0, 1]`.

## 3. Canonical score form

The canonical weighted form is:

`AuthRatio(v, ctx) = Σ (w_i * s_i)`

Where:

- `s_i` is a normalized factor score in `[0, 1]`
- `w_i` is the corresponding weight in `[0, 1]`
- `Σ w_i = 1`
- `ctx` is the evaluation context, including vector type, operation class, space policy, and risk profile

A minimal canonical base model is:

`AuthRatio = wM*M + wC*C + wO*O + wX*X`

where `X` is an aggregated extension score.

If a deployment uses the aggregated extension score `X`, it MUST define:

`X = Σ (u_j * e_j)` with `Σ u_j = 1`

for the chosen extension factors `e_j`.

## 4. Factor definitions

### 4.1 Magnitude validity (`M`)
Measures whether the vector's magnitude is structurally acceptable for the active type and operation.

Examples of invalid magnitude conditions:

- negative magnitude in a nonnegative domain
- magnitude exceeding declared bounds
- magnitude inconsistent with declared component domain

### 4.2 Composition validity (`C`)
Measures whether the component ratios or component layout satisfy the active type's composition rule.

Examples:

- normalized composition within allowed simplex
- required dimension present
- forbidden component absent
- component proportions within policy bounds

### 4.3 Ownership proof validity (`O`)
Measures whether the wallet or authority claim is genuine.

Examples:

- valid signature
- valid custody proof
- valid delegate authorization
- unrevoked authority binding

## 5. Threshold model

AuthRatio alone does not decide certification. The threshold is context dependent:

`Certified(v, ctx) = 1 if AuthRatio(v, ctx) ≥ Threshold(ctx) else 0`

The threshold MUST be explicit and derived from the active:

- vector type
- operation class
- space policy
- risk profile
- protocol version

A deployment MAY define:

`Threshold = Θ(type, op, space, risk, policy_version)`

## 6. Bounds and normalization

All factor scores MUST be normalized to `[0, 1]`.

If a factor is unavailable, a deployment MUST either:

- define a documented fallback rule, or
- fail closed and reject certification

Silent substitution is prohibited.

## 7. Determinism rules

A compliant implementation MUST ensure:

- same vector state
- same context
- same rule version

produces the same AuthRatio.

Any nondeterministic input MUST be excluded from the score or transformed into a deterministic proof.

## 8. Weight governance

Weights MUST be:

- explicit
- versioned
- audit-friendly
- space-aware when applicable
- type-aware when applicable

Weights MUST NOT be hidden inside unrelated code paths.

Versioned weight sets SHOULD be recorded as:

`weight_set_id`, `weight_version`, `effective_from`, `effective_context`

## 9. Certification linkage

AuthRatio is an input to certification, not certification itself.

A vector may have a high AuthRatio and still be uncertified if:

- the threshold is higher
- the vector is revoked
- the vector is suspended
- the required proof is missing
- the operation class requires additional authority

## 10. Drain credits

If a space permits offset credits, then the effective drain MAY be reduced by an AuthRatio-linked credit:

`delta_effective = max(delta - credit, 0)`

where `credit` MUST be defined by policy and MAY depend on:

- AuthRatio
- certification status
- reputation decay
- expiry window
- non-transferability rules

## 11. Failure modes

A compliant implementation MUST fail closed if:

- factor scores are missing and no fallback exists
- weights do not sum to 1 within the declared tolerance
- threshold rules are ambiguous
- a referenced policy version is unknown
- a proof required for a factor is invalid

## 12. Output contract

A full AuthRatio evaluation MUST return at minimum:

- score
- threshold
- certified boolean
- factor breakdown
- weight set reference
- policy version reference
- evaluation timestamp or deterministic proof reference

## 13. Canonical formula summary

`AuthRatio(v, ctx) = wM*M + wC*C + wO*O + Σ(wk*Sk)`

subject to:

- `0 ≤ score ≤ 1`
- `Σ weights = 1`
- `threshold = Θ(ctx)`
- `certified = score ≥ threshold`
