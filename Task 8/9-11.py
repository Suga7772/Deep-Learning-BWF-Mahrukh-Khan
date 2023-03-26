from user import Admin
#importing admin class from user python file
# suga is obj of admin class
suga = Admin('suga', 'works', 'S_works', 'SugaisBomb@example.com', 'antonito')
suga.describe_user()
# making privileges
suga_privileges = ['can delete users', 'permission to suspend accounts', 'changing password']

suga.privileges.privileges = suga_privileges
suga.privileges.show_priv()
