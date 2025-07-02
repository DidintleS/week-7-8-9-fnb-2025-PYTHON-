
#Create a shopping cart that will contain a list of items.
#Have the ability to add items, remove items, and view the cart.
#At the end, display the total cost of the items in the cart.

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item (or 'done' to finish): ")
    if food.lower() == 'q': 
        break
    else:
        price = float(input(f"Enter the price for {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("-----Your Cart -----")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price

print("\n")
print(f"Total: R{total}")