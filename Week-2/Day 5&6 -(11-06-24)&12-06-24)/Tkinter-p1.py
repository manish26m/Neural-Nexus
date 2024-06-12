import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("My Tkinter App")
root.geometry("500x500")

# Define a function to be called when the button is clicked
def on_button_click():
    print("Button Clicked")

# Define a function to get input from the Entry widget
def get_input():
    print(entry.get())

# Define a function to get text from the Text widget
def get_text():
    print(text.get("1.0", tk.END))

# Define a function to show a message box
def show_message():
    messagebox.showinfo("Message Box", "This is a message box!")

# Define a function to get selected item from Listbox
def get_selected_item():
    selected_item = listbox.get(tk.ACTIVE)
    print("Selected item:", selected_item)

# Button widget
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()

# Label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Entry widget
entry = tk.Entry(root)
entry.pack()

# Button to get input from the Entry widget
get_input_button = tk.Button(root, text="Get Input", command=get_input)
get_input_button.pack()

# Text widget
text = tk.Text(root, height=5, width=40)
text.pack()

# Button to get text from the Text widget
get_text_button = tk.Button(root, text="Get Text", command=get_text)
get_text_button.pack()

# Frame widget
frame = tk.Frame(root, bg="lightblue")
frame.pack(fill=tk.BOTH, expand=True)

# Label inside the Frame
frame_label = tk.Label(frame, text="Inside Frame")
frame_label.pack()

# Geometry Management with Pack
button1 = tk.Button(root, text="Button 1")
button1.pack(side=tk.LEFT, padx=10, pady=10)

button2 = tk.Button(root, text="Button 2")
button2.pack(side=tk.RIGHT, padx=10, pady=10)

# Geometry Management with Grid
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1)

entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=2)

# Geometry Management with Place
absolute_label = tk.Label(root, text="Absolute Positioning")
absolute_label.place(x=50, y=50)

# Event Handling
def on_button_click_event(event):
    print("Button Clicked with Event")

event_button = tk.Button(root, text="Click Me with Event!")
event_button.pack()
event_button.bind("<Button-1>", on_button_click_event)

# Canvas widget
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.pack()
canvas.create_line(0, 0, 200, 100, fill="blue")
canvas.create_rectangle(50, 25, 150, 75, fill="green")

# Message Box button
message_button = tk.Button(root, text="Show Message", command=show_message)
message_button.pack()

# Listbox widget
listbox = tk.Listbox(root)
listbox.pack()
items = ["Item 1", "Item 2", "Item 3", "Item 4"]
for item in items:
    listbox.insert(tk.END, item)

# Button to get selected item from Listbox
get_selected_button = tk.Button(root, text="Get Selected Item", command=get_selected_item)
get_selected_button.pack()

# Start the main event loop
root.mainloop()
