from config.db import get_db, Session
from sqlalchemy import text, or_
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, status
from fastapi.responses import StreamingResponse
from models.index import UserLiens
from schemas.index import UserLien, UserLienCreate, UserLienUpdate
from crud.userLien import create_userLien, get_userLien, update_userLien, delete_userLien  # Importez les fonctions spécifiques

userLien = APIRouter()

@userLien.post("/userLiens/", response_model=UserLien)
def rt_create_userLien(userLien: UserLienCreate, db: Session = Depends(get_db)):
    userLien_data = dict(userLien)  # Convertit l'objet ImageCreate en dictionnaire
    return create_userLien(db, userLien_data)

@userLien.get("/userLiens/{id}", response_model=UserLien)
def rt_read_userLien(id: int, db: Session = Depends(get_db)):
    userLien = get_userLien(db, id)
    if userLien is None:
        raise HTTPException(status_code=404, detail="userLien not found")
    return userLien

@userLien.put("/userLiens/{id}", response_model=UserLien)
def rt_update_userLien(id: int, userLien: UserLienUpdate, db: Session = Depends(get_db)):
    updated_userLien = update_userLien(db, id, userLien)
    if updated_userLien is None:
        raise HTTPException(status_code=404, detail="userLien not found")
    return updated_userLien

@userLien.delete("/userLiens/{id}", status_code=status.HTTP_204_NO_CONTENT)
def rt_delete_userLien(id: int, db: Session = Depends(get_db)):
    success = delete_userLien(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="userLien not found")
    return None
