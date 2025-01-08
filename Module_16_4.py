from fastapi import FastAPI, Path, HTTPException
from typing import  Annotated, List
from pydantic import BaseModel, Field

app = FastAPI()

users_db = []

class User(BaseModel):
    id: int = Field(0, ge=0, le= 10000, description="Номер по порядку")
    username: str = Field(0, min_length=3, max_length = 20, description="Имя пользователя")
    age: int = Field(0, ge=18, le = 120, description="Возраст пользователя")

@app.get("/")
async  def get_all_users() -> List[User]:
    return users_db

@app.post("/user/{username}/{age}")
async def create_user(user: User):
    user.id = len(users_db)
    users_db.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, user: User):
    try:
        for person in users_db:
            if person.id == user_id:
                person.username = user.username
                person.age = user.age
                return  person
    except IndexError:
        raise  HTTPException(status_code=404, detail="Такого пользователя не сущетсвуте")

@app.delete("/users/{user_id}")
async  def delete_user(user_id: int) :
    try:
        users_db.pop(user_id)
        return f"Пользователь номер {user_id} удален"
    except IndexError:
         raise HTTPException(status_code=404, detail="Такое пользователя не существует")
@app.delete("/")
async  def delete_all_users() -> str:
    users_db.clear()
    return "Обнуление"
