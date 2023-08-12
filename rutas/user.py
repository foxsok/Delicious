from bson import ObjectId
from fastapi import APIRouter, status,Response
from bson import ObjectId
# from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

from modelos.user import cafes
from config.db import conn
from esquemas.user import CafesEntity, CafeEntity

Cafes = APIRouter()


@Cafes.get('/Cafes', response_model=list[cafes], tags=["Cafes"])
async def find_all_Cafes():
    # print(list(conn.CRUDF.Leyendas.find()))
    return CafeEntity(conn.CRUDF.Cafes.find())


@Cafes.post('/Cafes', response_model=cafes, tags=["Cafes"])
async def create_cafes(Cafes: cafes):
    new_user = dict(Cafes)
    del new_user["id"]
    id = conn.CRUDF.Cafes.insert_one(new_user).inserted_id
    cafes = conn.CRUDF.Cafes.find_one({"_id": id})
    return CafesEntity(cafes)


@Cafes.get('/cafes/{id}', response_model=cafes, tags=["Cafes"])
async def find_cafes(id: str):
    return CafesEntity(conn.CRUDF.Cafes.find_one({"_id": ObjectId(id)}))


@Cafes.put("/cafes/{id}", response_model=cafes, tags=["Cafes"])
async def update_cafes(id: str, Cafes: cafes):
    conn.CRUDF.Cafes.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(Cafes)
    })
    return CafesEntity(conn.CRUDF.Cafes.find_one({"_id": ObjectId(id)}))


@Cafes.delete("/cafes/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Cafes"])
async def delete_Campeones(id: str):
    conn.CRUDF.Cafes.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)