current_number = 1
while current_number < 12:
    print(current_number)
    current_number += 1

prompt = "\nI will repeat anything you put here: "
prompt+= "\nIf you want to stop, enter 'quit'. "
message = ""

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        print("That was fun! Goodbye.")
        active = False
    elif message == 'secret command':
        print("Executing Order 67.")
        active = False
    else:
        print(message)
# The 'active' bit is a flag. We can insert one or more flags into a while loop to give it more than 
# one end condition to watch for.

present_number = 0
while present_number < 10:
    present_number += 1
    if present_number % 2 == 0:
        continue
    
    print(present_number)
#sticking an if loop with a modulo in this script lets us exclude the 'print' command under the 'continue' clause
#so that we only print odd numbers. Handy!

    