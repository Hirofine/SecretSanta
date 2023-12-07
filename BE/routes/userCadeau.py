from config.db import get_db, Session
from sqlalchemy import text, or_
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, status
from fastapi.responses import StreamingResponse
from models.index import UserCadeaux, Users, UserLiens
from schemas.index import UserCadeau, UserCadeauCreate, UserCadeauUpdate
from crud.userCadeau import create_userCadeau, get_userCadeau, update_userCadeau, delete_userCadeau  # Importez les fonctions spécifiques

userCadeau = APIRouter()

@userCadeau.post("/userCadeaux/", response_model=UserCadeau)
def rt_create_userCadeau(userCadeau: UserCadeauCreate, db: Session = Depends(get_db)):
    userCadeau_data = dict(userCadeau)  # Convertit l'objet ImageCreate en dictionnaire
    return create_userCadeau(db, userCadeau_data)

@userCadeau.get("/userCadeaux/{id}", response_model=UserCadeau)
def rt_read_userCadeau(id: int, db: Session = Depends(get_db)):
    userCadeau = get_userCadeau(db, id)
    if userCadeau is None:
        raise HTTPException(status_code=404, detail="userCadeau not found")
    return userCadeau

@userCadeau.put("/userCadeaux/{id}", response_model=UserCadeau)
def rt_update_userCadeau(id: int, userCadeau: UserCadeauUpdate, db: Session = Depends(get_db)):
    updated_userCadeau = update_userCadeau(db, id, userCadeau)
    if updated_userCadeau is None:
        raise HTTPException(status_code=404, detail="userCadeau not found")
    return updated_userCadeau

@userCadeau.delete("/userCadeaux/{id}", status_code=status.HTTP_204_NO_CONTENT)
def rt_delete_userCadeau(id: int, db: Session = Depends(get_db)):
    success = delete_userCadeau(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="userCadeau not found")
    return None


@userCadeau.post("/generate/{year}")
def rt_generate(year: int, db: Session = Depends(get_db)):
    # get user list for year
    users = db.query(Users).all()
    liens = db.query(UsersLiens).all()

    print(users[0].pseudo)
    print(year)
    return None