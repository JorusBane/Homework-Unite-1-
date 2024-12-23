from fastapi import FastAPI, Path
from typing import  Annotated

app = FastAPI()

users = {"1": "Имя: Иван, Возраст: 18"}

@app.get("/")
async  def get_all_users() -> dict:
    return users

@app.post("/{username}/{age}")
async def create_user(username: str = Path(min_length=3, max_length=15, description="Введите имя пользователя", example="Иван"),
                      age: int = Path(ge=18, le=120, description="Введите возраст пользователя", example=18) ) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя {username}, возраст {age}"
    return "Пользователь добавлен!"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int = Path(ge=0, le=1000, description="Введите номер в списке", example=3),
                      username: str = Path(min_length=3, max_length=15, description="Введите имя пользователя", example="Иван"),
                      age:  int = Path(ge=18, le=120, description="Введите возраст", example=18)) -> str:
    users[str(user_id)] =  f"Имя {username}, возраст {age}"
    return "Данные о пользователе обновлены!"

@app.delete("/users/{user_id}")
async  def delete_user(user_id: str = Path(ge=0, le=1000, description="Введите номер в списке", example=2)) -> str:
    users.pop(user_id)
    return f"Пользователь {user_id} были удалены."

@app.delete("/")
async  def delete_all_users() -> str:
    users.clear()
    return "Обнуление"
