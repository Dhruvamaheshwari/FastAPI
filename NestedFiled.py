from fastapi import FastAPI
from pydantic import BaseModel , Field , EmailStr

app = FastAPI()

class Address(BaseModel):
    city:str = Field(max_length=50 , min_length=3)
    pincode:int = Field(ge=1 , le=10)


class User(BaseModel):
    name:str
    age:int
    email:EmailStr
    address : Address


@app.post('/create')
def create_user(use:User):
    return {"message":"user is created" , 'user':use}



@app.get('/response' , response_model=User)
def get_all_user():
    return{
        "name":"Dhruva Maheshwari",
        "age":22,
        "password":"1234",
        "admin":True,
        "email":"dhruva@gamil.com",
        "address":{"city" : "delhi" , "pincode":1 , "home_no.":22}
    }