
# Fortlev Solar SDK Documentation

Welcome to documentation for the **Fortlev Solar SDK**. This SDK is designed to simplify the process of interacting with the Fortlev Solar API.

## Getting Started

The Fortlev Solar SDK provides easy-to-use methods for:

- **Register**: Register a new partner in the Fortlev Solar
- **Authentication**: Authenticate users and generate access token.
- **Surfaces**: Retrieve available surfaces for photovoltaic installations.
- **Components**: Access data for various solar components.
- **Cities**: Get a list of cities with available data.
- **Orders**: Create orders based on specific power, voltage, and phase parameters.

### Installation

You can install the SDK using pip:

```bash
pip install fortlev_solar_sdk
```

### Quick Example

Here's a quick example of how to use the SDK to authenticate and fetch available surfaces:

```python
from fortlev_solar_sdk import FortlevSolarClient

client = FortlevSolarClient()
client.authenticate(username="username", pwd="password")
orders = client.orders(power=5.0, voltage="220", phase=1, surface="surface_id", city="city_id")
for order in orders:
    print(order)
```

## API Reference

For a complete reference of available endpoints, visit the official API documentation:

[Fortlev Solar API Documentation](https://api-platform.fortlevsolar.app/partner/docs)

## Fortlev Solar Platform

To access the Fortlev Solar platform, where you can manage your orders and more, visit:

[Fortlev Solar Platform](https://fortlevsolar.app)

## Contributing

We welcome contributions to the SDK! If you'd like to report an issue or contribute to the project, please visit our [GitHub repository](https://github.com/patrickpasquini/fortlev_solar_sdk).
