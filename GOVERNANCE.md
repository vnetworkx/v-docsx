# Governance and Versioning

## 1. Purpose

Governance defines how the protocol evolves while preserving historical validity.

## 2. Version fields

Each implementation SHOULD declare:
- protocol version
- schema version
- rule version
- space version
- serialization version

## 3. Change classes

### 3.1 Non-breaking changes
Examples:
- adding optional metadata
- adding new non-conflicting operation types
- clarifying documentation
- adding new record annotations

### 3.2 Breaking changes
Examples:
- changing component order
- changing valuation semantics
- changing drain law
- changing settlement rule meaning
- changing certification threshold interpretation

Breaking changes MUST use explicit version increments and compatibility policy.

## 4. Upgrade requirements

An upgrade MUST:
- preserve historical replay of old records,
- clearly mark the active version,
- define compatibility behavior,
- avoid ambiguity between old and new semantics.

## 5. Deprecation

Deprecated features MAY remain readable and replayable.

Deprecated features MUST NOT be the default for newly created state unless the protocol explicitly permits that behavior.

## 6. Parameter governance

Protocol parameters such as thresholds, drain rates, or settlement intervals MUST be:
- documented
- versioned
- auditable
- reproducible
- scoped to the correct space or type

## 7. Consensus on rule changes

If the network uses consensus or governance voting, the protocol MUST define:
- who may propose changes
- how changes are authorized
- when changes activate
- how pending changes are recorded
- how rollbacks are handled, if allowed

## 8. Backward compatibility

The protocol SHOULD preserve backward compatibility where practical.

If compatibility cannot be preserved, migration and translation rules MUST be published before activation.

## 9. Governance principle

No hidden rule changes.

Any change that affects interpretation, value, certification, or record validity MUST be surfaced as a versioned protocol event.
