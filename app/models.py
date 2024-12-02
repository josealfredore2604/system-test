from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Task(Base):
  __tablename__ = "tasks"
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)

def create_tables():
  Base.metadata.create_all(bind=engine)
