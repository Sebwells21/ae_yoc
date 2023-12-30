def get_valid_input(prompt, type_func=int, valid_check=lambda x: x > 0):
    while True:
        try:
            value = type_func(input(prompt))
            if valid_check(value):
                return value
        except ValueError:
            pass
        print("Invalid input, please enter a valid number.")

def get_structure_data(num_structures):
    for _ in range(num_structures):
        name = input("Structure Name: ").strip()
        production_income = get_valid_input("Production Income: ")
        cost = get_valid_input("Cost: ", valid_check=lambda x: x > 0)
        yield_on_cost = production_income / cost
        yield name, yield_on_cost

def find_optimal_structures(structures):
    highest_yield = 0
    optimal_structures = []
    for name, yield_on_cost in structures:
        if yield_on_cost > highest_yield:
            highest_yield = yield_on_cost
            optimal_structures = [name]
        elif yield_on_cost == highest_yield:
            optimal_structures.append(name)
    return optimal_structures, highest_yield

num_structures = get_valid_input("How many structures are being compared?: ", valid_check=lambda x: x >= 1)
optimal_structures, highest_yield = find_optimal_structures(get_structure_data(num_structures))
if optimal_structures:
    formatted_yield = "{:.4f}".format(highest_yield)
    optimal_structures_str = ", ".join(optimal_structures)
    print(f"The optimal structure(s) is/are {optimal_structures_str} with a yield on cost of {formatted_yield}.")
else:
    print("No valid structures were entered.")
