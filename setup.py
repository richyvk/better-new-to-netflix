# setup.py

import pickle

from pony.orm import Database, Required


# Pickle empty string used to save last scraped article title
last_scraped_title = ""

with open('last_scraped_title.p', 'wb') as f:
    pickle.dump(last_scraped_title, f)


# Create the database
db = Database()


class Movie(db.Entity):
    title = Required(str)
    year = Required(int)
    genre = Required(str)
    plot = Required(str)
    rating = Required(str)
    date_added = Required(str)


db.bind('sqlite', 'db.sqlite', create_db=True)

db.generate_mapping(create_tables=True)

print('database created')
