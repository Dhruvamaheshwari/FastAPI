from fastapi import FastAPI

app = FastAPI()

@app.get('/') # this is the decorator
def home():
    return{"welcome Message : ":"this is the home page"}




    