def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Invalid input, please enter a valid number.")

def get_structure_data(num_structures):
    for _ in range(num_structures):
        name = input("Structure Name: ").strip()
        production_income = get_valid_input("Production Income: ")
        cost = get_valid_input("Cost: ")
        yield name, production_income, cost

def find_optimal_structures(structures):
    highest_yield = 0
    optimal_structures_str = ""
    for name, production_income, cost in structures:
        yield_on_cost = production_income / cost
        if yield_on_cost > highest_yield:
            highest_yield = yield_on_cost
            optimal_structures_str = name
        elif yield_on_cost == highest_yield:
            optimal_structures_str += ", " + name
    return optimal_structures_str, highest_yield

num_structures = get_valid_input("How many structures are being compared?: ")
optimal_structures_str, highest_yield = find_optimal_structures(get_structure_data(num_structures))
if optimal_structures_str:
    formatted_yield = "{:.4f}".format(highest_yield)
    print(f"The optimal structure(s) is/are {optimal_structures_str} with a yield on cost of {formatted_yield}.")
else:
    print("No valid structures were entered.")
