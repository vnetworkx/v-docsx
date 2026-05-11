# SDK Function Contracts

**Status:** Interface-level contract reference  
**Version:** 1.1

## 1. Global rules

All SDK functions MUST:

- be deterministic in serialization
- preserve protocol versioning
- validate required arguments
- return typed success or failure values
- avoid silent state assumptions

## 2. Wallet functions

### `create_wallet()`
Creates a local wallet container.

**Returns:** wallet object with public/private key material managed locally.

### `bind_wallet(public_key)`
Binds an SDK client session to an on-network wallet identifier.

**Must validate:** key shape, compatibility, and session rules.

### `sign(request)`
Produces a signature over the canonical request payload.

**Must ensure:** stable serialization before signing.

## 3. Operation submission functions

### `create(params)`
Submits a CREATE request.

**Preconditions:**
- origin path is permitted
- parameters are complete
- required proof is present

### `certify(vector_id, context)`
Submits a CERTIFY request.

**Preconditions:**
- vector exists
- context is explicit
- threshold policy is known

### `transfer(source, destination, amount, options?)`
Submits a TRANSFER request.

**Preconditions:**
- source and destination exist
- authority is valid
- amount is within bounds
- drain option, if used, is explicit

### `drain(vector_id, amount_or_rule, options?)`
Submits a DRAIN request.

**Preconditions:**
- drain rule is explicit
- offset behavior is explicit if present

### `project(vector_id, environment_id, amount, policy?)`
Submits a PROJECT request.

**Preconditions:**
- environment exists or is declared
- settlement model is explicit
- locked portion is defined

### `reconstruct(vector_id, projection_id)`
Submits a RECONSTRUCT request.

**Preconditions:**
- projection exists
- projection has not already been settled beyond its allowed phases

### `query(expression)`
Performs a read-only query.

**Preconditions:**
- expression is valid and deterministic

### `record(record_id)`
Fetches or inspects a record.

## 4. Response contracts

### Success
On success, functions SHOULD return:

- canonical receipt
- record id
- state delta
- certification result if applicable
- server hash or proof reference

### Failure
On failure, functions SHOULD return:

- machine-readable error code
- human-readable message
- recoverability flag
- fields that failed validation

## 5. Error contract

SDKs SHOULD normalize errors into a stable set such as:

- `INVALID_ARGUMENT`
- `MISSING_PROOF`
- `CERTIFICATION_FAILED`
- `AUTHORIZATION_FAILED`
- `TYPE_MISMATCH`
- `ZERO_VECTOR_INVALID`
- `UNKNOWN_POLICY`
- `DRAIN_RULE_UNDEFINED`
- `PROJECTION_ALREADY_SETTLED`
- `RECORD_CONFLICT`
- `PROTOCOL_VERSION_UNSUPPORTED`

## 6. Idempotency

State-changing functions SHOULD accept an idempotency key where the transport permits retries.

The kernel remains the source of truth for whether a repeated request is accepted or deduplicated.
