from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class TvMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    director = db.Column(db.String(50))
    date_added = db.Column(db.DateTime, index=True)
    raiting = db.Column(db.String(20))
    type = db.Column(db.String(20))
    duration = db.Column(db.String(30))
    description = db.Column(db.String(200))
    show_id = db.Column(db.Integer, unique=True)
    release_year = db.Column(db.String(50))
    channels = db.relationship('Channel', secondary='movie_channel', back_populates='tv_movies')
    actors = db.relationship('Actor', secondary='movie_actor', back_populates='tv_movies')
    directors = db.relationship('Director', secondary='movie_director', back_populates='tv_movies')
    countries = db.relationship('Country', secondary='movie_country', back_populates='tv_movies')

 
class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    tv_movies = db.relationship('TvMovie', secondary='movie_channel', back_populates='channels')
 
 
class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    tv_movies = db.relationship('TvMovie', secondary='movie_director', back_populates='directors')


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    tv_movies = db.relationship('TvMovie', secondary='movie_actor', back_populates='actors')


class MovieChannel(db.Model):
    __tablename__ = 'movie_channel'
    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column('channel_id', db.Integer, db.ForeignKey('channel.id'))
    tv_movie_id = db.Column('tv_movie_id', db.Integer, db.ForeignKey('tv_movie.id'))


class MovieActor(db.Model):
    __tablename__ = 'movie_actor'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'))
    tv_movie_id = db.Column('tv_movie_id', db.Integer, db.ForeignKey('tv_movie.id'))


class MovieDirector(db.Model):
    __tablename__ = 'movie_director'
    id = db.Column(db.Integer, primary_key=True)
    director_id = db.Column('director_id', db.Integer, db.ForeignKey('director.id'))
    tv_movie_id = db.Column('tv_movie_id', db.Integer, db.ForeignKey('tv_movie.id'))


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    tv_movies = db.relationship('TvMovie', secondary='movie_country', back_populates='countries')


class MovieCountry(db.Model):
    __tablename__ = 'movie_country'
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column('country_id', db.Integer, db.ForeignKey('country.id'))
    tv_movie_id = db.Column('tv_movie_id', db.Integer, db.ForeignKey('tv_movie.id'))

