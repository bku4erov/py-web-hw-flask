from abc import ABC

import pydantic

class AbstractAdvertisement(pydantic.BaseModel, ABC):
    title: str
    description: str
    owner_id: int
