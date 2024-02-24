from .database import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.Date, nullable=False)
    reservations = db.relationship("Reservation", backref="book", cascade="delete, delete-orphan")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    registration_date = db.Column(db.Date)
    reservations = db.relationship("Reservation", backref="user", cascade="delete, delete-orphan")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reservation_date = db.Column(db.Date)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
