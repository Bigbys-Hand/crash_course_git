guest_list = ['Abraham Lincoln', 'Buddhadama', 'Angela Merkel', 'Elizabeth Warren']
print(guest_list)

Abe_invitation = f"Mr. {guest_list[0]}, would you please join me for dinner?"
BD_invitation = f"Mr. {guest_list[1]}, would you please join me for dinner?"
AM_invitation = f"Mrs. {guest_list[2]}, would you please join me for dinner?"
EW_invitation = f"Mr. {guest_list[3]}, would you please join me for dinner?"
print(Abe_invitation)
print(BD_invitation)
print(AM_invitation)
print(EW_invitation)

# Buddhadama has to cancel, he said dinner is a mental construct. Shakyabuddha can make it.
BD_cancel = guest_list.pop(1)
print(f"Sadly, {BD_cancel} is unable to attend, as dinner is a mental construct.")
guest_list.insert(1, 'Shakyabuddha')
SD_invitation = f"Mr. {guest_list[1]}, would you please join me for dinner?"
print(SD_invitation)
print(guest_list)

print("Woot, we found a bigger table!")
guest_list.insert(0, 'Jackie Kennedy')
guest_list.insert(2, 'Winston Churchill')
guest_list.append('Robert Oppenheimer')
print(guest_list)
JK_invitation = f"Mrs. {guest_list[0]}, would you please join me for dinner?"
Abe_invitation = f"Mr. {guest_list[1]}, would you please join me for dinner?"
WC_invitation = f"Mr. {guest_list[2]}, would you please join me for dinner?"
SB_invitation = f"Mr. {guest_list[3]}, would you please join me for dinner?"
AM_invitation = f"Mrs. {guest_list[4]}, would you please join me for dinner?"
EW_invitation = f"Mrs. {guest_list[5]}, would you please join me for dinner?"
RO_invitation = f"Mr. {guest_list[-1]}, would you please join me for dinner?"
print(JK_invitation, Abe_invitation, WC_invitation, SB_invitation, AM_invitation, EW_invitation, RO_invitation, sep='\n')

print("Whoops, the table was an illusion and so are most of my guests. Only room for three!")
JK_drop = guest_list.pop(0)
print(f"Sorry {JK_drop}, no trout for you")
print(guest_list)
WC_drop = guest_list.pop(1)
print(f"Sorry {WC_drop}, no trout for you")
print(guest_list)
SB_drop = guest_list.pop(1)
print(f"Sorry {SB_drop}, no mental constructs for you")
print(guest_list)
RO_drop = guest_list.pop(-1)
print(f"Sorry {RO_drop}, no trout for you")
print(guest_list)
print(f"Good news {guest_list[0]}, {guest_list[1]}, and {guest_list[2]}! You're still on the list.")
