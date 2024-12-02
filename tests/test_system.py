import requests

BASE_URL = "http://localhost:8000"

def test_system():
  task_data = {"title": "System Test Task"}
  response = requests.post(f"{BASE_URL}/tasks", json=task_data)
  assert response.status_code == 200

  response = requests.get(f"{BASE_URL}/tasks")
  assert response.status_code == 200
  tasks = response.json()
  assert len(tasks) > 0

  task_id = tasks[0]["id"]
  response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
  assert response.status_code == 200
