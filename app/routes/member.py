from typing import List
from fastapi import APIRouter
from app.models import Member
from app.database import collection_name
from app.schemas import list_serial
from bson import ObjectId

route_member = APIRouter(prefix="/member", tags=["Members"])


#   GETs Requests Methods

@route_member.get("/")
def get_mebers() -> List:
    member = list_serial(collection_name.find())
    return member


#   POST Request Method

@route_member.post("/")
def create_new_menber(member: Member):
    collection_name.insert_one(dict(member))


# PUT Request Method

@route_member.put('/{member_id}')
def update_member_by_id(member_id: str, member: Member):
    collection_name.find_one_and_update(
        {"_id": ObjectId(member_id)}, {"$set": dict(member)})


# DELETE Resquest Method

@route_member.delete("/{member_id}")
def delete_member_by_id(meber_id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(meber_id)})
