from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from contextlib import asynccontextmanager

from app.db.engine import engine, Base


from app.todo_list.routes import todo


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(todo.router, tags=["Todo"])


@app.get("/", include_in_schema=False)
def redirect_root():
    return RedirectResponse("/docs")
