def calculate_bmr(weight_lbs, height_inches, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation.

    Parameters:
    - weight_lbs (float): Weight in pounds
    - height_inches (float): Height in inches
    - age (int): Age in years
    - gender (str): Gender ('male' or 'female')

    Returns:
    - float: BMR value
    """
    # Convert weight from pounds to kilograms and height from inches to centimeters
    weight_kg = weight_lbs * 0.453592
    height_cm = height_inches * 2.54

    if gender.lower() == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")
    return bmr

def calculate_tdee(bmr, activity_level):
    """
    Calculate Total Daily Energy Expenditure (TDEE).

    Parameters:
    - bmr (float): Basal Metabolic Rate
    - activity_level (str): Activity level ('sedentary', 'light', 'moderate', 'active', 'very active', 'extra active')

    Returns:
    - float: TDEE value
    """
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.465,
        'active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    if activity_level.lower() not in activity_multipliers:
        raise ValueError("Activity level must be one of: 'sedentary', 'light', 'moderate', 'active', 'very active', 'extra active'")
    
    tdee = bmr * activity_multipliers[activity_level.lower()]
    return tdee

def main():
    try:
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
        age = int(input("Enter your age in years: "))
        gender = input("Enter your gender (male/female): ")
        
        activity_level = input(
            "Enter your activity level (sedentary, light, moderate, active, very active, extra active): "
        )
        
        bmr = calculate_bmr(weight, height, age, gender)
        tdee = calculate_tdee(bmr, activity_level)

        print(f"\nYour BMR is: {bmr:.2f} calories/day")
        print(f"Your TDEE is: {tdee:.2f} calories/day")
    except ValueError as e:
        print(f"Input error: {e}")

# Uncomment below to run the script if using an IDE or script file
main()
