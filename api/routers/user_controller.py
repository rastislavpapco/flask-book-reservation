from datetime import datetime
from flask import Blueprint, request

from database.database import db
from database.models import User

user_router = Blueprint("user_router", __name__, url_prefix="/users")


@user_router.route("/")
def get_all_users():
    users = User.query.all()
    return [user.as_dict() for user in users]


@user_router.route("/<user_id>", methods=["GET", "DELETE"])
def get_or_delete_user(user_id: int):
    user = User.query.get(user_id)

    if not user:
        msg = f"Cannot find user with id={user_id}."
        print(msg)
        return msg, 404

    # DELETE
    if request.method == "DELETE":
        db.session.delete(user)
        db.session.commit()
        return f"User with id={user_id} successfully deleted."

    # GET
    return user.as_dict()


@user_router.route("/create", methods=["POST"])
def create_user():
    try:
        user = User(name=request.json['name'], age=request.json['age'],
                    phone=request.json['phone'], registration_date=datetime.now())
    except KeyError as e:
        msg = f"Cannot create new user: missing field {e}."
        print(msg, flush=True)
        return msg, 400

    db.session.add(user)
    db.session.commit()

    return "User successfully created.", 201
