def get_xp_from_cr(cr):
    # D&D 5e Challenge Rating XP Table
    cr_to_xp = {
        0: 10,
        0.125: 25,
        0.25: 50,
        0.5: 100,
        1: 200,
        2: 450,
        3: 700,
        4: 1100,
        5: 1800,
        6: 2300,
        7: 2900,
        8: 3900,
        9: 5000,
        10: 5900,
        11: 7200,
        12: 8400,
        13: 10000,
        14: 11500,
        15: 13000,
        16: 15000,
        17: 18000,
        18: 20000,
        19: 22000,
        20: 25000,
        21: 33000,
        22: 41000,
        23: 50000,
        24: 62000,
        25: 75000,
        26: 90000,
        27: 105000,
        28: 120000,
        29: 135000,
        30: 155000,
    }
    return cr_to_xp.get(cr, 0)  # Default to 0 if CR is not in table

def calculate_level_and_xp(xp):
    # D&D 5e XP Thresholds
    xp_table = {
        1: 0,
        2: 300,
        3: 900,
        4: 2700,
        5: 6500,
        6: 14000,
        7: 23000,
        8: 34000,
        9: 48000,
        10: 64000,
        11: 85000,
        12: 100000,
        13: 120000,
        14: 140000,
        15: 165000,
        16: 195000,
        17: 225000,
        18: 265000,
        19: 305000,
        20: 355000,
    }

    level = 1
    next_level_xp = 0

    # Determine the level
    for lvl, xp_threshold in xp_table.items():
        if xp < xp_threshold:
            break
        level = lvl
        next_level_xp = xp_threshold

    # Determine XP required for the next level, if applicable
    if level < 20:
        next_level_xp = xp_table[level + 1]
    else:
        next_level_xp = "Max level reached"

    return level, next_level_xp

def main():
    print("Welcome to the XP and Level Tracker!")
    
    # Ask for the initial XP to determine current level
    while True:
        try:
            total_xp = int(input("Enter your current XP: "))
            if total_xp < 0:
                print("XP cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Calculate starting level
    level, next_level_xp = calculate_level_and_xp(total_xp)
    print(f"\nStarting Stats:")
    print(f"Current Level: {level}")
    if isinstance(next_level_xp, int):
        print(f"XP needed for next level: {next_level_xp - total_xp}")
    else:
        print(next_level_xp)  # Max level message

    print("\nNow, enter the Challenge Rating (CR) of each enemy you defeat. Type 'done' to finish.")
    
    while True:
        user_input = input("Enter CR of defeated enemy (or 'done' to finish): ").strip().lower()
        if user_input == 'done':
            break
        
        try:
            cr = float(user_input)
            xp_gained = get_xp_from_cr(cr)
            if xp_gained == 0:
                print("Invalid CR or no XP awarded for this CR. Try again.")
                continue
            
            total_xp += xp_gained
            level, next_level_xp = calculate_level_and_xp(total_xp)
            
            print(f"Enemy defeated! Gained {xp_gained} XP.")
            print(f"Total XP: {total_xp}")
            print(f"Current Level: {level}")
            if isinstance(next_level_xp, int):
                print(f"XP needed for next level: {next_level_xp - total_xp}")
            else:
                print(next_level_xp)  # Max level message
        except ValueError:
            print("Invalid input. Please enter a numeric CR or 'done'.")

    print("\nFinal Stats:")
    level, next_level_xp = calculate_level_and_xp(total_xp)
    print(f"Total XP: {total_xp}")
    print(f"Final Level: {level}")
    if isinstance(next_level_xp, int):
        print(f"XP needed for next level: {next_level_xp - total_xp}")
    else:
        print(next_level_xp)

if __name__ == "__main__":
    main()
