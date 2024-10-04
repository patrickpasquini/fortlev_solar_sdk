from .base_classes import Identity, File
from dataclasses import dataclass


@dataclass
class Component(Identity):
    code: str
    attachments: list[File]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            code=data.get("code"),
            family=data.get("family"),
            attachments=[
                File.from_dict(attachment) for attachment in data.get("attachments", [])
            ],
        )
