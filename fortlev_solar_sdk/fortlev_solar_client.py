from .auth import Auth
from .surface import Surface
from .component import Component
from .city import City
from .errors import RequestError
from .order import Order
import requests
from typing import Literal


class FortlevSolarClient:

    base_url = "https://api-platform.fortlevsolar.app"

    def __init__(self) -> None:
        self._auth = None
        self._headers = None

    def authenticate(self, username: str, pwd: str):
        url = f"{self.base_url}/user/login"
        form_body = {"username": username, "password": pwd}
        response = requests.post(url=url, data=form_body)
        if response.status_code == 200:
            self._auth = Auth(
                access_token=response.json().get("access_token"),
                scope=response.json().get("scope"),
                token_type=response.json().get("token_type"),
            )
            token = f"{self._auth.token_type} {self._auth.access_token}"
            self._headers = {"Authorization": token}
            return self._auth
        raise RequestError(
            status_code=response.status_code,
            error_message=response.json().get("detail", "Unknown error"),
        )

    def base_request(self, endpoint: str, Model, query_params: dict = {}):
        url = f"{self.base_url}/{self._auth.scope}/{endpoint}"
        response = requests.get(url=url, headers=self._headers, params=query_params)
        if response.status_code == 200:
            docs = response.json().get("docs")
            return [Model.from_dict(doc) for doc in docs]
        raise RequestError(
            status_code=response.status_code,
            error_message=response.json().get("detail", "Unknown error"),
        )

    def surfaces(self, query_params: dict = {}) -> list[Surface] | RequestError:
        return self.base_request(
            endpoint="surface", Model=Surface, query_params=query_params
        )

    def components(self, query_params: dict = {}) -> list[Component] | RequestError:
        return self.base_request(
            endpoint="component/all", Model=Component, query_params=query_params
        )

    def cities(self, query_params: dict = {}) -> list[City] | RequestError:
        return self.base_request(
            endpoint="brazilian-city", Model=City, query_params=query_params
        )

    def orders(
        self,
        power: float = 0,
        voltage: Literal["220", "380", "+"] = "220",
        phase: Literal[1, 2, 3] = 1,
        surface: str = None,
        city: str = None,
    ):
        payload = {
            "target_power": power,
            "voltage": voltage,
            "phase": phase,
            "surface": surface,
            "brazilian_city": city,
        }
        response = requests.post(
            url=f"{self.base_url}/{self._auth.scope}/order",
            headers=self._headers,
            json=payload,
        )
        if response.status_code == 200:
            return [Order.from_dict(order) for order in response.json()]
        raise RequestError(
            status_code=response.status_code,
            error_message=response.json().get("detail", "Unknown error"),
        )
