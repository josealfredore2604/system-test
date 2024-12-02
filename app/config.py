import os

DB_NAME = os.getenv("DB_NAME", "test_db")
DB_USER = os.getenv("DB_USER", "dbuser")
DB_PASS = os.getenv("DB_PASS", "dbpass")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
