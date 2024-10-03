from .auth import Auth
from .surface import Surface
from .component import Component
from .errors import AuthenticationError
import requests


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
            self._headers = {
                "Authorization": f"{self._auth.token_type} {self._auth.access_token}"
            }
            return self._auth
        raise AuthenticationError(
            status_code=response.status_code,
            error_message=response.json().get("detail", "Unknown error"),
        )

    def surfaces(self):
        url = f"{self.base_url}/{self._auth.scope}/surface"
        response = requests.get(url=url, headers=self._headers)
        if response.status_code == 200:
            docs = response.json().get("docs")
            surfaces = [Surface.from_dict(surface) for surface in docs]
            return surfaces

    def components(self):
        url = f"{self.base_url}/{self._auth.scope}/component/all"
        response = requests.get(url=url, headers=self._headers)
        if response.status_code == 200:
            docs = response.json().get("docs")
            components = [Component.from_dict(component) for component in docs]
            return components
