from sqlalchemy.orm import Session
from ..models.hash_model import Hash, Base
from ..db import engine


def add_hash(db: Session, hash_value: str):
    db_hash = Hash(hash_value=hash_value)
    db.add(db_hash)
    db.commit()
    
    # Making sure the db_hash object is the same as the object that is in the database because the database might have triggered other mechanism that we don't know about
    db.refresh(db_hash)
    return db_hash

def hash_exists(db: Session, hash_value: str) -> bool:
    return db.query(Hash).filter(Hash.hash_value == hash_value).first() is not None