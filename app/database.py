from pymongo.mongo_client import MongoClient

from app.core.config import settings

uri = settings.DATABASE_URI

client = MongoClient(uri)

db = client.db_members_iv

collection_name = db['members']
