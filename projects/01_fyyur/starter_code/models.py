from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'Show'

    # Put after the FK constratraints: onupdate="CASCADE", ondelete="CASCADE" or "SET NULL" for artist_id and venue_id
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    start_time = db.Column(db.DateTime())

    def __repr__(self):
      return f"Show <id: {'%d'}, artist_id: {'%d'}, venue_id: {'%d'}, start_time: {self.start_time}>"% (
        self.id, self.artist_id, self.venue_id)


class Venue(db.Model):
    __tablename__ = 'Venue'

    # implement after the unicityof each row
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
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship(Show, backref='venue', lazy=True)

    def __repr__(self):
      return f"Venue <id: {'%d'}, name: {'%s'}, city: {'%s'}, state: {'%s'}, address: {'%s'}, phone: {'%s'}, image_link: {'%s'}, facebook_link: {'%s'}, genres: {'%s'}, web_link: {'%s'}, seeking_talent: {'%r'}, seeking_description: {'%s'}>"% (
        self.id, self.name, self.city, self.state, self.address, self.phone, self.image_link,
        self.facebook_link, self.genres, self.website_link, self.seeking_talent, self.seeking_description)


class Artist(db.Model):
    __tablename__ = 'Artist'

    # implement after the unicityof each row
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship(Show, backref='artist', lazy=True)

    def __repr__(self):
      return f"Artist <id: {'%d'}, name: {'%s'}, city: {'%s'}, state: {'%s'}, phone: {'%s'}, genres: {'%s'}, image_link: {'%s'}, facebook_link: {'%s'}, web_link: {'%s'}, seeking_talent: {'%r'}, seeking_description: {'%s'}>"% (
        self.id, self.name, self.city, self.state, self.phone, self.genres, self.image_link,
        self.facebook_link, self.website_link, self.seeking_venue, self.seeking_description)

    
