from pydantic import BaseModel, PydanticUserError

try:
    class Item(BaseModel):
        my_name: str = None
        desc: str = None
        price: float = 0.00
        tax: float = 0.00
except PydanticUserError as exc_info:
    print(exc_info)
