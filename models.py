from sqlalchemy import Column, Integer, String, Float, Text

from database import Base 
# สร้างโมเดลสำหรับฐานข้อมูล
class ItemDB(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)