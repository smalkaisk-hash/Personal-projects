print('===================')
print('Rock Paper Scissors')
print('===================')
print('')

import random
player = int(input("1✊\n2✋\n3✌️""\nEnter a number: "))
computer = random.randint(1, 3)

if player == 1:
    print('You chose:✊')
elif player == 2:
    print('You chose:✋')
elif player == 3:
    print('You chose:✌️')

if computer == 1:
    print('CPU chose:✊')
elif computer == 2:
    print('CPU chose:✋')
elif computer == 3:
    print('CPU chose:✌️')

if player == 1 and computer == 1:
    print('It\'s a tie!')

elif player == 1 and computer == 2:
    print('Computer won!')

elif player == 1 and computer == 3:
    print('Player won!')

elif player == 2 and computer == 1:
    print('Player won!')

elif player == 2 and computer == 2:
    print('It\'s a tie!')

elif player == 2 and computer == 3:
    print('Computer won!')

elif player == 3 and computer == 1:
    print('Computer won!')

elif player == 3 and computer == 2:
    print('Player won!')

elif player == 3 and computer == 3:
    print('It\'s a tie!')