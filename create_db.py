from yummly import db
from yummly.models import User, Recipe

db.create_all()

# insert data
# db.session.add(User("admin", "admin", "admin"))
# db.session.add(User("user", "user", "admin2"))
# db.session.add(Recipe("Test recipe", "http://yum.com"))
db.session.commit()

# sanity check!
admin = User.query.filter_by(username='admin').first()
print admin.password

user = User.query.filter_by(username='user').first()
print user.password

recipe = Recipe.query.filter_by().all()
print recipe
