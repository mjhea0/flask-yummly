from yummly import db
from yummly.models import User

db.create_all()

# insert data
db.session.add(User("user", "user", "admin2"))
db.session.commit()

# sanity check!
admin = User.query.filter_by(username='admin').first()
print admin.password

user = User.query.filter_by(username='user').first()
print user.password
