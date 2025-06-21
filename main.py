from typing import Union,List
from fastapi import *
from sqlalchemy.orm import Session

from schema import *
from database import *
from models import * 

app = FastAPI()

# Create: สร้างสินค้าใหม่
@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    return db_item

@app.get("/items", response_model=List[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    db_items = db.query(ItemDB).all()
    return db_items


@app.post("/items", response_model=ItemResponse)

def create_item(item: item_created, db: Session = Depends(get_db)):
    db_item = ItemDB(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: item_created, db: Session = Depends(get_db)):
        db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        for key, value in item.model_dump().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
        db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        db.delete(db_item)
        db.commit()
        return {"message": "Item deleted successfully"}