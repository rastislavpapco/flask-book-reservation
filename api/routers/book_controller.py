from datetime import datetime
from flask import Blueprint, request

from database.database import db
from database.models import Book

book_router = Blueprint("book_router", __name__, url_prefix="/books")


@book_router.route("/")
def get_all_books():
    books = Book.query.all()
    return [book.as_dict() for book in books]


@book_router.route("/<book_id>", methods=["GET", "DELETE"])
def get_or_delete_book(book_id: int):
    book = Book.query.get(book_id)

    if not book:
        msg = f"Cannot find book with id={book_id}."
        print(msg)
        return msg, 404

    # DELETE
    if request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return f"Book with id={book_id} successfully deleted."

    # GET
    return book.as_dict()


@book_router.route("/create", methods=["POST"])
def create_book():
    try:
        book = Book(title=request.json['title'], author=request.json['author'], genre=request.json['genre'],
                    pages=request.json['pages'], creation_date=datetime.now())
    except KeyError as e:
        msg = f"Cannot create new book: missing field {e}."
        print(msg, flush=True)
        return msg, 400

    db.session.add(book)
    db.session.commit()

    return "Book successfully created.", 201
