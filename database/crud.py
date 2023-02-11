from sqlalchemy.orm import Session

from database import models, schemas

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.username == user_id).first()

def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate, datatype: models.check_data_type):
    db_user = models.User(
        username=datatype.username,
        password=user.password,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()

    db.refresh(db_user)

    return db_user