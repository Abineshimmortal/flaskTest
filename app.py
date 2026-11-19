import sqlite3
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DATABASE"] = Path(app.instance_path) / "todos.sqlite3"


def get_db():
    connection = sqlite3.connect(app.config["DATABASE"])
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    with get_db() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


initialize_database()


@app.route("/")
def home():
    with get_db() as connection:
        todos = connection.execute(
            "SELECT id, title, completed FROM todos ORDER BY completed, id DESC"
        ).fetchall()
    remaining = sum(not todo["completed"] for todo in todos)
    return render_template("index.html", todos=todos, remaining=remaining)


@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title", "").strip()
    if title and len(title) <= 200:
        with get_db() as connection:
            connection.execute("INSERT INTO todos (title) VALUES (?)", (title,))
    return redirect(url_for("home"))


@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    with get_db() as connection:
        connection.execute(
            "UPDATE todos SET completed = NOT completed WHERE id = ?", (todo_id,)
        )
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    with get_db() as connection:
        connection.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
