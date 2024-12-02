from app.services import create_task, get_tasks, delete_task
from app.models import Task, SessionLocal

def test_create_task():
  db = SessionLocal()
  task = create_task(db, "Test Task")
  assert task.title == "Test Task"
  db.close()

def test_get_tasks():
  db = SessionLocal()
  tasks = get_tasks(db)
  assert isinstance(tasks, list)
  db.close()

def test_delete_task():
  db = SessionLocal()
  task = create_task(db, "Task to Delete")
  deleted_task = delete_task(db, task.id)
  assert deleted_task is not None
  db.close()
