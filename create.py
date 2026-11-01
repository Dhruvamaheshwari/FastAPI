from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


list_student = []

class student_structure(BaseModel):
    name:str
    age:int

@app.post("/student" , status_code=200)
def create_student(student:student_structure):
    list_student.append(student.model_dump())
    return {"message" : "student created",'student':student}
