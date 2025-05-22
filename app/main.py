from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from contextlib import asynccontextmanager

from app.db.engine import engine, Base
from app.todo_list.routes.todo import router as todo_router
from app.todo_list.routes.category import router as category_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(todo_router, tags=["Todo"])
app.include_router(category_router, tags=["Category"])

@app.get("/", include_in_schema=False)
def redirect_root():
    return RedirectResponse("/docs")
