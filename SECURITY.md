# Security

## 1. Ownership model

Ownership is verified by cryptographic signature or a protocol-equivalent proof.

A vWallet owner MUST be able to demonstrate control over the associated public identity.

## 2. Private key handling

Private keys MUST NOT be exposed on the shared ledger.

Implementations SHOULD:
- store private keys locally or in secure hardware,
- avoid plaintext key export,
- rotate or migrate keys only via explicit protocol support,
- treat key compromise as a security incident.

## 3. Authorization

Ownership proof and authorization are distinct.

- Ownership proof shows control of the wallet identity.
- Authorization determines whether a specific operation is allowed.

A valid signature alone does not override certification, type, drain, or space constraints.

## 4. Signature verification

Signature verification MUST:
- bind the initiator to the requested operation,
- bind the request to the target vector or wallet,
- prevent replay when the protocol uses nonces or nonces-equivalent fields,
- fail closed on malformed input.

## 5. Threat model

The protocol SHOULD consider at least the following threats:
- replay attacks
- signature forgery
- double settlement
- double spend-like reuse
- malformed vector type injection
- unauthorized projection
- record rewriting
- cross-space confusion
- drain manipulation
- zero-vector normalization failure
- metadata spoofing

## 6. Defensive requirements

A compliant implementation SHOULD:
- use canonical serialization,
- validate all numeric bounds,
- reject negative or NaN values unless explicitly allowed,
- enforce atomic transition logic,
- log security-relevant events,
- separate custody from ledger visibility,
- use versioned rule sets.

## 7. Delegation

Delegated authority MAY be supported if the protocol explicitly defines:
- delegation scope
- expiry
- revocation
- replay protection
- audit trail

## 8. Recovery

If key compromise is detected, the protocol MAY provide:
- revocation,
- wallet freezing,
- owner reauthentication,
- migration to a new identity,
- emergency governance actions.

Every recovery action MUST be recorded.

## 9. Confidentiality

The protocol is not required to make all state private.

However, any sensitive material that is not necessary for validation SHOULD be minimized, encrypted, or referenced by commitment instead of disclosed directly.

## 10. Security baseline

A system is not compliant if it:
- exposes private keys,
- accepts unsigned owner-bound actions,
- fails to detect replay where replay protection is declared,
- allows hidden value creation,
- or silently bypasses certification.
