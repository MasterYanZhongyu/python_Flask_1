from App import db
from Model import User,Role
user_role=Role(name='User')
print(User.query.filter_by(role_id=3).all())