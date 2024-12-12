from datetime import datetime, timedelta


def get_day_of_week(year, month, day):
    if year > 0:
        # AD year (Anno Domini)
        try:
            date = datetime(year, 1, 1) # Jan 1st of the year
            return date.strftime("%A")
        except ValueError:
            return "Invalid date provided. Please ensure the date is correct."
    else:
        # BC year (Before Christ)
        try:
            # Calculate the Gregorian equivalent for BC
            bc_year = abs(year)
            julian_day = datetime(1, month, day) - timedelta(days=(365 * bc_year + (bc_year // 4)))
            return julian_day.strftime("%A")
        except ValueError:
            return "Invalid date provided. Please ensure the date is correct."


# Example usage
try:
    year_input = int(input("Enter a year (BC as negative, e.g., -469 for 469 BC, AD as positive): "))
    month_input = int(input("Enter a month (1-12): "))
    day_input = int(input("Enter a day (1-31): "))
    day_of_week = get_day_of_week(year_input, month_input, day_input)
    print(f"The date {year_input}-{month_input:02d}-{day_input:02d} was a {day_of_week}.")
except ValueError:
    print("Invalid input. Please enter numerical values for year, month, and day.")
