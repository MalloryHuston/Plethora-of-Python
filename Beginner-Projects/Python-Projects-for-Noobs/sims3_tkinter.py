import tkinter as tk
import random

# Set up the Tkinter window
root = tk.Tk()
root.title("Sims 3 Random Face Generator")
root.geometry("500x700")

# Function to display results in the text widget
def display_result(text):
    result_display.insert(tk.END, text + "\n")
    result_display.see(tk.END)

# Function to roll head
def roll_head():
    display_result("\nRolling Head:")
    display_result("Face Height: " + str(random.randint(min_val, max_val)))
    display_result("Face Profile: " + str(random.randint(min_val, max_val)))
    display_result("Head Width: " + str(random.randint(-256, 0)))

# Function to roll chin
def roll_chin():
    display_result("\nRolling Chin:")
    display_result("Chin Depth: " + str(random.randint(0, 150)))
    display_result("Chin Height: " + str(random.randint(-150, 256)))
    display_result("Chin Scale: " + str(random.randint(-175, 100)))
    display_result("Chin Underlip Depth: " + str(random.randint(-100, 150)))

# Function to roll jaw
def roll_jaw():
    display_result("\nRolling Jaw:")
    display_result("Jaw Depth: " + str(random.randint(-80, 150)))
    display_result("Jaw Height: " + str(random.randint(-175, 175)))
    display_result("Jaw Shape: " + str(random.randint(-175, 125)))
    display_result("Jaw Underbite: " + str(random.randint(0, 75)))
    display_result("Jaw Width: " + str(random.randint(-256, 175)))

# Function to roll cheek
def roll_cheek():
    display_result("\nRolling Cheek:")
    display_result("Cheek Bone Height: " + str(random.randint(min_val, max_val)))
    display_result("Cheek Bone Shape: " + str(random.randint(-175, 175)))
    display_result("Cheek Fullness: " + str(random.randint(-150, 150)))
    display_result("Cheek Jowls: " + str(random.randint(0, 156)))
    display_result("Nasolabial Crease: " + str(random.randint(0, 200)))

# Function to roll ears
def roll_ears():
    display_result("\nRolling Ears:")
    display_result("Ears Orbit: " + str(random.randint(-120, 256)))
    display_result("Ears Point: " + str(random.randint(0, 20)))
    display_result("Ears Rotate: " + str(random.randint(-256, 0)))
    display_result("Ears Scale: " + str(random.randint(-100, 0)))

# Function to roll eyes
def roll_eyes():
    display_result("\nRolling Eyes:")
    display_result("Eye Depth: " + str(random.randint(min_val, max_val)))
    display_result("Eye Distance: " + str(random.randint(-256, 100)))
    display_result("Eye Height: " + str(random.randint(-150, 150)))
    display_result("Eye Scale: " + str(random.randint(-175, 100)))
    display_result("Eye Socket Height: " + str(random.randint(-125, 125)))
    display_result("Rotate Eyes: " + str(random.randint(-100, 100)))

# Function to roll eye shape
def roll_eye_shape():
    display_result("\nRolling Eye Shape:")
    display_result("Eye Apex: " + str(random.randint(-175, 175)))
    display_result("Eye Corner Height: " + str(random.randint(-100, 100)))
    display_result("Eye Inner Corner Height: " + str(random.randint(-150, 150)))
    display_result("Eye Shape: " + str(random.randint(-100, 256)))
    display_result("Eye Apex Lower: " + str(random.randint(-150, 100)))

# Function to roll eyelids
def roll_eyelids():
    display_result("\nRolling Eyelids:")
    display_result("Eyelid Height: " + str(random.randint(-100, 100)))
    display_result("Eyes Lower Lid Height: " + str(random.randint(0, 256)))
    display_result("Eyes Upper Lid Height: " + str(random.randint(0, 125)))

# Function to roll brow
def roll_brow():
    display_result("\nRolling Brow:")
    display_result("Brow Curve: " + str(random.randint(-175, 175)))
    display_result("Brow Definition: " + str(random.randint(0, 100)))
    display_result("Brow Height: " + str(random.randint(-175, 175)))
    display_result("Brow Rotation: " + str(random.randint(-175, 50)))

