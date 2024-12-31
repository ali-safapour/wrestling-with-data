from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hash(Base):
    __tablename__ = 'hash'
    id = Column(Integer, primary_key=True, index=True)
    hash_value = Column(String(256), unique=True, nullable=False)