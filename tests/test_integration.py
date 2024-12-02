from app.models import engine, SessionLocal

def test_database_connection():
  try:
    connection = engine.connect()
    assert connection.closed == False
  finally:
    connection.close()
