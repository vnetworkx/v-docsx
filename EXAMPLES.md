# Examples

These examples are educational. They illustrate the protocol concepts without introducing implementation-specific shortcuts.

## 1. Basic vector

A wallet holds:

`v = (10, 5, 0)`

This vector has:

- dimension `n = 3`
- magnitude `M(v) = 15`
- a defined type

If the type requires non-negative values, this vector is valid.

## 2. Certification example

Suppose the context yields:

- `M = 0.95`
- `C = 0.90`
- `O = 0.80`
- `X = 0.70`

With weights:

- `w1 = 0.35`
- `w2 = 0.25`
- `w3 = 0.25`
- `w4 = 0.15`

Then:

`AuthRatio = (0.35*0.95) + (0.25*0.90) + (0.25*0.80) + (0.15*0.70) = 0.8575`

If the threshold is `0.80`, the vector is certified.

## 3. Transfer example

Wallet A transfers 4 units from component 1 to Wallet B.

Before:
- A = `(10, 5, 0)`
- B = `(1, 1, 1)`

After:
- A = `(6, 5, 0)`
- B = `(5, 1, 1)`

If a drain of 1 unit applies, the protocol MUST define whether that 1 unit is removed from the source, collected by the network, or allocated according to a settlement rule. The choice MUST be explicit.

## 4. Projection example

Wallet A projects 5 units from `v = (10, 5, 0)`.

Possible state:

- free portion = `(5, 5, 0)`
- projected portion = `(5, 0, 0)`

The projection contract MUST define:

- where the locked value lives
- what settlement means
- when reconstruction is allowed

## 5. Reconstruction example

After settlement, projected value may return as:

- principal returned
- gain added
- loss applied

If the settlement result is a gain of 2 units, the final reconstructed outcome MUST reflect that exact rule and MUST be traceable to the original projection.

## 6. Zero vector example

`v = (0, 0, 0)`

Properties:

- magnitude = 0
- normalization is undefined
- transfer may be a no-op if the protocol allows no-op transfer
- any operation that assumes a non-zero denominator MUST fail safely

## 7. Origin example

A new vector is created from verified effort.

The origin engine MUST attach:

- the origin proof
- the creation rule set
- the new vector type
- the certification result or pending status

Unverified creation is invalid.

## 8. Record example

A record could conceptually look like:

`R = (v_before, v_after, "TRANSFER", {amount: 4}, "CERTIFIED", timestamp, proof)`

A production implementation SHOULD add structured identifiers and canonical serialization details.

## 9. Vector Language example

```vector
vector treasury: free = (100, 25, 0);
wallet treasury_owner = bind(pk_treasury);
certify treasury with ctx(space="global", op="transfer");
transfer treasury to reserve amount 10;
project treasury into staking_pool amount 20;
reconstruct treasury from proj_001;
query treasury.certification;
```

## 10. SDK example

```ts
const tx = await client.operations.transfer({
  source: "wallet_a",
  destination: "wallet_b",
  amount: 4,
});

if (!tx.accepted) {
  throw new Error(tx.error_code);
}
```

## 11. State transition example

Allowed canonical sequence:

`CREATE -> CERTIFY -> TRANSFER -> PROJECT -> RECONSTRUCT -> QUERY`

A direct `TRANSFER` on an uninitialized vector is invalid.

## 12. Learning note

The easiest way to think about the protocol is:

- vector = state
- wallet = owner-bound container
- space = rule environment
- record = immutable history
- certification = permission gate
- projection = locked process
- reconstruction = controlled return
- drain = explicit cost
- origin = authorized creation
