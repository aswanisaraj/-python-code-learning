# Game Development Saraj: Snake Water Gun
# Rules:-
# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.
# In situations where both players choose the same object, the result will be a draw.
import random


def enter_choice():
    while True:
        print("Enter your choice from following:")
        for x, y in choice_dict.items():
            print(x, ':', y)
        z = input()
        if z in choice_dict.keys():
            break
        else:
            print('Wrong input, Try again !!!')
    return choice_dict[z]


choice_dict = {'1': 'Snake', '2': 'Water', '3': 'Gun'}
compu_score = 0
your_score = 0
i = 10
while i:
    compu_choice = random.choice(list(choice_dict.values()))
    your_choice = enter_choice()
    if compu_choice == your_choice:
        print(f'computer choice was {compu_choice} and it is tie in round {11-i}')
        i -= 1
        continue
    elif compu_choice == 'Snake' and your_choice == 'Water':
        print(f'computer choice was {compu_choice} and computer won in round {11 - i}')
        compu_score += 1
    elif compu_choice == 'Water' and your_choice == 'Snake':
        print(f'computer choice was {compu_choice} and you won in round {11 - i}')
        your_score += 1
    elif compu_choice == 'Snake' and your_choice == 'Gun':
        print(f'computer choice was {compu_choice} and you won in round {11 - i}')
        your_score += 1
    elif compu_choice == 'Gun' and your_choice == 'Snake':
        print(f'computer choice was {compu_choice} and computer won in round {11 - i}')
        compu_score += 1
    elif compu_choice == 'Water' and your_choice == 'Gun':
        print(f'computer choice was {compu_choice} and computer won in round {11 - i}')
        compu_score += 1
    elif compu_choice == 'Gun' and your_choice == 'Water':
        print(f'computer choice was {compu_choice} and you won in round {11 - i}')
        your_score += 1
    i -= 1
print('Game Over !!!')
if your_score > compu_score:
    print('You Won Finally!!!')
elif compu_score > your_score:
    print('Computer Won Finally!!!')
else:
    print("It is tie !!!")
print(f'your score : {your_score} \ncomputer\'s score: {compu_score}')
