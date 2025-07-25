# Concession stand program
# dictionary {key:value}

menu = {"popcorn": 5.00,
        "nachos": 3.50,
        "pizza": 4.90,
        "coke": 2.10,
        "pretzel": 4.50,
        "chips": 1.10,
        "fries": 2.50}
cart = []
total = 0

print("-------- MENU --------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----------- YOUR ORDER -----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")