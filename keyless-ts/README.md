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
} = require("@traittech/trait-keyless");
```

Example for AppAgent addresses:

```javascript
const appAgentId = 123;
const encodedAppAgentAddress = encodeAppAgent(appAgentId);
console.log("Encoded AppAgent address:", encodedAppAgentAddress);

const decodedAppAgentId = decodeAppAgent(encodedAppAgentAddress);
console.log("Decoded AppAgent ID:", decodedAppAgentId);

const decodedAppAgentAddress = decodeAddress(encodedAppAgentAddress);
console.log("Decoded AppAgent address:", decodedAppAgentAddress);
```

Example for Transactional addresses

```javascript
const taId = 456;
const encodedTaAddress = encodeTransactional(appAgentId, taId);
console.log("Encoded Transactional address:", encodedTaAddress);

const decodedTaId = decodeTransactional(encodedTaAddress);
console.log("Decoded Transactional ID:", decodedTaId);

const decodedTransactionalAddress = decodeAddress(encodedTaAddress);
console.log("Decoded Transactional address:", decodedTransactionalAddress);
```

Example for Named addresses

```javascript
const addressName = "hot-wallet";
const encodedNamedAddress = encodeNamed(appAgentId, addressName);
console.log("Encoded Named address [123, 'hot-wallet']:", encodedNamedAddress);

const decodedAddressName = decodeNamed(encodedNamedAddress);
console.log("Decoded address name:", decodedAddressName);

const decodedNamedAddress = decodeAddress(encodedNamedAddress);
console.log("Decoded Named address:", decodedNamedAddress);
```

Example for Regular addresses

```javascript
const encodedRegularAddress =
  "ttowKp8AmRn9nxt8Gcout4stYQem7TZNkhpnVmtpS5KG39m2Y";
const decodedRegularAddress = decodeAddress(encodedRegularAddress);
console.log("Decoded Regular address:", decodedRegularAddress);
```
