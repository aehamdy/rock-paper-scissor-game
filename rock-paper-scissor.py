
player = input('\nSelect your choice "rock", "paper" or "scissor": ')

choices = ['rock', 'paper', 'scissor']

import random
pc = choices[random.randint(0,2)]
print(f'\nYour choice is "{player}", and the PC choice is: "{pc}"')

if player == pc:
    print('\nDraw!\n')
elif (player == "rock" and pc == "scissor") or (player == "scissor" and pc == "paper") or (player == "paper" and pc == "rock"):
    print('\nYou won! 👍\n')
else:
    print('\nYou lose! 👎\n')
