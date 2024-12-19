from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    idx = Column(Integer, primary_key=True, index=True)
    id = Column(String(45), unique=True, index=True, nullable=False)
    name = Column(String(45), nullable=False)
    password = Column(String(255), nullable=False)  # 암호화된 비밀번호 저장
