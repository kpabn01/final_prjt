from app import db
from sqlalchemy.dialects.postgresql import JSON

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# I HAVE TO DECLARE THE ASSOCIATION TABLE FIRST TO BE ABLE TO USE THE VARIABLE IN THE OTHER TABLES
shows = db.Table('Show',
    db.Column('Artist_id', db.ForeignKey('Artist.id'), primary_key=True),
    db.Column("Venue_id", db.ForeignKey('Venue.id'), primary_key=True),
    db.Column('start_time', db.DateTime(), nullable=False)
)


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.String(120))
    web_link = db.Column(db.String(120))
    looking_for_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    artists = db.relationship("Artist", secondary=shows, lazy='subquery', backref=db.backref('Venue', lazy=True))

    def __repr__(self):
      return "<Venue(id='%d', name='%s', city='%s', state='%s', address='%s', phone='%s')>" % (
              self.id, self.name, self.city, self.state, self.address, self.phone)


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    web_link = db.Column(db.String(120))
    looking_for_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))


    def __repr__(self):
      return "<Artist(id='%d', name='%s', city='%s', state='%s', phone='%s', genres='%s')>" % (
            self.id, self.name, self.city, self.state, self.phone, self.genres)

    
# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
# PLEASE SEE LINE 10
