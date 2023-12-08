from typing import Union

from fastapi import FastAPI
from routes.index import user, userCadeau, userLien
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()

# Configuration de CORS
origins = ["https://magimathicart.hirofine.fr","https://be.magimathicart.hirofine.fr"] # permettre l'accès à partir de n'importe quelle origine
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

origins = ["*"]
methods = ["*"]
headers = ["*"]


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

@app.get("/reveal/")
def get_login_page():
    return FileResponse("static/reveal.html")

@app.get("/cgu/")
def get_login_page():
    return FileResponse("static/cgu.html")

@app.get("/favicon/")
def get_login_page():
    return FileResponse("static/favicon2.ico")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://magimathicart.hirofine.fr", "https://be.magimathicart.hirofine.fr"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)