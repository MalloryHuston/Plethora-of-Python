def get_average_hp(class_levels, constitution_mod, tough_feat, hill_dwarf, draconic_sorcerer):
    """
    Calculate the average HP of a multiclass D&D 5e character,
    factoring in Tough feat, Hill Dwarf race, and Draconic Sorcerer.

    :param class_levels: Dictionary where keys are class names and values are levels.
    :param constitution_mod: Integer representing the character's Constitution modifier.
    :param tough_feat: Boolean indicating whether the Tough feat is taken.
    :param hill_dwarf: Boolean indicating if the character is a Hill Dwarf.
    :param draconic_sorcerer: Boolean indicating if the character is a Draconic Sorcerer.
    :return: Integer average HP.
    """

    # Define hit dice per class (D&D 5e standard)
    hit_dice = {
        "artificer": 8, "barbarian": 12,
        "fighter": 10, "paladin": 10, "ranger": 10,
        "bard": 8, "cleric": 8, "druid": 8, "monk": 8, "rogue": 8, "warlock": 8,
        "blood hunter": 10, "sorcerer": 6, "wizard": 6,
    }

    total_hp = 0
    first_class = True  # Track first class to apply max hit die rule

    for class_name, level in class_levels.items():
        if class_name not in hit_dice:
            print(f"Warning: {class_name} is not a valid class.")
            continue

        hit_die = hit_dice[class_name]

        # Level 1 max hit die, rest use average
        if first_class:
            hp = hit_die + constitution_mod  # Max roll at level 1
            level -= 1
            first_class = False
        else:
            hp = 0

        # Average HP for remaining levels
        if level > 0:
            avg_hp_per_level = (hit_die // 2) + 1
            hp += level * (avg_hp_per_level + constitution_mod)

        # Apply Draconic Sorcerer bonus
        if class_name == "sorcerer" and draconic_sorcerer:
            hp += class_levels["sorcerer"]  # +1 HP per sorcerer level

        total_hp += hp

    # Apply racial and feat bonuses
    total_levels = sum(class_levels.values())

    if tough_feat:
        total_hp += total_levels * 2  # +2 HP per level

    if hill_dwarf:
        total_hp += total_levels  # +1 HP per level

    return total_hp


# User Input
def get_user_input():
    print("Enter your character's class levels:")

    class_levels = {}

    while True:
        class_name = input("Enter a class name (or 'done' to finish): ").strip().lower()
        if class_name == "done":
            break
        level = input(f"Enter level for {class_name}: ")

        if not level.isdigit() or int(level) <= 0:
            print("Please enter a valid positive integer for level.")
            continue

        class_levels[class_name] = int(level)

    constitution_modifier = input("Enter Constitution modifier: ")
    while not constitution_modifier.lstrip('-').isdigit():
        print("Please enter a valid integer for Constitution modifier.")
        constitution_modifier = input("Enter Constitution modifier: ")

    constitution_modifier = int(constitution_modifier)

    # Ask if the character has the Tough feat
    tough_feat = input("Did your character take the Tough feat? (yes/no): ").strip().lower() == "yes"

    # Ask if the character is a Hill Dwarf
    hill_dwarf = input("Is your character a Hill Dwarf? (yes/no): ").strip().lower() == "yes"

    # Check if the character has levels in Sorcerer, then ask if they are Draconic
    draconic_sorcerer = False
    if "sorcerer" in class_levels:
        draconic_sorcerer = input("Is your Sorcerer subclass Draconic Bloodline? (yes/no): ").strip().lower() == "yes"

    return class_levels, constitution_modifier, tough_feat, hill_dwarf, draconic_sorcerer


# Get user input
character_classes, constitution_modifier, tough_feat, hill_dwarf, draconic_sorcerer = get_user_input()

# Calculate and display HP
average_hp = get_average_hp(character_classes, constitution_modifier, tough_feat, hill_dwarf, draconic_sorcerer)
print(f"\nYour character's average HP: {average_hp}")
