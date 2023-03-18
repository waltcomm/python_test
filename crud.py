from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_first_name(db: Session, first_name: str):
    return db.query(models.User).filter(models.User.first_name == first_name).first()

def get_user_by_last_name(db: Session, last_name: str):
    return db.query(models.User).filter(models.User.last_name == last_name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(first_name=user.first_name, last_name = user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: schemas.User):
    db_user: schemas.User
    db_user = Session.get(db, models.User, user.id)
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db.commit()
    return db_user
