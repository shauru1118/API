from pydantic import BaseModel

class Item(BaseModel):
    name: str
    id : int
    is_offer: bool | None = None

    def __repr__(self):
        return f"{self.name} {self.id} {self.is_offer}"
