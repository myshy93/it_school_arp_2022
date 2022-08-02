import sqlite3
import db
from models import Todo

from fastapi import FastAPI, Response, status

app = FastAPI()

# db init
db_con = sqlite3.connect("db.sqlite")
db.create_todo_table(db_con)
# -------

@app.post("/todo", name="Create TODO")
def create_todo(todo: Todo):
    """Create new TODO."""
    db_con = sqlite3.connect("db.sqlite")
    db.create_todo(db_con, todo.title, todo.body)
    db_con.close()
    return {"status": "TODO created"}

@app.get("/todos")
def get_todos():
    db_con = sqlite3.connect("db.sqlite")
    r = db.read_todos(db_con)
    r = list(r)
    db_con.close()
    return r


@app.get("/todos/{id}")
def get_todos(id):
    db_con = sqlite3.connect("db.sqlite")
    r = db.read_todo(db_con, id)
    r = list(r)
    db_con.close()
    if len(r) == 0:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return r