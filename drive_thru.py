# Write code below 💖

def welcome():
    print("🍔 Cheeseburger")
    print("🍟 Fries")
    print("🥤 Soda")
    print("🍦 Ice Cream")
    print("🍪 Cookie")

welcome()

print()

program = input('Welcome! What would you like to order? ')


def get_item(program):
  foods = {
    "1": "🍔 Cheeseburger",
    "2": "🍟 Fries",
    "3": "🥤 Soda",
    "4": "🍦 Ice Cream",
    "5": "🍪 Cookie"
  }

  if program in foods:
    return foods[program]
  else:
    return ("sorry this is not one the menu")

result = get_item(program)

print(result)
