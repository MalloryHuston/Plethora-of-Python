import random


def roll_4d6_drop_lowest():
    """Roll 4 six-sided dice and drop the lowest one."""
    # Roll four 6-sided dice
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.sort()    # Sort the rolls to easily drop the lowest
    return sum(rolls[1:])   # Sum the top 3 dice (drop the lowest one)


def generate_ability_scores():
    """Generate 6 ability scores by rolling 4d6
    and dropping the lowest roll."""
    # Roll 6 times
    ability_scores = [roll_4d6_drop_lowest() for _ in range(6)]
    return ability_scores


def main():
    """Main function to run the script and ask if the user
    wants to reroll their ability scores."""
    while True:
        # Generate aned display ability scores
        scores = generate_ability_scores()
        print("Your D&D 5e ability scores are:", scores)

        # Ask the user if they want to generate another set of scores
        while True:
            rerun = input
            ("Would you like to roll again? (y/n): ").strip().lower()

            if rerun == 'y':
                break   # Valid input, rerun the loop

            if rerun == 'n':
                print("Exiting the program. Have fun with your character!")
                return  # Exit the entire program

            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue


if __name__ == "__main__":
    main()
