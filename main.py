from fastapi import FastAPI

app = FastAPI()

@app.get('/') # this is the decorator
def home():
    return{"welcome Message : ":"this is the home page"}

@app.get('/about')
def about():
    return{"name : " : "My name is Dhruva Maheshwari"}

@app.get("/health")
def health():
    return{"status": "healthy"}


# GET Method — Read data

student = [
    {"id" : 1 , "name" : "Dhruva Maheshwari" , "age" : 22},
    {"id" : 2 , "name" : "Bhumi Maheshwari" , "age" : 21},
    {"id" : 3 , "name" : "Aastha Gosh" , "age" : 22},
    ]

@app.get('/student')
def get_student():
    return student


@app.get('/student/{student_id}')
def get_one_student(student_id: int):
    return{"your student is " : student_id}

@app.get('/search')
def search_student(age: int):
    return {'age of student is ' : age}