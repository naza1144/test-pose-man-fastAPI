from pydantic import BaseModel

# สร้างคลาส Pydantic สำหรับการรับข้อมูลจากผู้ใช้
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

class item_created(Item):
    pass

class item_updated(Item):
    id: int
    class Config:
        from_attributtes = True

class ItemResponse(Item):
    id: int

    class Config:
        from_attributes = True

class ItemDelete(Item):
    id: int
    class Config:
        from_attributtes = True