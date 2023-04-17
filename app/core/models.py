from datetime import datetime

from pydantic import BaseModel


class ModelCollectionNovels(BaseModel):
    name: str
    year: int
    actor: str
    inserted_at: datetime
