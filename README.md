
# Fortlev Solar SDK Documentation

This SDK is designed to simplify the process of interacting with the Fortlev Solar API.

## Documentation

**Go to:** [Docs](https://patrickpasquini.github.io/fortlev_solar_sdk/)

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
