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