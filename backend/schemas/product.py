from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    image_url: str
    attachment_url: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
