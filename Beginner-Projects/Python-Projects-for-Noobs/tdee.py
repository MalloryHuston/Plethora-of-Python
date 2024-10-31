import tkinter as tk
from tkinter import ttk
import math

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

    if gender == 'Male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender == 'Female':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        raise ValueError("Gender must be 'Male' or 'Female'")
    return bmr

def calculate_tdee(weight_lbs, height_inches, age, gender, activity_level):
    """
    Calculate Total Daily Energy Expenditure (TDEE).

    Parameters:
    - weight_lbs (float): Weight in pounds
    - height_inches (float): Height in inches
    - age (int): Age in years
    - gender (str): Gender ('Male' or 'Female')
    - activity_level (str): Activity level ('Sedentary', 'Light', 'Moderate', 'Active', 'Very Active', 'Extra Active')

    Returns:
    - int: TDEE value rounded down to the nearest whole number
    """
    bmr = calculate_bmr(weight_lbs, height_inches, age, gender)

    activity_multipliers = {
        'Sedentary': 1.2,
        'Light': 1.375,
        'Moderate': 1.465,
        'Active': 1.55,
        'Very Active': 1.725,
        'Extra Active': 1.9
    }
    
    tdee = bmr * activity_multipliers[activity_level]
    return math.ceil(tdee)

def calculate_and_display_tdee():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        gender = gender_combobox.get()
        activity_level = activity_combobox.get()
        

        tdee = calculate_tdee(weight, height, age, gender, activity_level)
        result_label.config(text=f"Your TDEE is: {tdee} calories/day")
    except ValueError as e:
        result_label.config(text=f"Input error: {e}")


# Create the main window
root = tk.Tk()
root.title("TDEE Calculator")

# Create and place the widgets
tk.Label(root, text="Weight (in pounds):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height (in inches):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Age (in years):").grid(row=2, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Gender:").grid(row=3, column=0, padx=10, pady=10)
gender_combobox = ttk.Combobox(root, values=["Male", "Female"])
gender_combobox.grid(row=3, column=1, padx=10, pady=10)
gender_combobox.set("Male")

tk.Label(root, text="Activity Level:").grid(row=4, column=0, padx=10, pady=10)
activity_combobox = ttk.Combobox(root, values=["Sedentary", "Light", "Moderate", "Active", "Very Active", "Extra Active"])
activity_combobox.grid(row=4, column=1, padx=10, pady=10)
activity_combobox.set("Sedentary")

# Calculate button
calculate_button = tk.Button(root, text="Calculate TDEE", command=calculate_and_display_tdee)
calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()