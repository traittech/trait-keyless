# TRAIT Keyless Address Encoding and Decoding Library

This library provides functions for encoding and decoding keyless addresses, used by the TRAIT blockchain: application agent addresses, transactional addresses, and named addresses.

For more detailed docs, visit the README of the specific library:

- Typescript
  - Sources: [GitHub](./keyless-ts/)
  - Package: [NPM](https://www.npmjs.com/package/@traittech/trait-keyless)
- Python 
  - Sources: [GitHub](./keyless-python/)
- Rust
  - Sources: [GitHub](./keyless-rust/)
  - Package: [Crates.io](https://crates.io/crates/trait-keyless)

## Common terms

- **AppAgent**: on-chain entity that serves as a blockchain representation of an off-chain application;
- **Keyless address**: an address with unknown private key controlled by an AppAgent;
- **Address**: a 47-chars long address;
- **Account**: a 32-byte public key of an address;
- **Address type**: one of the possible address types;
- **AppAgent ID**: an identifier of an AppAgent `uint32`;
- **TA ID**: an identifier of a Transactional address, `uint32`;
- **Address name**: a name of a Named address, 10 ASCII characters from the list `0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-#`;