# Function to roll nose
def roll_nose():
    display_result("\nRolling Nose:")
    display_result("Nose Definition: " + str(random.randint(-175, 256)))
    display_result("Nose Height: " + str(random.randint(-100, 150)))
    display_result("Nose Length: " + str(random.randint(-175, 50)))
    display_result("Nose Mass: " + str(random.randint(0, 175)))
    display_result("Nose Rotate: " + str(random.randint(-150, 125)))
    display_result("Nose Scale: " + str(random.randint(-175, 75)))
    display_result("Nose Width: " + str(random.randint(-200, 110)))

# Function to roll nostrils
def roll_nostril():
    display_result("\nRolling Nostril:")
    display_result("Nostril Definition: " + str(random.randint(-100, 150)))
    display_result("Nostril Height: " + str(random.randint(-150, 175)))
    display_result("Nostril Rotate: " + str(random.randint(-125, 150)))
    display_result("Nostril Scale: " + str(random.randint(-125, 150)))

# Function to roll tip
def roll_tip():
    display_result("\nRolling Tip:")
    display_result("Nose Tip Depth: " + str(random.randint(-35, 135)))
    display_result("Nose Tip Rotate: " + str(random.randint(-125, 150)))
    display_result("Nose Tip Scale: " + str(random.randint(-125, 175)))

# Function to roll bridge
def roll_bridge():
    display_result("\nRolling Bridge:")
    display_result("Bridge Depth: " + str(random.randint(-100, 200)))
    display_result("Bridge Height: " + str(random.randint(-130, 130)))
    display_result("Bridge Rotate: " + str(random.randint(-100, 175)))
    display_result("Bridge Width: " + str(random.randint(-150, 100)))

# Function to roll mouth
def roll_mouth():
    display_result("\nRolling Mouth:")
    display_result("Mouth Corner Depth: " + str(random.randint(-175, 150)))
    display_result("Mouth Corners Rotate: " + str(random.randint(-150, 150)))
    display_result("Mouth Curve: " + str(random.randint(-100, 175)))
    display_result("Mouth Definition: " + str(random.randint(-100, 175)))
    display_result("Mouth Depth: " + str(random.randint(-175, 150)))
    display_result("Mouth Height: " + str(random.randint(-200, 175)))
    display_result("Mouth Width: " + str(random.randint(-150, 150)))

# Function to roll lower lip
def roll_lower_lip():
    display_result("\nRolling Lower Lip:")
    display_result("Lower Lip Shape: " + str(random.randint(-175, 175)))
    display_result("Lower Lip Thickness: " + str(random.randint(-100, 200)))
    display_result("Lower Lip Width: " + str(random.randint(-175, 175)))

# Function to roll upper lip
def roll_upper_lip():
    display_result("\nRolling Upper Lip:")
    display_result("Upper Lip Shape: " + str(random.randint(50, 200)))
    display_result("Upper Lip Thickness: " + str(random.randint(-256, 170)))
    display_result("Upper Lip Width: " + str(random.randint(-100, 100)))

# Set random ranges
min_val = -256
max_val = 256

# Text box to display the results
result_display = tk.Text(root, height=30, width=60)
result_display.pack(pady=10)

# Buttons for each feature roll
tk.Button(root, text="Roll Head", command=roll_head).pack(pady=5)
tk.Button(root, text="Roll Chin", command=roll_chin).pack(pady=5)
tk.Button(root, text="Roll Jaw", command=roll_jaw).pack(pady=5)
tk.Button(root, text="Roll Cheek", command=roll_cheek).pack(pady=5)
tk.Button(root, text="Roll Ears", command=roll_ears).pack(pady=5)
tk.Button(root, text="Roll Eyes", command=roll_eyes).pack(pady=5)
tk.Button(root, text="Roll Eye Shape", command=roll_eye_shape).pack(pady=5)
tk.Button(root, text="Roll Eyelids", command=roll_eyelids).pack(pady=5)
tk.Button(root, text="Roll Brow", command=roll_brow).pack(pady=5)
tk.Button(root, text="Roll Nose", command=roll_nose).pack(pady=5)
tk.Button(root, text="Roll Nostril", command=roll_nostril).pack(pady=5)
tk.Button(root, text="Roll Tip", command=roll_tip).pack(pady=5)
tk.Button(root, text="Roll Bridge", command=roll_bridge).pack(pady=5)
tk.Button(root, text="Roll Mouth", command=roll_mouth).pack(pady=5)
tk.Button(root, text="Roll Lower Lip", command=roll_lower_lip).pack(pady=5)
tk.Button(root, text="Roll Upper Lip", command=roll_upper_lip).pack(pady=5)

# Start the Tkinter main loop
root.mainloop()
