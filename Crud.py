from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_list = []

class user_class(BaseModel):
    id:int | None = None
    name:str | None = None
    age:int | None = None


# Return all user
@app.get('/all_user')
def get_all_user():
    return{'all_user' : user_list}

# Return one user
@app.get('/user/{id}')
def get_one_user(id : int):
    if(id > 0 or id <= len(user_list)):
        return user_list[id]
    else:
        return{"message":'user is not found'}

# Create student
@app.post('/creat_user')
def creat_user(user:user_class):
    user_list.append(user.model_dump())
    return{"message":"user is created" , "user":user}

# Replace user details
@app.put('/update/{id}')
def update_user(id:int , user:user_class):
    for exist_user in user_list:
        if(exist_user["id"] == id):
            exist_user.update(user.model_dump())
            return {"message":"user is updated" , 'user':exist_user}

    return {"message" : "user not found"}

    

# Update selected fields
@app.patch('/user/{id}')
def update_oneField(id:int , user:user_class):
    for exist_user in user_list:
        if(exist_user["id"] == id):
            exist_user.update(user.model_dump(exclude_unset=True))
            return {"message":"user is updated" , 'user':exist_user}

    return {"message" : "user not found"}


# Delete user
@app.delete('/user_delete/{id}')
def user_delete(id:int):
    for exist_user in user_list:
        if(exist_user["id"] == id):
            user_list.remove(exist_user)
            return {"message":"user is deleted from list" , 'user':user_list}

    return {"message" : "user not found"}