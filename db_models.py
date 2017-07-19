# models.py

import datetime

from pony.orm import Database, Required, select, db_session

db = Database()

db.bind('sqlite', 'db.sqlite')


class Movie(db.Entity):
    title = Required(str)
    year = Required(int)
    genre = Required(str)
    plot = Required(str)
    rating = Required(str)
    date_added = Required(str)


db.generate_mapping(create_tables=False)


@db_session
def add_movie(title, year, genre, plot, rating):
    today = str(datetime.date.today())
    Movie(title=title, year=year, genre=genre,
          plot=plot, rating=rating, date_added=today)


@db_session
def get_all_movies():
    all_movies = select(m for m in Movie)[:]
    return all_movies


@db_session
def get_movies_by_date(date):
    """ (str) -> pony.orm.core.Query object

    Date must be in  format yyyy-mm-dd
    """
    movies_by_date = Movie.select(lambda m: m.date_added == date)
    return movies_by_date
