# Write code below 💖

height = int(input('Your height (cm): '))

credits = int(input('credits: '))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("You are not tall enough for this ride, nor do you have enough credits.")
