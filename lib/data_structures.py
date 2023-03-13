spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [name.get("name", "Spicy food not found") for name in spicy_foods]

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [heat for heat in spicy_foods if heat.get("heat_level") > 5 ]
    return spiciest_foods
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')


    # `Buffalo Wings (American) | Heat Level: 🌶🌶🌶`

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [heat for heat in spicy_foods if heat.get("heat_level") > 5 ]
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)



def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods



# ### `print_spiciest_foods()`

# Define a function `print_spiciest_foods()` that takes a list of `spicy_foods`
# and **outputs to the terminal** ONLY the spicy foods that have a heat level
# greater than 5, in the following format:

# `Buffalo Wings (American) | Heat Level: 🌶🌶🌶`.

# Try to use functions you've already written to solve this!

# ```py
# print_spiciest_foods(spicy_foods)
# # => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# # => Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
# ```

# ### `get_average_heat_level()`

# Define a function `average_heat_level()` that takes a list of `spicy_foods` and
# **returns an integer** representing the average heat level of all the spicy
# foods in the array. Recall that to derive the average of a collection, you need
# to calculate the total and divide number of elements in the collection.

# ```py
# average_heat_level(spicy_foods)
# # => 6
# ```

# ### `create_spicy_food()`

# Define a function `create_spicy_food()` that takes a list of `spicy_foods` and a
# new `spicy_food` and returns the original list with the new `spicy_food` added.

# Example:

# ```py
# create_spicy_food(
#     spicy_foods,
#     {
#         'name': 'Griot',
#         'cuisine': 'Haitian',
#         'heat_level': 10,
#     }
# )

# # => [
# # =>     {
# # =>         "name": "Green Curry",
# # =>         "cuisine": "Thai",
# # =>         "heat_level": 9,
# # =>     },
# # =>     {
# # =>         "name": "Buffalo Wings",
# # =>         "cuisine": "American",
# # =>         "heat_level": 3,
# # =>     },
# # =>     {
# # =>         "name": "Mapo Tofu",
# # =>         "cuisine": "Sichuan",
# # =>         "heat_level": 6,
# # =>     },
# # =>     {
# # =>         'name': 'Griot',
# # =>         'cuisine': 'Haitian',
# # =>         'heat_level': 10,
# # =>     },
# # => ]
