from datetime import datetime
from flask import Flask


from api.routers.book_controller import book_router
from api.routers.reservation_controller import reservation_router
from api.routers.user_controller import user_router
from database.database import db
from database.models import Book, User


app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    book1 = Book(title="Book 1", author="Author 1", genre="Comedy", pages=40, creation_date=datetime(2020, 5, 10, 15, 0, 0))
    book2 = Book(title="Book 2", author="Author 2", genre="Drama", pages=60, creation_date=datetime(2021, 6, 15, 18, 10, 0))
    book3 = Book(title="Book 3", author="Author 3", genre="Fantasy", pages=80, creation_date=datetime(2022, 8, 18, 20, 30, 0))

    user1 = User(name="John", age=18, phone="554 877 444", registration_date=datetime(2024, 2, 1, 16, 32, 44))
    user2 = User(name="Steve", age=33, phone="540 899 665", registration_date=datetime(2024, 2, 12, 10, 2, 25))

    db.session.add_all([book1, book2, book3, user1, user2])
    db.session.commit()

# Attach routers
app.register_blueprint(book_router)
app.register_blueprint(reservation_router)
app.register_blueprint(user_router)


if __name__ == "__main__":
    app.run()
