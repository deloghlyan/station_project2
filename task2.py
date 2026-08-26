import random


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"The sum of dice is {die1} + {die2} = {total}")
    return total


def play_craps():
    sum_dice = roll_dice()

    if sum_dice in (7, 11):
        print("Congratulations! You win!")
        return
    elif sum_dice in (2, 3, 12):
        print("You lose.")
        return
    else:
        goal_number = sum_dice
        print(f"Now your goal number is {goal_number}")

        while True:
            sum_dice = roll_dice()

            if sum_dice == goal_number:
                print(f"You win!")
                break
            elif sum_dice == 7:
                print("You lose!")
                break

play_craps()