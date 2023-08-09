import tkinter as tk
from PIL import Image, ImageTk

def convert_to_celsius():
    temperature = float(entry_temperature.get())
    celsius = (temperature - 32) * 5/9
    label_result.config(text=f"{temperature:.2f} °F = {celsius:.2f} °C")

def convert_to_fahrenheit():
    temperature = float(entry_temperature.get())
    fahrenheit = temperature * 9/5 + 32
    label_result.config(text=f"{temperature:.2f} °C = {fahrenheit:.2f} °F")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("420x420")
root.configure(bg="light blue")

# Load the background image
background_image = Image.open("sky.jpg") 
background_photo = ImageTk.PhotoImage(background_image)

# Create a Label widget to hold the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Temperature entry
label_temperature = tk.Label(root, text="Temperature Convertor", font=("Helvetica", 20, 'bold'),bg='black',fg='yellow')
label_temperature.pack( padx=10, pady=10)

label_temperature = tk.Label(root, text="Enter Temperature", font=("Helvetica", 20, 'bold'),bg='black',fg='yellow')
label_temperature.pack( padx=10, pady=10)

entry_temperature = tk.Entry(root, width=15, font=("Helvetica", 20),justify=tk.LEFT)
entry_temperature.pack(padx=10, pady=10)

# Conversion buttons
button_celsius = tk.Button(root, text="Convert to Celsius", command=convert_to_celsius, font=("Helvetica", 18, 'bold'),bg='black',fg='yellow')
button_celsius.pack(padx=10, pady=10)

button_fahrenheit = tk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit, font=("Helvetica", 18, 'bold'),bg='black',fg='yellow')
button_fahrenheit.pack(padx=5, pady=5)

# Result label
label_result = tk.Label(root, text="", font=("Helvetica", 30, 'bold'),bg='orange',fg='black')
label_result.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()

