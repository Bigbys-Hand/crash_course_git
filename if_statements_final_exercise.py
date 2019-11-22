usernames = ['John', 'Mike', 'Dom', 'Kyle', 'Paul', 'admin']
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Greetings, {username.title()}")
        else:
            print("Greetings, user!")
else:
    print("We need to find some users!")

members = ['Francine', 'Robert', 'Gary', 'Bill', 'Maud', 'Loren']
new_members = ['Alberta', 'Francine', 'gary', 'Jerry', 'Larry', 'Loren']
members_lower = [member.lower() for member in members]
for new_member in new_members:
    if new_member.lower() in members_lower:
        print(f"Sorry, {new_member.title()}, you must already have an account. Please reset your password.")
    else:
        print(f"Welcome aboard, {new_member.title()}!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st\n")
    elif number == 2:
        print(f"{number}nd\n")
    elif number == 3:
        print(f"{number}rd\n")
    else:
        print(f"{number}th\n")
