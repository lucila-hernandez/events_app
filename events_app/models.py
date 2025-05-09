"""Create database models to represent tables."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy import Enum
from events_app import db  # Import db from __init__.py

# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(80))
    events = db.relationship('Event', secondary='guest_event_table', back_populates='guests')  # Relationship named 'events'

    def __repr__(self):
        return f'<Guest {self.name}>'

# TODO: Create a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    guests = db.relationship('Guest', secondary='guest_event_table', back_populates='events')    # back_populates should be 'events'

    # STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
    # type of event (Party, Study, Networking, etc)
    # event_type = db.Column(Enum('Party', 'Study', 'Networking', name='event_type'))

    def __repr__(self):
        return f'<Event {self.title}>'

# TODO: Create a table `guest_event_table` with the following columns:
# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)

guest_event_table = db.Table('guest_event_table',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'), primary_key=True)
)