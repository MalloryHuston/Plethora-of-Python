def dnd_speed_to_mph(feet_per_round):
    # D&D rounds are 6b seconds each
    seconds_per_round = 6
    # Convert feet per round to feet per second
    feet_per_second = feet_per_round / seconds_per_round
    # Convert feet per second to miles per hour
    miles_per_hour = (feet_per_second * 3600) / 5280
    return miles_per_hour


# Example usage
feet_per_round = float(input("Enter speed in feet per round: "))
mph = dnd_speed_to_mph(feet_per_round)
print(f"Your character moves at {mph:.2f} miles per hour!")
