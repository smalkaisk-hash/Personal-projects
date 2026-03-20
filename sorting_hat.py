Gryffindor_score = 0
Hufflepuff_score = 0
Ravenclaw_score = 0
Slytherin_score = 0

Q1 = int(input('Do you like Dawn or Dusk? '))

if Q1 == 1:
    print('Dawn')
    Gryffindor_score = Gryffindor_score + 1
    Ravenclaw_score = Ravenclaw_score + 1

elif Q1 == 2:
    print('Dusk')
    Hufflepuff_score = Hufflepuff_score + 1
    Slytherin_score = Slytherin_score + 1

else: print('Wrong input')

Q2 = int(input('When Im dead, I want people to remember me as: '))

if Q2 == 1:
    print('The Good')
    Hufflepuff_score = Hufflepuff_score + 2

elif Q2 == 2:
    print('The Great')
    Slytherin_score = Slytherin_score + 2

elif Q2 == 3:
    print('The Wise')
    Ravenclaw_score = Ravenclaw_score + 2

elif Q2 == 4:
    print('The Bold')
    Gryffindor_score = Gryffindor_score + 2

else: print('Wrong input')

Q3 = int(input('Which kind of instrument most pleases my ear? '))

if Q3 == 1:
    print('The violin')
    Slytherin_score = Slytherin_score + 4
elif Q3 == 2:
    print('The trumpet')
    Hufflepuff_score = Hufflepuff_score + 4

elif Q3 == 3:
    print('The piano')
    Ravenclaw_score = Ravenclaw_score + 4

elif Q3 == 4:
    print('The drums')
    Gryffindor_score = Gryffindor_score + 4
else: print('Wrong input')

print('Gryffindor score: ' + str(Gryffindor_score))
print('Hufflepuff score: ' + str(Hufflepuff_score))
print('Ravenclaw score: ' + str(Ravenclaw_score))
print('Slytherin score: ' + str(Slytherin_score))

if Gryffindor_score > Hufflepuff_score and Gryffindor_score > Ravenclaw_score and Gryffindor_score > Slytherin_score:
    print('You belong to Gryffindor!')
elif Hufflepuff_score > Ravenclaw_score and Hufflepuff_score > Slytherin_score:
    print('You belong to Hufflepuff!')
elif Ravenclaw_score > Slytherin_score:
    print('You belong to Ravenclaw!')
else:
    print('You belong to Slytherin!')