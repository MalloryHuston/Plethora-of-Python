import tkinter as tk
import random
import re


def roll_dice_with_mode():
    input_text = dice_entry.get().strip()
    result_label.config(text="")  # Clear previous results
    total_rolls = []

    # Toggle between normal, advantage, and disadvantage
    mode = mode_var.get()

    try:
        # Parse the dice roll input (e.g., 2d6+3, 4d8-1)
        rolls = input_text.split(",")
        for roll in rolls:
            match = re.match(r"(\d+)d(\d+)([+-]\d+)?", roll.strip().lower())
            if not match:
                raise ValueError("Invalid input format")

            num = int(match.group(1))  # Number of dice
            die = int(match.group(2))  # Sides of the dice
            # Modifier (+/- value)
            modifier = int(match.group(3)) if match.group(3) else 0

            for _ in range(num):
                if mode == "Normal":
                    roll_result = random.randint(1, die) + modifier
                elif mode == "Advantage":
                    first_roll = random.randint(1, die)
                    second_roll = random.randint(1, die)
                    roll_result = max(first_roll, second_roll) + modifier
                elif mode == "Disadvantage":
                    first_roll = random.randint(1, die)
                    second_roll = random.randint(1, die)
                    roll_result = min(first_roll, second_roll) + modifier
                total_rolls.append(roll_result)

        # Display the result
        rolls_str = ", ".join(map(str, total_rolls))
        total = sum(total_rolls)
        result_label.config(
            text=f"Rolls: {rolls_str}\nTotal: {total}",
            font=("Arial", 16),
            fg="#38b000"
        )
    except ValueError:
        result_label.config(
            text="Invalid input! Use the format '2d6+3, 4d8-1'.",
            font=("Arial", 16),
            fg="red"
        )


def reset_app():
    dice_entry.delete(0, tk.END)
    result_label.config(text="", font=("Arial", 16), fg="black")
    mode_var.set("Normal")


# Initialize the Tkinter app
app = tk.Tk()
app.title("Advanced Dice Roller with Modifiers")
app.geometry("500x600")
app.configure(bg="#1a1a2e")

# Add a heading
heading = tk.Label(
    app,
    text="Advanced Dice Roller",
    font=("Arial", 24, "bold"),
    fg="#00a8cc",
    bg="#1a1a2e",
    pady=20
)
heading.pack()

# Add a text entry for dice rolls
entry_frame = tk.Frame(app, bg="#1a1a2e")
entry_frame.pack(pady=10)

dice_entry_label = tk.Label(
    entry_frame,
    text="Enter rolls (e.g., 2d6+3, 4d8-1):",
    font=("Arial", 12),
    fg="#edf2f4",
    bg="#1a1a2e"
)
dice_entry_label.grid(row=0, column=0, padx=5)

dice_entry = tk.Entry(entry_frame, font=("Arial", 12), width=20)
dice_entry.grid(row=0, column=1, padx=5)

# Add radio buttons for roll modes
mode_var = tk.StringVar(value="Normal")  # Default mode

mode_frame = tk.Frame(app, bg="#1a1a2e")
mode_frame.pack(pady=10)

mode_label = tk.Label(
    mode_frame,
    text="Roll Mode:",
    font=("Arial", 12),
    fg="#edf2f4",
    bg="#1a1a2e"
)
mode_label.grid(row=0, column=0, padx=5)

modes = ["Normal", "Advantage", "Disadvantage"]
for i, mode in enumerate(modes):
    tk.Radiobutton(
        mode_frame,
        text=mode,
        variable=mode_var,
        value=mode,
        font=("Arial", 12),
        fg="#00a8cc",
        bg="#1a1a2e",
        selectcolor="#1a1a2e"
    ).grid(row=0, column=i+1, padx=5)

# Add a button to roll the dice
roll_button = tk.Button(
    app,
    text="Roll",
    font=("Arial", 12, "bold"),
    bg="#162447",
    fg="#e94560",
    width=10,
    height=2,
    command=roll_dice_with_mode
)
roll_button.pack(pady=10)

# Add a label to display the result
result_label = tk.Label(
    app,
    text="",
    font=("Arial", 16),
    fg="black",
    bg="#1a1a2e"
)
result_label.pack()

# Add a reset button
reset_button = tk.Button(
    app,
    text="Reset",
    font=("Arial", 12, "bold"),
    bg="#f77f00",
    fg="black",
    width=10,
    height=2,
    command=reset_app
)
reset_button.pack(pady=10)

# Add an exit button
exit_button = tk.Button(
    app,
    text="Exit",
    font=("Arial", 12, "bold"),
    bg="#f72585",
    fg="black",
    width=10,
    height=2,
    command=app.quit
)
exit_button.pack(pady=20)

# Run the application
app.mainloop()
