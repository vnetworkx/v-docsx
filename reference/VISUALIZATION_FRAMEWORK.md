# Visualization Framework

**Status:** Architecture and protocol visualization layer  
**Version:** 1.1

## 1. Purpose

The visualization framework renders protocol state, record history, operation flow, and network topology.

It is observability-only. It MUST NOT modify kernel state.

## 2. Visualization goals

The framework SHOULD support:

- vector state diagrams
- record chain views
- certification dashboards
- operation flow charts
- projection lifecycle visuals
- network topology maps
- space-to-space synchronization views

## 3. Visual primitives

### 3.1 Vector node
Represents a vector state.

### 3.2 Wallet node
Represents a wallet identity and its bound vectors.

### 3.3 Record edge
Represents an immutable transition from one state to another.

### 3.4 Space boundary
Represents a vector space, shard, or execution domain.

### 3.5 Projection container
Represents locked or projected value.

## 4. Required diagrams

A compliant visualization suite SHOULD include the following diagram classes.

### 4.1 Canonical architecture diagram
```text
Users -> SDKs -> API Layer -> Kernel -> Records -> Sync -> Nodes
```

### 4.2 Operation pipeline diagram
```text
Request -> Validate -> Certify -> Execute -> Record -> Replicate
```

### 4.3 Vector lifecycle diagram
```text
CREATE -> CERTIFY -> TRANSFER / PROJECT / DRAIN -> RECONSTRUCT -> QUERY
```

### 4.4 Certification flow diagram
```text
Inputs -> Score factors -> AuthRatio -> Threshold -> Certified / Uncertified
```

### 4.5 Projection lifecycle diagram
```text
PROJECT -> LOCK -> SETTLE -> RECONSTRUCT
```

## 5. Chart types

The framework MAY render:

- sankey flows for value movement
- node-link graphs for network topology
- timelines for record history
- stacked bars for vector composition
- threshold gauges for AuthRatio
- state machines for operation legality

## 6. Visual rules

Visual outputs MUST:

- distinguish state from metadata
- show immutable records explicitly
- show certification state explicitly
- show drain as a separate stage when applied
- show projection and reconstruction as distinct lifecycle phases
- avoid implying hidden mutation

## 7. Architecture layers

### 7.1 Data layer
Reads records, state snapshots, and query results.

### 7.2 Model layer
Normalizes protocol entities into visual objects.

### 7.3 Render layer
Converts objects into charts, graphs, and diagrams.

### 7.4 Interaction layer
Supports filtering, zooming, and inspection.

## 8. Example visual mapping

| Protocol concept | Suggested visual |
|---|---|
| wallet | labeled node |
| vector | stacked component bar |
| transfer | directed edge |
| certification | gauge / badge |
| drain | loss segment |
| projection | lock box |
| reconstruction | return edge |
| record chain | linked timeline |

## 9. Non-goals

The visualization framework MUST NOT:

- decide legality
- create protocol records
- infer state not present in records
- override kernel validation
- alter source ordering
