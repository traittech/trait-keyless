# Keyless Addresses Python Library

This Python library provides functionality for encoding and decoding keyless addresses. 

A keyless address is a type of address that doesn't rely on cryptographic key pairs for identification. Instead, it is derived from a combination of identifiers and checksums, making it suitable for various use cases such as tracking and verification.

## Installation

You can install the library using pip:

``` python3
pip install traitkeyless
```

## Usage

### Encode and Decode AppAgent Addresses

``` python3
import traitkeyless

app_agent_id = 123

# Encode an AppAgent address
encoded_address = traitkeyless.encode_app_agent_address(app_agent_id)
assert encoded_address == "ttowKp8AmRn9nxt8Gcout4stYQem7TZNkhpnVmtpS5KG39m2Y"

# Decode the AppAgent address
decoded_app_agent_id = traitkeyless.decode_app_agent_address(encoded_address)
assert decoded_app_agent_id == 123
```

### Encode and Decode Transactional Addresses

``` python3
import traitkeyless

app_agent_id = 123
transactional_address_id = 456

# Encode a Transactional address
encoded_address = traitkeyless.encode_transactional_address(app_agent_id, transactional_address_id)
assert encoded_address == "ttowKp8AmjjQh4HoMJwdKPyEQS5HSXQHwBUrLbn2LJFopLG85"

# Decode the Transactional address
decoded_data = traitkeyless.decode_transactional_address(encoded_address)
assert decoded_data == (123, 456)
```

### Encode and Decode Named Addresses

``` python3
import traitkeyless

app_agent_id = 123
address_name = "example123"

# Encode a Named address
encoded_address = traitkeyless.encode_named_address(app_agent_id, address_name)
assert encoded_address == "ttowKp8Amrt2FQ2eNdsbMsWDhEDiavXcVdeJBhQE7ttL1np4c"

# Decode the Named address
decoded_data = traitkeyless.decode_named_address(encoded_address)
assert decoded_data == (123, "example123")
```

### Decode any address

``` python3
import traitkeyless

app_agent_id = 123

# Encode a Named address
encoded_address = traitkeyless.encode_app_agent_address(app_agent_id)
assert encoded_address == "ttowKp8AmRn9nxt8Gcout4stYQem7TZNkhpnVmtpS5KG39m2Y"

# Decode the Named address
decoded_data = traitkeyless.decode_address(encoded_address)
expected_data = traitkeyless.BlockchainAddressInfo(
    address=encoded_address,
    account_id="0x7b000000013c8b3aeb6b293833058fc7db52fc03f6ce344bca98bd7825ff7477",
    address_type=traitkeyless.AddressType.AppAgent,
    app_agent_id=123,
    ta_id=None,
    address_name=None,
)
assert decoded_data == expected_data
```

## Development

To generate python stub files:

`stubgen traitkeyless/keyless.py`