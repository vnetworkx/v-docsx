# Vector Network Documentation Set (v-docsx)

This directory contains the master protocol specification for Vector Network and a set of supporting documents for researchers, developers, auditors, and implementers.

## Document map

- `SPEC.md` — master protocol rulebook and normative specification
- `GLOSSARY.md` — canonical terminology and field definitions
- `STATE_MODEL.md` — mathematical state model for vectors and vector spaces
- `OPERATIONS.md` — operational rules for transfer, projection, reconstruction, drain, and origin
- `CERTIFICATION.md` — certification, AuthRatio, validation, and rejection logic
- `RECORDS.md` — immutable record format and event log requirements
- `SECURITY.md` — ownership, signatures, key handling, and threat controls
- `ERRORS.md` — protocol error classes and failure handling
- `GOVERNANCE.md` — versioning, upgrades, parameters, and compatibility rules
- `EXAMPLES.md` — worked examples and learning-oriented scenarios
- `FORMALISM.md` — formal notation, invariants, and proof obligations
- `experiments.py` — small reference math utilities for testing and experimentation

## Reading order

1. Read `SPEC.md` first.
2. Use `GLOSSARY.md` for terminology.
3. Use `STATE_MODEL.md` and `FORMALISM.md` for formal structure.
4. Use `OPERATIONS.md`, `CERTIFICATION.md`, and `RECORDS.md` for implementation.
5. Use `EXAMPLES.md` and `experiments.py` for learning and validation.

## Normative language

The words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as normative requirements in the sense of a technical protocol specification.
