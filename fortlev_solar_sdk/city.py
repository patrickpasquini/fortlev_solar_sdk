from dataclasses import dataclass


@dataclass
class City:
    id: str
    name: str
    ibge_code: str
    isopleth: int
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            ibge_code=data.get("ibge_code"),
            isopleth=data.get("isopleth"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
        )
