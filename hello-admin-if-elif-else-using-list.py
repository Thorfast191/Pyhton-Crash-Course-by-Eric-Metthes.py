usernames = ['admin', 'arafat', 'anis', 'rohit', 'niloy', 'nabil']

#using a for loop to print
for username in usernames:
    if username == 'admin':
        print('hello ' + f'{username}' + ',' + ' would you like to see the report?')
    else :
        print('Greetings ' + f'{username}')
