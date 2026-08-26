from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float

#datos de entrada
item = Item(name="Cafetera", price=120.0)
item_id = 505

resultado = {"item_id": item_id, **item.model_dump()}
print(resultado)