from App import db
from Model import User,Role
admin_role=Role(name='Admin')
mod_role=Role(name='Moderator')
user_role=Role(name='User')
# user_john=User(username='john',role=admin_role)
# user_susan = User(username='susan', role=user_role)
# user_david = User(username='david', role=user_role)
# db.session.add_all([admin_role,mod_role,user_role,user_david,user_john,user_susan])


#admin_role.name='Administrator'
#db.session.add(user_zhong)
#db.session.commit()

#admin=Role.query.filter_by(name='Administrator').first()
#user_zhong=User(username='zhong',role=admin)
#admin.name='Administrator'

print(User.query.all())
print(str(User.query.filter_by(role=user_role)))
#db.session.commit()
#print(admin)