# Operations

This document defines the protocol semantics for the canonical core operations.

## 1. Scope

The canonical core operation set is finite:

- CREATE
- CERTIFY
- TRANSFER
- DRAIN
- PROJECT
- RECONSTRUCT
- QUERY
- RECORD

If an implementation supports extension operations such as split, merge, freeze, unfreeze, or migration, those operations MUST be defined in a separate versioned extension specification and MUST NOT be treated as part of the canonical v1 core.

## 2. Common preflight checks

Before any operation, an implementation MUST:

1. authenticate the caller
2. verify authorization
3. ensure the vector exists or is eligible for creation
4. ensure the wallet exists when a wallet-bound action is requested
5. verify type compatibility
6. check certification if required
7. validate parameters
8. confirm the operation is permitted in the current space
9. ensure zero-vector safety where relevant
10. ensure a record will be produced for state-changing actions

Failure at any stage MUST abort the operation.

## 3. CREATE

### 3.1 Purpose
Create a new origin-valid vector.

### 3.2 Requirements
A CREATE operation MUST:

- specify the intended type
- specify initial components or generation parameters
- use the origin engine or equivalent approved origin path
- satisfy any proof-of-effort or procedural proof requirement
- produce an origin record

### 3.3 Postconditions
After CREATE:

- the vector exists
- the vector has a valid origin reference
- the initial certification state is recorded
- hidden mutation is prohibited

## 4. CERTIFY

### 4.1 Purpose
Verify whether a vector may participate in restricted actions.

### 4.2 Requirements
A CERTIFY operation MUST:

- identify the target vector
- evaluate AuthRatio in the current context
- compare the score against the applicable threshold
- write the resulting certification state to the record stream

### 4.3 Postconditions
The result MUST be one of:

- certified
- uncertified
- suspended
- revoked
- pending

## 5. TRANSFER

### 5.1 Purpose
Transfer moves vector value from one owner-bound context to another.

### 5.2 Requirements
A TRANSFER operation MUST:

- specify source and destination
- specify amount or component subset
- respect type compatibility
- apply drain if required
- preserve record traceability
- reject if the source is not authorized or not certified when required

### 5.3 Postconditions
After a valid transfer:

- source balance decreases
- destination balance increases
- total transferred value follows the declared drain rule
- a record exists

## 6. DRAIN

### 6.1 Purpose
Drain is an explicit protocol cost.

### 6.2 Requirements
A DRAIN operation MUST:

- declare the drain rule
- declare the amount or formula
- declare whether offset credit is used
- define the destination of any collected value or the absence of one

### 6.3 Postconditions
After a valid drain:

- the drained portion is removed or redirected according to policy
- the effective drain is deterministic
- a record exists

## 7. PROJECT

### 7.1 Purpose
Project locks part of a vector into a controlled process.

### 7.2 Required fields
A PROJECT operation MUST specify:

- projection identifier
- locked components or amount
- rule environment
- settlement rule
- settlement trigger
- drain rule if applicable
- certification requirement

### 7.3 Semantics
During projection:

- locked value is not freely transferable unless explicitly allowed
- the projection must remain traceable
- settlement MUST be single-source-of-truth

### 7.4 Settlement outcomes
A settlement MAY result in:

- no change
- gain
- loss
- partial release
- staged release

Every outcome MUST be encoded in the record stream.

## 8. RECONSTRUCT

### 8.1 Purpose
Reconstruction returns projected value after settlement.

### 8.2 Requirements
A RECONSTRUCT operation MUST:

- reference a valid prior projection
- consume the projection exactly as defined
- apply the settlement rule exactly once unless the projection type explicitly allows multiple settlement phases
- prevent double reconstruction
- preserve traceability to the original projection record

### 8.3 Postconditions
The wallet MUST recover:

- the permitted returned principal
- the settlement outcome
- the final state required by the projection contract

## 9. QUERY

### 9.1 Purpose
Query reads wallet state, records, certification, projection status, origin status, or network state.

### 9.2 Rules
Query does not change ledger state.

Query MAY return:

- vector state
- wallet state
- record history
- certification status
- projection status
- origin status
- network metadata

## 10. RECORD

### 10.1 Purpose
Persist an immutable state transition entry.

### 10.2 Requirement
Every successful state-changing operation MUST produce a record.

Read-only inspection of existing records does not itself need to create a new record unless the protocol explicitly logs reads.

## 11. Validation order

The recommended order for state-changing operations is:

1. security and authentication
2. ownership authority
3. certification
4. type constraints
5. drain rules
6. settlement rules
7. state mutation
8. record creation

## 12. Determinism

All core operations MUST be deterministic:

- same state
- same inputs
- same policy version

=> same output and same record content, modulo timestamp or proof fields that are themselves derived deterministically or canonically signed.

## 13. Reference implementation note

An implementation SHOULD use atomic state transition logic so that partial application cannot occur.

## 14. Core operation summary

| Operation | State change | Record required |
|---|---|---|
| CREATE | yes | yes |
| CERTIFY | yes | yes |
| TRANSFER | yes | yes |
| DRAIN | yes | yes |
| PROJECT | yes | yes |
| RECONSTRUCT | yes | yes |
| QUERY | no | no |
| RECORD | write path yes / read path no | yes on write |
