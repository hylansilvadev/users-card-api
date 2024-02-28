from typing import List

import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials, firestore, storage
from firedantic import configure

from api.user import User, UserCreate
from core.Settings import settings

cred = credentials.Certificate(
    'core/db-card-dev-firebase-adminsdk-c91lk-7184239cbb.json'
)


firebase_admin.initialize_app(cred)
app = FastAPI(title=settings.PROJECT_NAME)
db = firestore.client()
bucket = storage.bucket('db-card-dev')
configure(db)


@app.get('/')
def root() -> str:
    return 'Hello World'


@app.get('/users', tags=["User Routes"])
def get_all_users() -> List[User]:
    return User.find()


@app.get('/users/{user_id}', tags=["User Routes"])
def get_user_by_id(user_id: str) -> str:
    user = User.get_by_doc_id(user_id)
    nick = user.name.lower().replace(' ', '')
    image = bucket.blob(nick).public_url
    return image


# to-do: fazer o restante das rotas de Users