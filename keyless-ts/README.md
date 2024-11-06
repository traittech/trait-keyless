# Keyless Address Encoding and Decoding Library

This library provides functions for encoding and decoding keyless addresses, including application agent addresses, transactional addresses, and named addresses.

## Usage

To use this library in your project, import the necessary functions and constants:

```javascript
const {
  encodeAppAgent,
  encodeTransactional,
  encodeNamed,
  AddressType,
  BlockchainAddressInfo,
  decodeAppAgent,
  decodeTransactional,
  decodeNamed,
  decodeAddress,
} = require("@trait-keyless/keyless-address");
```

## Encoding Addresses

```javascript
const appAgentId = 123;
const encodedAddress = encodeAppAgent(appAgentId);
console.log(encodedAddress);
```

## Decoding Addresses

```javascript
const encodedAddress = "ttowKp8AmRn9nxt8Gcout4stYQem7TZNkhpnVmtpS5KG39m2Y";
const appAgentId = decodeAppAgent(encodedAddress);
console.log(appAgentId);
```

## Test

```shell
npm run test
```
