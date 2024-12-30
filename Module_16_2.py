from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get("/")
async def main_page() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin_login() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_login(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=3)]) -> str:
    return  f"Вы вошли как пользователь N{user_id}"

@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Vlad")],
                    age: Annotated[int,Path(ge=18, le=120, description="Enter age", example="23")]) -> str:
    return  f"Информация о пользователе. Имя {username}, возраст {age}"
