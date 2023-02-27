import flask
from books import Book
import json

app = flask.Flask(__name__)

library = [
    Book("The Gunslinger", "Stephen King", "Fantasy", 1),
    Book("The Canterbury Tales", "Geoffrey Chaucer", "Anthology", 2),
    Book("20,000 Leagues Under the Sea", "Jules Verne", "Science Fiction", 3),
    Book("Red Dragon", "Thomas Harris", "Crime Fiction", 4),
    Book("Prometheus Bound", "Aeschylus", "Tragedy", 5)
    ]


@app.route("/")
def homePage():
    page = "<!DOCTYPE html><html><head><title>The Little Library</title></head>"
    page += "<body><h1>The Little Library</h1></body>"
    return page


@app.route("/items")
def itemspage():
    items = {}
    for l in library:
        yield json.dumps({"title": l.title, "author": l.author, "genre": l.genre, "pub": l.pub}) + "\n"



@app.route("/find/by-title/<title>")
def particular(title):
    print(title)
    for l in library:
        if l.author == title:
            yield json.dumps({"title": l.title, "author": l.author, "genre": l.genre, "pub": l.pub}) + "\n"