from typing import Union

from fastapi import FastAPI
from routes.index import user, userCadeau, userLien
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()


app.include_router(user)
app.include_router(userLien)
app.include_router(userCadeau)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/register/")
def get_register_page():
    return FileResponse("static/account_creation.html")

@app.get("/login/")
def get_login_page():
    return FileResponse("static/account_login.html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://magimathicart.hirofine.fr", "https://be.magimathicart.hirofine.fr"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)