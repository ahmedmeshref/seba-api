from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime

# create a db instance
db = SQLAlchemy()


# setup db for the flask app instance
def setup_db(app):
    db.app = app
    db.init_app(app)
    # db.drop_all()
    db.create_all()
    migrate = Migrate(app, db)


# DB Models

class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey(
        'venues.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    image_link = db.Column(db.String(500), nullable=True)
    avaliable_seats = db.Column(db.Integer, default=capacity)

    # create a relationship between Venue and Show. To get the venue of a show run (show_obj.venue).
    # To get all shows of a venue (venue_obj.shows)
    venues = db.relationship('Venue',
                             backref=db.backref('shows', lazy='select', cascade='all, delete-orphan'))

    # create a relationship between users and Show
    users = db.relationship('User', secondary='reservations', lazy='subquery')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Show <{self.id}, {self.venue_id}, {self.artist_id}, {self.start_time}>'

    def __dir__(self):
        return ['venue_id', 'start_date', 'capacity', 'capacity', 'image_link', 'avaliable_seats']

    def format(self):
        return {
            'id': self.id,
            'venue_id': self.venue_id,
            'start_date': self.start_date,
            'capacity': self.capacity,
            'avaliable_seats': self.avaliable_seats,
        }


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

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'address': self.address,
            'image_link': self.image_link
        }

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

    # relationship between venues and users
    venue = db.relationship('Venue', backref=db.backref(
        'users', lazy='select'))

    # create a relationship between users and Show
    shows = db.relationship('Show', secondary='reservations', lazy='subquery')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

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
    user = db.relationship(User, backref=db.backref(
        "reservations", cascade="all, delete-orphan"))
    product = db.relationship(Show, backref=db.backref(
        "reservations", cascade="all, delete-orphan"))
