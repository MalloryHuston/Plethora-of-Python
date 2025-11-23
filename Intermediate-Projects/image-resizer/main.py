from tkinter import Tk, Label, Button, Entry, filedialog
from PIL import Image


def resize_image(input_path, output_path, width, height):
    with Image.open(input_path) as img:
        resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
        resized_img.save(output_path)
        print(f"[CLI] Image saved to {output_path} with size {width}x{height}")


# GUI Application
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    input_entry.delete(0, "end")
    input_entry.insert(0, file_path)


def save_file_dialog():
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    output_entry.delete(0, "end")
    output_entry.insert(0, file_path)


def run_resize():
    in_path = input_entry.get()
    out_path = output_entry.get()
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        resize_image(in_path, out_path, width, height)
        status_label.config(text="✅ Resizing complete!", fg="green")
    except Exception as e:
        status_label.config(text=f"❌ Error: {e}", fg="red")


# Build GUI
root = Tk()
root.title("Image Resizer")

Label(root, text="input Image Path:").grid(row=0, column=0)
input_entry = Entry(root, width=40)
input_entry.grid(row=0, column=1)
Button(root, text="Browse", command=open_file_dialog).grid(row=0, column=2)

Label(root, text="Output Image Path:").grid(row=1, column=0)
output_entry = Entry(root, width=40)
output_entry.grid(row=1, column=1)
Button(root, text="Save As", command=save_file_dialog).grid(row=1, column=2)

Label(root, text="Width:").grid(row=2, column=0)
width_entry = Entry(root, width=10)
width_entry.grid(row=2, column=1, sticky="w")

Label(root, text="Height:").grid(row=3, column=0)
height_entry = Entry(root, width=10)
height_entry.grid(row=3, column=1, sticky="w")

Button(root, text="Resize Image", command=run_resize).grid(
    row=4, column=1, pady=10
)

status_label = Label(root, text="")
status_label.grid(row=5, column=1)

root.mainloop()
