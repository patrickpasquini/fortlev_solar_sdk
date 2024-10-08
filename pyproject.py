from pathlib import Path
import requests

project_toml = Path("pyproject.toml")

git_hub_latest_release_url = (
    "https://api.github.com/repos/patrickpasquini/fortlev_solar_sdk/releases/latest"
)
response = requests.get(url=git_hub_latest_release_url)
VERSION = response.json()["tag_name"]


with open(project_toml, "r+") as file:
    data = file.read()
    new_data = data.replace("__VERSION__", VERSION)
    file.seek(0)
    file.truncate()
    file.write(new_data)
