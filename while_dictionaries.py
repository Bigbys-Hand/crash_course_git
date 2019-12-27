unconfirmed_users = ['billy bob', 'tilda', 'judy', 'james c.', 'scarlett', 'james s.', 'katherine h.', 'roger', 'roger', 'roger']
confirmed_users = []

while 'roger' in unconfirmed_users:
    unconfirmed_users.remove('roger')
#pulling out roger, he is clearly spamming the signup page

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
#confirming everyone row by row

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    