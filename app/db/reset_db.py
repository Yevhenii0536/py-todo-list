import os
import subprocess

from pathlib import Path
from app.settings import settings


ALEMBIC_DIR = Path("migrations")
# DB_PATH = settings.db_url
DB_PATH = "D:/Education/Python/Self/todo_list/db.sqlite3"


def reset_db():
    db_file = Path(DB_PATH)

    if db_file.exists():
        db_file.unlink()
        print(f"🗑️ Deleted SQLite database at {DB_PATH}")
    else:
        print(f"ℹ️ No SQLite database found at {DB_PATH}")

    db_file.parent.mkdir(parents=True, exist_ok=True)

    db_file.touch()
    print(f"📁 Created empty SQLite database at {DB_PATH}")
    

def clear_migrations():
    versions_path = Path(ALEMBIC_DIR)

    if versions_path.exists():
        for file in versions_path.iterdir():
            if file.is_file():
                file.unlink()

        print("🧹 Cleared existing Alembic migration files.")
    else:
        print("ℹ️ No Alembic 'versions' folder found. Creating...")
        versions_path.mkdir(parents=True, exist_ok=True)
                


def run_alembic():
    print("⚙️ Generating new Alembic migration...")
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", "initial"], check=True)

    print("⬆️  Upgrading database to latest migration...")
    subprocess.run(["alembic", "upgrade", "head"], check=True)


if __name__ == "__main__":
    reset_db()
    clear_migrations()
    run_alembic()