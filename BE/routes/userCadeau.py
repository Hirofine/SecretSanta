from config.db import get_db, Session
from sqlalchemy import text, or_
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, status, Request
from helper import verify_token, user_id_from_token, TOKEN_VALIDE, TOKEN_EXPIRE, TOKEN_INVALIDE, TOKEN_NOT_SENT, USER_NOT_EXISTANT
from fastapi.responses import StreamingResponse, JSONResponse
from models.index import UserCadeaux, Users, UserLiens
from schemas.index import UserCadeau, UserCadeauCreate, UserCadeauUpdate, User
from crud.userCadeau import create_userCadeau, get_userCadeau, update_userCadeau, delete_userCadeau  # Importez les fonctions spécifiques
import random

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

@userCadeau.get("/userCadeau/")
def rt_get_cadeau(request: Request, db: Session = Depends(get_db)):
    tok = verify_token(request, db)
    if (tok == TOKEN_VALIDE):
        id = user_id_from_token(request, db)
        kdo = db.query(UserCadeaux).filter(UserCadeaux.user1id == id).first()
        if kdo == None:
            raise HTTPException(status_code=404, message="Erreur: pas de cadeau trouvé pour cet utilisateur")
        user = db.query(Users).filter(Users.id == kdo.user2id).first()
        if user == None:
            raise HTTPException(status_code=404, message="Erreur: pas de cadeau trouvé pour cet utilisateur")
        return user
    elif (tok == TOKEN_EXPIRE):
        return JSONResponse(content={"message": "Session expirée", "data" : False})
    elif (tok == TOKEN_INVALIDE):
        return JSONResponse(content={"message": "Session non valide", "data" : False})
    else:
        return JSONResponse(content={"message": "Error while verifying session", "data" : False})


@userCadeau.post("/generate/{year}")
def rt_generate(year: int, db: Session = Depends(get_db)):
    # reset by deleting previous gift in base
    cadeaux = db.query(UserCadeaux).all()
    for cad in cadeaux:
        delete_userCadeau(db, cad.id)

    # get user list for year
    users = db.query(Users).all()
    liens = db.query(UserLiens).all()

    user_giver = [us.id for us in users]
    user_recei = [us.id for us in users]

    asso = []

    while len(asso) < len(users):
        # select a random user
        giver = user_giver[random.randint(0,len(user_giver) - 1)]
        print("giver : ", giver)
        # extract a suitable list of user to receive from him
        suitable = []
        for pot_recei in user_recei:
            print("verifying potential user : ", pot_recei)
            is_suit = True
            if pot_recei == giver:
                is_suit = False
               
            for lien in liens:
                print("verifying link : ", lien.id, lien.user1id, lien.user2id, lien.typeLien)
                #print(type(lien.user1id))
                #print(type(giver))
                if lien.user1id == giver:
                    print("find matching giver in user1id")
                    if lien.user2id == pot_recei:
                        print("find matching receiver in user2id")
                        is_suit = False
                        
                if lien.user2id == giver:
                    print("find matching giver in user2id")
                    if lien.user1id == pot_recei:
                        print("find matching receiver in user1id")
                        is_suit = False
            if is_suit == True:
                suitable.append(pot_recei)
                print(pot_recei, " can receive")
        print("might gift to : ", suitable)
        if len(suitable) == 0:
            suitable = user_recei
            if(giver in suitable):
                if len(suitable) == 1:
                    raise HTTPException(status_code=404, detail="Une erreur est survenue, veuillez réessayer")
                suitable.pop(suitable.index(giver))
            print("no one suitable, defaulting to : ", suitable)
        # select a random in this list
        recei = suitable[random.randint(0,len(suitable) - 1)]
        print("selected : ", recei)
        # append to asso
        asso.append([giver, recei])
        # remove user from giver list
        user_giver.pop(user_giver.index(giver))
        # remove receiver from receiver list
        user_recei.pop(user_recei.index(recei))

    # save to db
    for ass in asso:
        create_userCadeau(db, dict(UserCadeauCreate(user1id = ass[0], user2id = ass[1], annee = 2023)))

    print(asso)
    print(user_giver)
    print(user_recei)
    print(year)
    return None