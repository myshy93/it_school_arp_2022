import sqlite3
import db
from models import Todo

from fastapi import FastAPI

app = FastAPI()

# db init
db_con = sqlite3.connect("db.sqlite")
db.create_todo_table(db_con)
# -------

@app.get("/", name="Hello World")
def read_root():
    """Get hello world!"""
    return {"Hello": "World"}

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

