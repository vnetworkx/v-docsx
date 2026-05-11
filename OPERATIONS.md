# Operations

This document defines the protocol semantics for the core operations.

## 1. Common preflight checks

Before any operation, an implementation MUST:

1. authenticate the caller,
2. verify authorization,
3. ensure the vector exists,
4. ensure the wallet exists,
5. verify type compatibility,
6. check certification if required,
7. validate parameters,
8. confirm the operation is permitted in the current space.

Failure at any stage MUST abort the operation.

## 2. Transfer

### 2.1 Purpose
Transfer moves vector value from one owner-bound context to another.

### 2.2 Requirements
A transfer MUST:
- specify source and destination
- specify amount or component subset
- respect type compatibility
- apply drain if required
- preserve record traceability

### 2.3 Postconditions
After a valid transfer:
- source balance decreases
- destination balance increases
- total preserved value matches the transfer law
- a record exists

## 3. Projection

### 3.1 Purpose
Projection locks part of a vector into a controlled process.

### 3.2 Required fields
A projection MUST specify:
- projection identifier
- locked components or amount
- rule environment
- settlement rule
- settlement trigger
- drain rule if applicable
- certification requirement

### 3.3 Semantics
During projection:
- locked value is not freely transferable unless explicitly allowed
- the projection must remain traceable
- settlement MUST be single-source-of-truth

### 3.4 Settlement outcomes
A settlement MAY result in:
- no change,
- gain,
- loss,
- partial release,
- staged release.

Every outcome MUST be encoded in the record stream.

## 4. Reconstruction

### 4.1 Purpose
Reconstruction returns projected value after settlement.

### 4.2 Requirements
A reconstruction MUST:
- reference a valid prior projection
- consume the projection exactly as defined
- apply the settlement rule exactly once unless the projection type explicitly allows multiple settlement phases
- prevent double reconstruction

### 4.3 Postconditions
The wallet MUST recover:
- the permitted returned principal,
- the settlement outcome,
- the final state required by the projection contract.

## 5. Drain

### 5.1 Purpose
Drain is an explicit protocol cost.

### 5.2 Drain forms
Drain MAY be:
- percentage-based,
- fixed-unit,
- tiered,
- type-based,
- space-based,
- operation-based,
- certification-offsettable.

### 5.3 Offset rules
A drain MAY be reduced by AuthRatio tokens or equivalent protocol credit only if the rule set explicitly provides that behavior.

The offset MUST be:
- bounded,
- deterministic,
- recorded,
- reversible only if the protocol explicitly allows reversal.

## 6. Certification check

### 6.1 Purpose
Certification determines eligibility.

### 6.2 Outcomes
Possible outputs are:
- certified
- uncertified
- suspended
- revoked
- pending

### 6.3 Effects
Restricted operations MUST reject non-certified states unless the specific operation is exempt.

## 7. Origin validation and creation

### 7.1 Purpose
Origin rules prevent unrestricted creation.

### 7.2 Requirements
A new vector MUST only be created if:
- the origin engine approves the creation path,
- the work or procedural proof is valid,
- the resulting vector is type-valid,
- the event is recorded,
- the certification rule is satisfied if required.

### 7.3 Anti-abuse rule
A protocol implementation MUST NOT accept a direct mint or creation bypass that skips origin validation.

## 8. Split

Split divides one vector into two or more vectors.

Rules:
- the split mapping MUST be explicit
- source components MUST map deterministically
- combined post-split value MUST match the source minus any declared drain

## 9. Merge

Merge combines vectors.

Rules:
- all inputs MUST be mutually compatible
- merge identity MUST be explicit
- component alignment MUST be deterministic
- any loss or drain MUST be declared

## 10. Freeze and unfreeze

Freeze locks a vector or wallet state from mutation.

Unfreeze restores permitted activity.

Rules:
- freeze MUST be reversible only through authorized action
- frozen state MUST be recorded
- freeze MUST NOT destroy underlying historical data

## 11. Migration

Migration changes the active vector space.

Rules:
- source and target spaces MUST be mutually compatible or explicitly bridged
- migration MUST preserve traceability
- incompatible fields MUST be normalized or rejected according to the target rules

## 12. Operational precedence

When multiple rules apply, precedence order is:

1. security and authentication
2. ownership authority
3. certification
4. type constraints
5. drain rules
6. settlement rules
7. record creation

## 13. Reference implementation note

An implementation SHOULD use atomic state transition logic so that partial application cannot occur.
