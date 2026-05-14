# Errors

This document defines protocol-level error classes.

## 1. General rule

Errors MUST be explicit. Invalid operations MUST fail closed.

## 2. Core error classes

### 2.1 `ERR_AUTH_FAILED`
Authentication or signature verification failed.

### 2.2 `ERR_UNAUTHORIZED`
The caller is not permitted to perform the requested action.

### 2.3 `ERR_UNCERTIFIED`
The vector does not satisfy certification requirements.

### 2.4 `ERR_INVALID_TYPE`
The vector type or operation type is unknown or incompatible.

### 2.5 `ERR_INVALID_STATE`
The requested state transition is not allowed in the current state.

### 2.6 `ERR_INVALID_DRAIN`
Drain parameters are missing, malformed, or not permitted.

### 2.7 `ERR_INVALID_PROJECTION`
Projection parameters or settlement rules are incomplete or inconsistent.

### 2.8 `ERR_INVALID_RECONSTRUCTION`
The reconstruction request does not match a valid prior projection.

### 2.9 `ERR_ORIGIN_DENIED`
The origin engine rejected creation.

### 2.10 `ERR_ZERO_NORMALIZATION`
Normalization was requested for a zero vector without a guard.

### 2.11 `ERR_RECORD_CONFLICT`
A record cannot be committed because it conflicts with existing canonical history.

### 2.12 `ERR_REPLAY_MISMATCH`
Replay produced a state different from the recorded post-state.

## 3. Error handling rules

An implementation MUST:
- preserve the pre-state on failure,
- not partially commit forbidden changes,
- log the error if logging is enabled,
- present errors in a stable machine-readable form.

## 4. Recoverability

Some errors are recoverable:
- `ERR_UNCERTIFIED`
- `ERR_INVALID_TYPE`
- `ERR_INVALID_DRAIN`
- `ERR_INVALID_PROJECTION`

Some errors are security-critical:
- `ERR_AUTH_FAILED`
- `ERR_UNAUTHORIZED`
- `ERR_RECORD_CONFLICT`
- `ERR_REPLAY_MISMATCH`

Security-critical errors SHOULD trigger heightened logging or monitoring.

## 5. Human-readable messages

Human-readable messages MAY accompany error codes, but the code MUST remain the authoritative machine interface.
