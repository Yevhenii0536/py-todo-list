from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    project_name: str = "Todo list"
    db_url: str = os.getenv("DB_URL", "sqlite+aiosqlite:///./todo.db")

settings = Settings()
