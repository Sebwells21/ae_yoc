""" INITIAL THOUGHTS:
Compare different production structures to
find the optimal next step forward. yield_on_cost = production / cost
key-value pair is {name:yield_on_cost}
"""

structures = []

#Prompts the user and creates the list of dicts
x = int(input("How many structures are being compared?: "))
for _ in range(x):
    name = input("Structure Name: ")
    production_income = int(input("Production Income: "))
    cost = int(input("Cost: "))

    yield_on_cost = production_income / cost
    dict = {name: yield_on_cost}
    structures.append(dict)


optimal_structure = None
highest_yield = 0

#Iterates through the list of dicts and finds the optimal structure
for structure in structures:
    for name, yield_on_cost in structure.items():
        if yield_on_cost > highest_yield:
            highest_yield = yield_on_cost
            optimal_structure = name


print(f"The optimal structure is the {optimal_structure} with a yield on cost of {highest_yield}.")
