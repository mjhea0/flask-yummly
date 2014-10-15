from yummly import db
from yummly.models import User

db.create_all()

# insert data
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.commit()

<<<<<<< HEAD
# sql.py - Create a SQLite3 table and populate it with data


# import sqlite3

# create a new database if the database doesn't already exist
# with sqlite3.connect('sample.db') as connection:

#     # get a cursor object used to execute SQL commands
#     c = connection.cursor()

#     # create the table
#     c.execute('CREATE TABLE User(username TEXT, email TEXT, password TEXT)')

    # insert dummy data into the table
    # c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')



# db.create_all()
# db.session.add(User("admin", "ad@min.com", "admin"))
# db.session.commit()




admin = User.query.filter(User.username=='test').first()
print admin.email
=======
# sanity check!
admin = User.query.filter_by(username='admin').first()
print admin.username
>>>>>>> 9e32403591504d8ef167b12515423903392c74a7
