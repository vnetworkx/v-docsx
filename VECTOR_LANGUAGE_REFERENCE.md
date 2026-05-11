# Vector Language Reference

**Status:** Informative reference  
**Version:** 1.1

This document is a compact reference for the native Vector Language.

## 1. Keywords

`vector`, `wallet`, `bind`, `certify`, `transfer`, `drain`, `project`, `reconstruct`, `query`, `record`

## 2. Core forms

### 2.1 Vector declaration
```vector
vector <name>: <type> = (<x1>, <x2>, ..., <xn>);
```

### 2.2 Wallet binding
```vector
wallet <name> = bind(<public_key>);
```

### 2.3 Certification
```vector
certify <vector_name> with <context>;
```

### 2.4 Transfer
```vector
transfer <source> to <destination> amount <amount>;
```

### 2.5 Drain
```vector
drain <vector_name> by <expression>;
```

### 2.6 Project
```vector
project <vector_name> into <environment> amount <amount> [policy <policy_id>];
```

### 2.7 Reconstruct
```vector
reconstruct <vector_name> from <projection_id>;
```

### 2.8 Query
```vector
query <expression>;
```

### 2.9 Record
```vector
record <event_id>;
```

## 3. Type tags

- `position`
- `free`
- `bound`
- `unit`
- `zero`

## 4. Context fields

A context MAY include:

- `space`
- `op`
- `risk`
- `threshold_version`
- `policy`
- `certification_state`

## 5. Common constraints

- Components MUST be nonnegative unless the type explicitly allows signed components.
- Zero normalization is undefined unless explicitly modeled.
- Transfer and projection MUST specify amount or component mapping.
- Restricted actions MUST pass certification.
- Every successful mutation MUST record.

## 6. Example snippets

```vector
vector treasury: free = (100, 25, 0);
wallet treasury_owner = bind(pk_treasury);
certify treasury with ctx(space="global", op="transfer");
transfer treasury to reserve amount 10;
project treasury into staking_pool amount 20;
query treasury.certification;
```

## 7. Compilation note

The runtime must not treat this language as a source of truth. It is a front end for kernel operations only.
