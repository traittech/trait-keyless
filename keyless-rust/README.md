# TRAIT Keyless Address Encoding and Decoding Library

This library provides functions for encoding and decoding keyless addresses, used by the TRAIT blockchain: application agent addresses, transactional addresses, and named addresses.

A keyless address is a type of address that doesn't rely on cryptographic key pairs for identification.
Instead, it is derived from a combination of identifiers and checksums, making it suitable and
convenient for off-chain applications to use.

## Example

```rust
use trait_keyless::*;

// Encode an AppAgent keyless address
let app_agent_id = 123;
let app_agent_address = encode_app_agent_account(&app_agent_id);

// Decode the keyless address
let decoded_app_agent_id = decode_app_agent_account(&app_agent_address).unwrap();
assert_eq!(decoded_app_agent_id, app_agent_id);
```
