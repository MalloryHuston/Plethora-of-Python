import random
import time

play = ''

while True:
    rollSum = 0
    rollNumber = int(input("How many times does the dice need to be rolled? "))
    diceType = int(input("How many sides does your dice have? "))


    for i in range (rollNumber):
        roll = random.randint(1, diceType)
        rollSum += roll
        print("Roll " + str(i + 1) + ": " + str(roll))
        time.sleep(1)
    

    print("TOTAL : " + str(rollSum))


# d4
# d6
# d8
# d10
# d12
# d20
# d100