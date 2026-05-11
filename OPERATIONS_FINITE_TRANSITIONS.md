# Operations Finite Transition Model

**Status:** Canonical allowed-transition reference  
**Version:** 1.1

## 1. Purpose

This document defines the finite set of canonical state transitions for the Vector Network core.

The canonical core operations are:

- CREATE
- CERTIFY
- TRANSFER
- DRAIN
- PROJECT
- RECONSTRUCT
- QUERY
- RECORD

No other operation is part of the v1 canonical core transition set unless introduced by a versioned extension spec.

## 2. State model

Let the operational state of a vector be represented by:

`σ = (v, owner, space, cert_state, proj_state, record_chain, status)`

Where:

- `v` = vector value
- `owner` = controlling wallet or custody binding
- `space` = active vector space
- `cert_state` = certification state
- `proj_state` = projection state
- `record_chain` = immutable history
- `status` = live/frozen/revoked/etc.

## 3. Canonical states

- `UNINITIALIZED`
- `PENDING`
- `CERTIFIED`
- `UNCERTIFIED`
- `SUSPENDED`
- `REVOKED`
- `ACTIVE`
- `PROJECTED`
- `SETTLED`
- `REPORTED` (query or record inspection only; no state mutation)

The exact state machine may vary by vector type, but the transition rules below define the core allowed transitions.

## 4. Transition table

| Operation | Allowed source states | Primary effect | Must create record |
|---|---|---|---|
| CREATE | UNINITIALIZED | create a new vector and origin record | yes |
| CERTIFY | PENDING, UNCERTIFIED, SUSPENDED | evaluate AuthRatio and update cert_state | yes |
| TRANSFER | CERTIFIED, ACTIVE | move permitted value to a destination | yes |
| DRAIN | CERTIFIED, ACTIVE, PROJECTED (if policy allows) | reduce transferable magnitude by explicit rule | yes |
| PROJECT | CERTIFIED, ACTIVE | lock value into a rule environment | yes |
| RECONSTRUCT | PROJECTED, SETTLED | return projected value under settlement rules | yes |
| QUERY | any readable state | read-only inspection | no |
| RECORD | any executable state | persist or retrieve immutable record entry | yes for write, no for read-only inspection |

## 5. Allowed transition rules

### 5.1 CREATE
`UNINITIALIZED -> PENDING -> CERTIFIED/UNCERTIFIED`

A new vector MAY begin in `PENDING` if certification is deferred.

### 5.2 CERTIFY
`PENDING|UNCERTIFIED|SUSPENDED -> CERTIFIED|UNCERTIFIED|SUSPENDED|REVOKED`

A certification operation MUST only change certification status.

### 5.3 TRANSFER
`CERTIFIED|ACTIVE -> CERTIFIED|ACTIVE`

Transfer changes ownership or destination linkage, not the underlying type semantics.

### 5.4 DRAIN
`CERTIFIED|ACTIVE|PROJECTED -> CERTIFIED|ACTIVE|PROJECTED`

Drain reduces value. It MUST NOT silently alter unrelated metadata.

### 5.5 PROJECT
`CERTIFIED|ACTIVE -> PROJECTED`

Projecting value locks a defined portion into a settlement environment.

### 5.6 RECONSTRUCT
`PROJECTED -> CERTIFIED|ACTIVE`

Reconstruction resolves the locked value and updates the free balance.

### 5.7 QUERY
No state change.

### 5.8 RECORD
Write path appends to the immutable chain.

## 6. Forbidden transitions

The following are forbidden in the canonical core:

- `REVOKED -> CERTIFIED` without explicit reauthorization or reorigin
- `PROJECTED -> PROJECTED` if it would duplicate settlement state
- `UNINITIALIZED -> TRANSFER`
- `UNINITIALIZED -> PROJECT`
- `REVOKED -> TRANSFER`
- `REVOKED -> PROJECT`
- `UNCERTIFIED -> TRANSFER` when certification is required
- any transition that mutates state without a record

## 7. Operation legality predicate

For any operation `op` and state `σ`:

`Allowed(op, σ, ctx) = preconditions(op, σ, ctx) ∧ validation(op, σ, ctx) ∧ policy(op, ctx)`

An operation is valid only if this predicate is true.

## 8. Read/write classification

### Read-only
- QUERY
- record inspection

### Write
- CREATE
- CERTIFY
- TRANSFER
- DRAIN
- PROJECT
- RECONSTRUCT
- RECORD write path

## 9. Determinism rule

For any allowed transition:

`F(op, σ, ctx) = σ'`

must be deterministic.

Same input state and same context MUST always produce the same output state and record payload.

## 10. Implementation note

This document is the canonical finite transition reference. Language specs, SDKs, and visualizations MUST reference this model rather than inventing new state transitions.
