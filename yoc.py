def get_valid_input(prompt, type_func=int, valid_check=lambda x: x > 0):
    """ Get valid input from the user. """
    while True:
        try:
            value = type_func(input(prompt))
            if valid_check(value):
                return value
            else:
                print("Invalid input, please enter a positive number.")
        except ValueError:
            print("Invalid input, please enter a number.")

def get_structure_data(num_structures):
    """ Get data for each structure. """
    structures = []
    for _ in range(num_structures):
        name = input("Structure Name: ").strip()
        production_income = get_valid_input("Production Income: ", int)
        cost = get_valid_input("Cost: ", int, lambda x: x > 0)

        yield_on_cost = production_income / cost
        structures.append((name, yield_on_cost))
    return structures

def find_optimal_structures(structures):
    """ Find the structure(s) with the highest yield on cost. """
    highest_yield = 0
    optimal_structures = []

    for name, yield_on_cost in structures:
        if yield_on_cost > highest_yield:
            highest_yield = yield_on_cost
            optimal_structures = [name]
        elif yield_on_cost == highest_yield:
            optimal_structures.append(name)

    return optimal_structures, highest_yield

# Main program execution
num_structures = get_valid_input("How many structures are being compared?: ", int, lambda x: x >= 1)
structure_list = get_structure_data(num_structures)
optimal_structures, highest_yield = find_optimal_structures(structure_list)

if optimal_structures:
    formatted_yield = "{:.4f}".format(highest_yield)
    optimal_structures_str = ", ".join(optimal_structures)
    print(f"The optimal structure(s) is/are {optimal_structures_str} with a yield on cost of {formatted_yield}.")
else:
    print("No valid structures were entered.")
