from contextlib import asynccontextmanager
import uvicorn

from fastapi import FastAPI

from core.config import settings
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as users_router


# Создание БД
@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def get_message_text():
    """Возвращает текст сообщения"""

    return {"message": "text"}


@app.get("/hello/")
def get_welcome_message(name: str = "World"):
    """Возвращает текст сообщения приветствия"""

    name = name.strip().title()
    return {"message": f"Hello, {name}"}


@app.get("/calc/")
def sum_a_and_b(a: int = 1, b: int = 2):
    """Складывает числа a и b"""

    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    # uvicorn.run("main:app", reload=True)
    uvicorn.run(app)
