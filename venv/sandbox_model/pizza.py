def picky_pizza(size, shape, *toppings):
    ###make a pizza with a certain size, shape, and any combination of toppings###
    print(f"\nMaking a {size}-inch {shape} pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")