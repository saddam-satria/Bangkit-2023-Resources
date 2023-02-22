from fastapi import APIRouter,status,HTTPException
from pydantic import BaseModel

class dataSchema(BaseModel):
    name: str
    age : str

data = [
        {
            "name" : "saddam",
            "age" : 21,
            "id": 1
        },
        {
            "name" : "satria",
            "age" : 22, 
            "id"  :2
        },
        {
            "name" : "ardhi",
            "age" : 23,
            "id" : 3
        }
    ]

testRoute = APIRouter(prefix="/test")

@testRoute.get("/")
def getData():
    
    return {
        "data" : data,
        "message" : "get data by id",
        "status" : "success",
        "errorMessage" : None
    }

@testRoute.get("/{id}")
def getData(id : str):
    dataByID = []

    for x in data:
        if x['id'] == int(id):
            dataByID.append(x) 

    return {
        "data" : dataByID,
        "message" : "get all data",
        "status" : "success",
        "errorMessage" : None
    }


@testRoute.post("/")
def postData(requestData: dataSchema):
    id = data[-1]["id"]
    newData = {
        "id" : id + 1,
        "name" : requestData.name,
        "age" : requestData.age
    }


    data.append(newData)

    return {
        "data" : requestData,
        "message" : "post data",
        "status" : "success",
        "errorMessage" : None
    }

@testRoute.delete("/{id}")
def postData(id: str):
    
    for index, x in enumerate(data) :
        if x['id'] == int(id):
            del data[index]


    return {
        "data" : id,
        "message" : "delete data",
        "status" : "success",
        "errorMessage" : None
    }