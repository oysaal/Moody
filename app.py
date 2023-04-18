from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL
import sqlite3

def initialize_db():
    connection = sqlite3.connect('main.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    connection.commit()
    connection.close()

app = Flask(__name__)
db = SQL("sqlite:///main.db")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return
