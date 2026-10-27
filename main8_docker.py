from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users" , tags = ["Пользователи"], summary = "Получить пользователей")
async def get_users():
    return [{"id": 1, "name": "Artem"}]

if __name__ == "__main__":
    uvicorn.run("main8_docker:app", host = "0.0.0.0")