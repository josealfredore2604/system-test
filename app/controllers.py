from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from .models import SessionLocal
from .services import create_task, get_tasks, delete_task
from .models import create_tables

app = FastAPI()

create_tables()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/tasks")
async def create_task_endpoint(request: Request, db: Session = Depends(get_db)):
  body = await request.json()
  title = body.get("title")

  if not title:
    raise HTTPException(status_code=400, detail="Title is required")

  return create_task(db, title)

@app.get("/tasks")
def get_tasks_endpoint(db: Session = Depends(get_db)):
  return get_tasks(db)

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
  task = delete_task(db, task_id)
  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  return {"message": "Task deleted"}

