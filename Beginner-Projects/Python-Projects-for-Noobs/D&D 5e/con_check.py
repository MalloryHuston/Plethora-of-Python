def calculate_con_save_dc(damage):
    """
    Calculate the DC for a Constitution saving throw based on the damage taken.

    The DC is 10 or half the damage taken (rounded down), whichever is higher.

    Parameters:
        damage (int): The amount of damage taken.

    Returns:
        int: The DC for the Constitution saving throw.
    """
    return max(10, damage // 2)


# Example usage
damage = int(input("Enter the amount of damage taken: "))
dc = calculate_con_save_dc(damage)
print(f"You must make a Constitution saving throw with a DC of {dc}.")
