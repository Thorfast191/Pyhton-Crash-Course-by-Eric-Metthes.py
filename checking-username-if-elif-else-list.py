current_users = ['admin', 'arafat', 'anis', 'rohit', 'niloy']
new_users = ['nabil', 'Rohit', 'anis', 'ariful', 'arafat']

for user in new_users:
    if user in current_users:
        print('username already in use')
    else: print('username is available')