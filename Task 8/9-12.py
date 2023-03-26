from admin import Admin

# suga is obj of admin class
suga = Admin('suga', 'works', 'S_works', 'SugaisBomb@example.com', 'antonito')
suga.describe_user()
# making privileges
suga_privileges = ['can play with users', 'permission to suspend accounts', 'changing password']

suga.privileges.privileges = suga_privileges
suga.privileges.show_priv()