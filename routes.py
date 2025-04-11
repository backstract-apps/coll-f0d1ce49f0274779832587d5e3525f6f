from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/id')
async def get_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(raw_data: schemas.PostStudents, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/id/')
async def put_students_id(id: str, user: str, password: str, name: str, db: Session = Depends(get_db)):
    try:
        return await service.put_students_id(db, id, user, password, name)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/id')
async def delete_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

