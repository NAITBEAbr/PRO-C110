import random

response = "y"

while response == "y":
    dice_roll = random.randint(1, 6)

    if dice_roll == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
    elif dice_roll == 2:
        print("---------")
        print("|       |")
        print("| 0   0 |")
        print("|       |")
        print("---------")
    elif dice_roll == 3:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("|   0   |")
        print("---------")
    elif dice_roll == 4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")
    elif dice_roll == 5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")
    else:
        print("---------")
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |")
        print("---------")

    response = input("Deseja jogar o dado novamente? (y/n): ")

print("Obrigado por jogar!")





