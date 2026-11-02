
from fastapi import FastAPI
from pydantic import BaseModel , Field , EmailStr

app = FastAPI()

class student(BaseModel):
    name: str = Field(max_length=10 , min_length=3)
    age:int = Field(ge=18 , le=80)
    email:EmailStr


@app.post('/create')
def create_student(std:student):
    return{"message":"student is created" , "student":std}