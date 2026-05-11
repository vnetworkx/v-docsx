# Certification

## 1. Purpose

Certification determines whether a vector is eligible to participate in restricted operations.

## 2. AuthRatio

AuthRatio is a composite score calculated from one or more factors.

Mandatory base factors:
- magnitude validity
- composition validity
- ownership proof validity

Optional factors:
- age of vector
- origin confidence
- historical integrity
- space trust level
- behavior reputation
- proof depth

## 3. General rule

A vector is certified if:

`AuthRatio >= Threshold`

where Threshold is determined by:
- vector type
- operation class
- space policy
- risk profile

## 4. Score model

A protocol MAY compute AuthRatio by weighted combination.

Example model:

`AuthRatio = w1*M + w2*C + w3*O + w4*X`

where:
- `M` = magnitude validity
- `C` = composition validity
- `O` = ownership proof validity
- `X` = optional extensions

The weights MUST be documented and versioned.

## 5. Validation requirements

Certification MUST verify:
- the vector exists,
- the vector type is recognized,
- the owner binding is genuine,
- the record chain is intact,
- any required proof is valid,
- the vector is not explicitly revoked.

## 6. Certification states

### 6.1 Pending
The vector has not yet completed validation.

### 6.2 Certified
The vector satisfies the threshold.

### 6.3 Uncertified
The vector does not satisfy the threshold.

### 6.4 Suspended
The vector was previously valid but is temporarily blocked.

### 6.5 Revoked
The vector is disallowed until reauthorization or reorigin is completed.

## 7. Threshold management

Thresholds MUST be:
- explicit
- versioned
- space-aware
- type-aware
- reproducible

Thresholds MUST NOT be implicit or hidden inside unrelated logic.

## 8. Revocation

Revocation MUST:
- create a record,
- state the reason,
- state the scope,
- state whether reversal is possible.

## 9. Revalidation

A vector MAY be revalidated after revocation or suspension if the protocol allows it.

Revalidation MUST:
- reference the reason for prior invalidity,
- prove that the issue is resolved,
- create a new certification record.

## 10. Certification and drain interplay

A protocol MAY permit drain offsets using certification credit only if the policy explicitly states:
- how credit is earned,
- how it is consumed,
- whether it decays,
- whether it is transferable,
- whether it survives migrations.

## 11. Certification failure

If certification fails, the implementation MUST:
- reject the restricted action,
- preserve the current state,
- record the failure reason if the protocol logs failed attempts,
- avoid partial state mutation.

## 12. Security note

Certification is not ownership. A certified vector may still require separate authority checks for owner-bound actions.
