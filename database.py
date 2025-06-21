from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
# instance class เริ่มต้นสำหรับ engine, SessionLocal และ Base
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# สร้างตารางในฐานข้อมูล
Base.metadata.create_all(bind=engine)


# Dependency สำหรับสร้าง Session กับฐานข้อมูลในแต่ละคำร้องขอ
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
