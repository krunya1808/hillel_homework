#Сделать программу в виде функций в которой нужно будет угадывать число.

import random
def game_guess():
    random_numb = random.randint(1, 50)
    print("Program number is: ", random_numb)
    guess_num = int(input("Choose number from 1 to 50: "))
    print("Your number is: ", guess_num)
    if guess_num == random_numb:
        print("Congrats, you win!")
    if guess_num != random_numb:
        print("Sorry, you lose")
game_guess()

