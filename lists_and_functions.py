def greet_nerds(names):
    """Prints a simple greeting to each nerd in the list of nerds"""
    for name in names:
        greeting = f"Hello {name.title()}! Live long and prosper!"
        print(greeting)
        
nerds = ['Suzy', 'Mortimer', 'Bromhilda', 'xXx_l337_Mstr_Cheef_xXx']
greet_nerds(nerds)

def print_ships(unprinted_ships, completed_ships):
    """
    Produces ED ships until none are left.
    Moves each produced ship into completed_ships once done for confirmation
    """
    while unprinted_ships:
        current_job = unprinted_ships.pop()
        print(f"Printing ship: {current_job.title()}")
        completed_ships.append(current_job)
        """
        working off of a copy of unprinted_ships via [:] lets us review the original work order later
        """
def show_finished_ships(completed_ships):
    """show all ships that were produced"""
    print("\nThe following ships have been rolled out:")
    for ship in completed_ships:
        print(f"A brand-new {ship.title()}!")

unprinted_ships = ['Adder','Anaconda','Chief',"Fleur d'Etoile",'Python','Vulture']
completed_ships = []

print_ships(unprinted_ships, completed_ships)
show_finished_ships(completed_ships)
#this script is currently spawning endless copies of 'vulture' somewhere...
