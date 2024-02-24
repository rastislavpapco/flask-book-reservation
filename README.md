# Book reservation system (flask)
This repository contains simple flask app for book reservation (library).
The application uses sqlite database with three tables: books, users, reservations.
Each of the three tables allow following operations:
- GET all entries
- GET entry by id
- POST new entry
- DELETE entry by id

### Installation
Clone repository
- `git clone https://github.com/rastislavpapco/flask-book-reservation.git`

Create python virtual environment and install requirements
- `cd flask-book-reservation`
- `python -m venv venv`
- `source venv/Scripts/activate`
- `pip install -r requirements.txt`

### Usage
Start the application: `./run.sh`

The app will run on `http://127.0.0.1:5000/`

You can easily test the endpoints in Postman
by importing `postman_collection.json`.