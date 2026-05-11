# Vector Language Specification

**Status:** Canonical language layer specification  
**Version:** 1.1  
**Target:** The Vector Network kernel

## 1. Purpose

Vector Language is a native protocol language that compiles into kernel operations. It is a control layer, not the source of truth.

The language MUST preserve the kernel's deterministic semantics, record requirements, and validation rules.

## 2. Design goals

Vector Language MUST support:

- vector declaration
- wallet binding
- transfer
- drain
- project
- reconstruct
- certify
- query
- record inspection
- deterministic contract logic

It MUST NOT allow hidden state mutation or nondeterministic execution in kernel-affecting code.

## 3. Language model

A program is a sequence of declarations and operations:

`Program := {Statement}*`

Each statement compiles to one or more kernel operations.

The compiler pipeline is:

`parse -> validate -> normalize -> compile -> execute -> record`

## 4. Canonical grammar sketch

The grammar below is normative at the conceptual level.

```ebnf
Program         := Statement*
Statement       := VectorDecl | WalletDecl | CertifyStmt | TransferStmt | DrainStmt
                 | ProjectStmt | ReconstructStmt | QueryStmt | RecordStmt
VectorDecl      := "vector" Ident ":" VectorType "=" VectorLiteral ";"
WalletDecl      := "wallet" Ident "=" "bind" "(" PubKey ")" ";"
CertifyStmt     := "certify" Ident "with" Context ";"
TransferStmt    := "transfer" Ident "to" Ident "amount" Amount [DrainClause] ";"
DrainStmt       := "drain" Ident "by" DrainExpr ";"
ProjectStmt     := "project" Ident "into" Ident "amount" Amount [PolicyClause] ";"
ReconstructStmt := "reconstruct" Ident "from" Ident ";"
QueryStmt       := "query" QueryExpr ";"
RecordStmt      := "record" Ident ";"
```

A deployment MAY extend the grammar only through versioned additions.

## 5. Core types

### 5.1 Vector literal
A vector literal is an ordered, nonnegative component tuple:

`(x1, x2, ..., xn)`

### 5.2 Vector type
A type tag describes operational behavior:

- `position`
- `free`
- `bound`
- `unit`
- `zero`

### 5.3 Context
Context includes:

- operation class
- vector type
- space policy
- certification rules
- threshold version
- drain policy
- settlement policy

## 6. Semantic rules

### 6.1 Deterministic execution
The same input program and the same starting state MUST produce the same output state and record sequence.

### 6.2 Zero safety
The language MUST reject operations that attempt to normalize a zero vector unless the operation explicitly defines zero handling.

### 6.3 Ownership checks
Owner-bound operations MUST require a valid wallet binding and proof.

### 6.4 Recordability
Every successful state-changing statement MUST produce at least one immutable record.

### 6.5 Failure semantics
Any invalid statement MUST fail before state mutation.

## 7. Operation mapping

| Language construct | Kernel operation |
|---|---|
| `vector` | CREATE |
| `certify` | CERTIFY |
| `transfer` | TRANSFER |
| `drain` | DRAIN |
| `project` | PROJECT |
| `reconstruct` | RECONSTRUCT |
| `query` | QUERY |
| `record` | RECORD |

## 8. Examples

### 8.1 Declaration
```vector
vector v1: free = (10, 5, 0);
wallet w1 = bind(pk_abc123);
```

### 8.2 Certify
```vector
certify v1 with ctx(space="main", op="transfer", risk="normal");
```

### 8.3 Transfer
```vector
transfer v1 to v2 amount 4;
```

### 8.4 Projection
```vector
project v1 into poolA amount 5 policy "settle-on-close";
```

### 8.5 Reconstruction
```vector
reconstruct v1 from proj_001;
```

### 8.6 Query
```vector
query wallet(w1).certification;
```

## 9. Compiler contract

A compliant compiler MUST:

- reject ambiguous syntax
- preserve source-to-operation traceability
- emit canonical operation parameters
- preserve record determinism
- version its output schema

## 10. Runtime contract

A compliant runtime MUST:

- validate against the kernel rules before submission
- never bypass certification or ownership checks
- never fabricate records
- never infer hidden drain or settlement behavior

## 11. Versioning

Vector Language MUST carry a language version and a target protocol version.

A compiled artifact MUST state:

- language version
- grammar version
- target kernel version
- feature flags used
- policy references
