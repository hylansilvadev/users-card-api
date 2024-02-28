from typing import List, Optional

import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials, firestore
from firedantic import Model
from pydantic import BaseModel

from core.Settings import settings

cred = credentials.Certificate(
    'core/db-card-dev-firebase-adminsdk-c91lk-7184239cbb.json'
)

firebase_admin.initialize_app(cred)

app = FastAPI(title=settings.PROJECT_NAME)

db = firestore.client()


class User(BaseModel):
    name: str
    tags: List
    linkedin: Optional[str] = None
    instagram: Optional[str] = None
    github: Optional[str] = None


class Users(Model):
    __collection__ = 'users'
    users: List[User]


@app.get('/')
def root() -> str:
    return 'Hello World'


@app.get('/users')
def get_users():
    users = db.collection('users').get()
    data = [user.to_dict() for user in users]
    return data