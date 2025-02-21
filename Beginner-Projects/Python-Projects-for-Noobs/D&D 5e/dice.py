import random
import time


while True:
    rollSum = 0

    # Prompt the user for the number of rolls with validation
    while True:
        try:
            rollNumber = input("How many times does the dice need to be rolled? (Enter 0 to quit) ")
            rollNumber = int(rollNumber)  # Convert input to an integer

            if rollNumber == 0:
                print("Thank you for using our program, and have a great rest of your day!")
                exit()  # Exit the program

            if rollNumber > 0:
                break  # Valid input, exit the loop
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a positive whole number.")

    # Prompt the user for the number of sides on the dice
    while True:
        try:
            diceType = input("How many sides does your dice have? ")
            diceType = int(diceType)  # Convert input to an integer

            if diceType > 0:
                break  # Valid input, exit the loop
            else:
                print("Please enter a positive whole number for the sides of the dice.")
        except ValueError:
            print("Invalid input. Please enter a positive whole number.")

    # Simulate the dice rolls
    for i in range(rollNumber):
        roll = random.randint(1, diceType)
        rollSum += roll
        print("Roll " + str(i + 1) + ": " + str(roll))
        time.sleep(1)

    # Display the total sum of the rolls
    print("TOTAL: " + str(rollSum))


# d4
# d6
# d8
# d10
# d12
# d20
# d100
