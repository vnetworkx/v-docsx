# Vector Network Overview

Vector Network is best understood as a layered ecosystem.

At the center is a deterministic kernel. Around that kernel are the network, the language tools, the SDKs, the wallet layer, the contract layer, and the visualization layer. Each piece has a role, but none of them replace the kernel as the source of truth.

This document gives a broad view of the whole system and shows how the main parts fit together.

## The ecosystem in one picture

You can think of the project as having these layers:

1. **Concept layer**  
   The idea of vector-based value and vector spaces.

2. **Protocol layer**  
   The rules for vector creation, transfer, drain, projection, reconstruction, certification, and recordkeeping.

3. **Kernel layer**  
   The deterministic execution engine that validates and applies state changes.

4. **Network layer**  
   Nodes that replicate records, synchronize state, and maintain consensus.

5. **Developer layer**  
   SDKs, CLI tools, language compilers, simulators, and testing tools.

6. **Application layer**  
   Wallets, dashboards, explorers, contracts, and custom applications.

The structure matters because it keeps the system clean. The core rules stay in one place, while the outer layers make the system usable.

## What the network is trying to do

Vector Network is designed to support a broad set of decentralized actions:

- create vector state
- certify vector validity
- transfer value between spaces
- apply drain or fee logic
- project value into contracts or risk environments
- reconstruct value after settlement
- query state and records
- replicate the ledger across nodes
- maintain deterministic history
- expose a friendly developer experience

Instead of being only a ledger or only an app platform, the project aims to be a **vector-native protocol environment**.

## Why the kernel matters

The kernel is the most important part of the system because it defines what is valid.

If two wallets, two apps, or two nodes disagree, the kernel rules decide the answer. That keeps the system deterministic and makes replay possible.

A kernel-driven model helps in several ways:

- it reduces ambiguity
- it makes validation consistent
- it prevents hidden state mutation
- it keeps records meaningful
- it allows different clients to behave the same way
- it makes future protocol upgrades easier to reason about

In other words, the kernel is not just a backend. It is the protocol itself.

## How nodes fit in

Nodes are responsible for storing and sharing the history of the network.

A node typically handles:

- live state
- immutable records
- indexes
- sync metadata
- query APIs
- validation results
- record propagation

Nodes do not invent the rules. They enforce and replicate them.

In a healthy network, nodes should be able to independently replay the same record sequence and arrive at the same result. That is what deterministic design is for.

## How wallets fit in

A wallet in Vector Network is not just a signing tool. It is a user-facing way to manage a vector state.

Wallet responsibilities can include:

- key generation
- key storage
- signing
- recovery
- transaction construction
- state display
- transfer preview
- certification visibility
- history inspection

The wallet should help users understand what is happening, but it should never silently override the kernel.

## How contracts fit in

Contracts are rule-bound environments where vector state can be projected, transformed, and settled.

They can be used for things like:

- staking rules
- rewards
- escrow
- access control
- pooled value logic
- settlement policies
- risk-based projection environments

A contract is best thought of as a controlled vector space with explicit rules. The contract logic may transform projected state, but the result must still be recorded and validated deterministically.

## How the language layer fits in

The Vector Language is a higher-level way to express protocol actions.

It might eventually support:

- declaring vectors
- sending transfers
- applying drain rules
- projecting state
- reconstructing outcomes
- querying state
- expressing contract policies
- composing reusable logic

This language is not the source of truth. It is a way to describe instructions that the kernel can execute.

## How SDKs fit in

SDKs are the developer bridge between applications and the network.

They are meant to provide safe, convenient access from common programming environments such as Python, TypeScript, Rust, Java, Go, Swift, and Kotlin.

An SDK should help developers:

- connect to nodes
- sign requests
- submit operations
- inspect records
- query state
- verify proofs
- handle wallet workflows
- integrate the network into apps

SDKs should be trustworthy and boring in the best possible way: they should package the rules cleanly without changing them.

## How visualization fits in

Vector systems can be hard to understand if they are only shown as raw data. That is why visualization matters.

Visualization tools can show:

- vector composition
- magnitude over time
- wallet flow graphs
- contract state changes
- ledger history
- node topology
- certification status
- projection and settlement paths

A good visualization layer helps people see the system instead of just reading it.

## Why this is not “just a blockchain”

Vector Network is not framed as a standard blockchain because the emphasis is different.

Traditional chain systems often center around blocks, simple balances, and transaction ordering.

Vector Network centers around:

- multidimensional state
- deterministic kernel rules
- certification and policy logic
- vector operations
- record-based history
- space-based architecture
- protocol-native transformations

That does not mean the network cannot borrow ideas from blockchain design. It means the project is aiming for a broader model with its own vocabulary and architecture.

## The naming style

The naming style is part of the identity of the project.

Examples:

- **vNetworkx** — the broader vector network space
- **v-kernelx** — the kernel execution environment
- **v-authx** — certification and authorization logic
- **v-walletx** — wallet and signing environment
- **v-nodex** — node and sync environment
- **v-contractx** — contract runtime space

The pattern makes the ecosystem easier to organize and understand. It also reinforces the idea that each module lives inside a space, not just a codebase.

## A practical way to understand the architecture

If you are new to the project, this mental model helps:

- **the protocol** defines the rules
- **the kernel** enforces the rules
- **the network** shares the results
- **the wallet** lets people interact
- **the SDK** helps developers build
- **the contract layer** adds programmable policy
- **the explorer** helps humans inspect everything

That is the overall shape of the system.

## What the overview is meant to do

This overview is not the final technical specification. It is the bridge between the idea and the implementation.

It should help readers understand:

- what Vector Network is
- what parts it contains
- how those parts depend on each other
- why deterministic design matters
- why vector state is the core abstraction
- why the system is broader than a standard ledger

## In short

Vector Network is a layered decentralized ecosystem where vector state is created, validated, transformed, recorded, and synchronized through a deterministic kernel and a network of spaces around it.
