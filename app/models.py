from app import db
from datetime import datetime


# DB Models

class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey(
        'venues.id'), nullable=False)
    # artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    image_link = db.Column(db.String(500), nullable=True)
    avaliable_seats = db.Column(db.Integer, default=capacity)
    # create a relationship between Venue and Show. To get the venue of a show run (show_obj.venue).
    # To get all shows of a venue (venue_obj.shows)
    venue = db.relationship('Venue',
                            backref=db.backref('shows', lazy='select', cascade='all, delete-orphan'))
    # create a relationship between users and Show
    users = db.relationship(
        'User', secondary='reservations', lazy='subquery', backref=db.backref('pages', lazy=True))

    def __repr__(self):
        return f'Show <{self.id}, {self.venue_id}, {self.artist_id}, {self.start_time}>'

    def __dir__(self):
        return ['venue_id', 'start_date', 'capacity', 'avaliable_seats']


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # relationship between venues and users
    user = db.relationship('Venue', backref=db.backref(
        'users', lazy='select', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'Venue <{self.id}, {self.name}, {self.city}>'

    def __dir__(self):
        return ['name', 'city', 'address', 'image_link', 'facebook_link',
                'website', 'user_id']


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)

    # create a relationship between users and Show
    shows = db.relationship(
        'Show', secondary='reservations', lazy='subquery', backref=db.backref('pages', lazy=True))


    def __repr__(self):
        return f'Artist <{self.id}, {self.name}, {self.email}>'

    def __dir__(self):
        return ['name', 'email', 'address', 'phone']


class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    dateTime = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'))

    # many to many relationships 
    user = db.relationship(User, backref=db.backref("reservations", cascade="all, delete-orphan"))
    product = db.relationship(Show, backref=db.backref("reservations", cascade="all, delete-orphan"))