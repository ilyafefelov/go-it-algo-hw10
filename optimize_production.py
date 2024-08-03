from pulp import LpMaximize, LpProblem, LpVariable
"""
This script optimizes the production of lemonade and fruit juice based on certain constraints.
The script uses the PuLP library to create a linear programming model and solve it to find the optimal production quantities.
The variables used in the model are:
- `lemonade`: Represents the quantity of lemonade to be produced.
- `fruit_juice`: Represents the quantity of fruit juice to be produced.
The constraints applied to the model are:
- `water_limit`: The total amount of water used in the production of lemonade and fruit juice should not exceed 100 units.
- `sugar_limit`: The amount of sugar used in the production of lemonade should not exceed 50 units.
- `lemon_juice_limit`: The amount of lemon juice used in the production of lemonade should not exceed 30 units.
- `fruit_puree_limit`: The amount of fruit puree used in the production of fruit juice should not exceed 40 units.
The objective function of the model is to maximize the total quantity of products, which is the sum of lemonade and fruit juice.
After solving the model, the script prints the optimal quantities of lemonade, fruit juice, and the total quantity of products.
Note: This script assumes that the PuLP library is installed.
"""

# Створення моделі
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Обмеження
model += (2 * lemonade + 1 * fruit_juice <= 100, "water_limit")
model += (1 * lemonade <= 50, "sugar_limit")
model += (1 * lemonade <= 30, "lemon_juice_limit")
model += (2 * fruit_juice <= 40, "fruit_puree_limit")

# Функція цілі
model += lemonade + fruit_juice, "total_products"

# Розв'язання задачі
status = model.solve()

# Виведення результатів
print(f"Lemonade: {lemonade.value()}")
print(f"Fruit Juice: {fruit_juice.value()}")
print(f"Total Products: {lemonade.value() + fruit_juice.value()}")
