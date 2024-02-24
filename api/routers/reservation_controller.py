from datetime import datetime
from flask import Blueprint, request

from database.database import db
from database.models import Book, Reservation, User

reservation_router = Blueprint("reservation_router", __name__, url_prefix="/reservations")


@reservation_router.route("/")
def get_all_reservations():
    reservations = Reservation.query.all()
    return [reservation.as_dict() for reservation in reservations]


@reservation_router.route("/<reservation_id>", methods=["GET", "DELETE"])
def get_or_delete_reservation(reservation_id: int):
    reservation = Reservation.query.get(reservation_id)

    if not reservation:
        msg = f"Cannot find reservation with id={reservation_id}."
        print(msg)
        return msg, 404

    # DELETE
    if request.method == "DELETE":
        db.session.delete(reservation)
        db.session.commit()
        return f"Reservation with id={reservation_id} successfully deleted."

    # GET
    return reservation.as_dict()


@reservation_router.route("/create", methods=["POST"])
def create_reservation():
    try:
        book_id = request.json['book_id']
        user_id = request.json['user_id']
    except KeyError as e:
        msg = f"Cannot make reservation: missing field {e}."
        print(msg)
        return msg, 400

    if not Book.query.get(book_id):
        msg = f"Cannot make reservation: book with id={book_id} doesn't exist."
        print(msg)
        return msg, 404

    if Reservation.query.filter_by(book_id=book_id).first():
        msg = f"Cannot make reservation: book with id={book_id} is already reserved."
        print(msg)
        return msg, 400

    if not User.query.get(user_id):
        msg = f"Cannot make reservation: user with id={user_id} doesn't exist."
        print(msg)
        return msg, 404

    reservation = Reservation(book_id=book_id, user_id=user_id, reservation_date=datetime.now())
    db.session.add(reservation)
    db.session.commit()

    return f"Successfully reserved book with id={book_id} for user with id={user_id}", 201
