current_users = ['james', 'robert', 'daniel', 'linda', 'maria', 'Lisa']
new_users = ['william', 'Richard', 'Robert', 'mary','linda', 'maria']

current_users_lower = [s.lower() for s in current_users]
#print(current_users_lower)
new_users_lower = [s.lower() for s in new_users]
#print(new_users_lower)

for new_user in new_users_lower:
    if new_user in current_users_lower:
        print(f'\nYou need to enter new username,this username ({new_user}) is taken.')
    else:
        print(f'\n{new_user.title()} is available')