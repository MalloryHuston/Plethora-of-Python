def dnd_speed_to_speed(feet_per_round, system="imperial"):
    # D&D rounds are 6 seconds each
    seconds_per_round = 6
    # Convert feet per round to feet per second
    feet_per_second = feet_per_round / seconds_per_round

    if system.lower() == "imperial":
        # Convert to miles per hour
        return (feet_per_second * 3600) / 5280
    elif system.lower() == "metric":
        # Convert to kilometers per hour
        return (feet_per_second * 3600) / 3280.84
    else:
        raise ValueError("Invalid system. Choose either 'imperial' or 'metric'.")


# Example usage
feet_per_round = float(input("Enter speed in feet per round: "))
system = input("Do you use the imperial or metric system? (imperial/metric): ").strip().lower()

try:
    speed = dnd_speed_to_speed(feet_per_round, system)
    unit = "miles per hour" if system == "imperial" else "kilometers per hour"
    print(f"Your character moves at {speed:.2f} {unit}!")
except ValueError as e:
    print(e)
