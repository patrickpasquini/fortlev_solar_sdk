
# Fortlev Solar SDK Documentation

Welcome to the **Fortlev Solar SDK** Documentation. This library is designed to simplify integration with Fortlev Solar **APIs**.

## Installation

You can install the SDK using pip:

```bash
pip install fortlev_solar_sdk
```

## Getting Started

### Authenticate

First, you need to `authenticate`. Once authenticated, the token will be stored in the client, allowing you to access all the methods that require authentication.

```py
from fortlev_solar_sdk import FortlevSolarClient

client = FortlevSolarClient()
client.authenticate(username="john@doe.com", pwd="Mypassword123@")
```

If you don't have an account, you can use the `register` method to create one:

```py
client.register(name="John Doe", email="john@doe.com", phone_number="51924979815", cnpj="36528955000163", pwd="Mypassword123@")
```

### Available Features

Once you're set up, you can:

- **Create Orders**: Seamlessly create orders, fully integrated with Fortlev Solar's inventory.
```py
orders = client.orders(power=12, voltage="220", phase=1)
```
- **Simulate Financing Installments**: Run simulations for the financing installments of your photovoltaic kit.
```py
financing = client.financing(value=10000)
```

To explore all the available methods and their usage [Click here](reference/fortlev_solar_client)

## API Reference


For a complete reference of available endpoints, visit the official API documentation:

[Fortlev Solar API Documentation](https://api-platform.fortlevsolar.app/partner/docs)

## Fortlev Solar Platform

To access the Fortlev Solar platform, where you can manage your orders and more, visit:

[Fortlev Solar Platform](https://fortlevsolar.app)

## Contributing

We welcome contributions to the SDK! If you'd like to report an issue or contribute to the project, please visit our [GitHub repository](https://github.com/patrickpasquini/fortlev_solar_sdk).

---

For more detailed information on how to use each class and method in the SDK, please refer to the documentation sections in the sidebar.