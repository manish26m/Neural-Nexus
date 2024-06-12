
# Tkinter Basics and Core Widgets

## Introduction to Tkinter
Tkinter is the standard Python interface to the Tk GUI toolkit. It provides a fast and easy way to create GUI applications.

### Setting up Tkinter
To use Tkinter, you need to import the `tkinter` module and create a main window object.

```python
import tkinter as tk

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("500x500")
```

## Core Widgets

### Button Widget
A button that triggers an action when clicked.

```python
def on_button_click():
    print("Button Clicked")

button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()
```

### Label Widget
Displays text in the window.

```python
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
```

### Entry Widget
A single-line text input field.

```python
entry = tk.Entry(root)
entry.pack()

def get_entry():
    print(entry.get())

button = tk.Button(root, text="Get Entry", command=get_entry)
button.pack()
```

### Text Widget
A multi-line text input field.

```python
text = tk.Text(root, height=5, width=40)
text.pack()

def get_text():
    print(text.get("1.0", tk.END))

button = tk.Button(root, text="Get Text", command=get_text)
button.pack()
```

### Frame Widget
A container for organizing other widgets.

```python
frame = tk.Frame(root)
frame.pack()

label_in_frame = tk.Label(frame, text="Inside Frame")
label_in_frame.pack()
```

## Geometry Management

### Pack
Simplest geometry manager, packs widgets into a frame.

```python
label.pack(side=tk.LEFT)
button.pack(side=tk.RIGHT)
```

### Grid
Arranges widgets in a grid with rows and columns.

```python
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, columnspan=2)
```

### Place
Places widgets at an absolute position.

```python
label.place(x=50, y=50)
button.place(x=100, y=100)
```

## Event Handling

Tkinter handles events through callback functions.

```python
def on_click(event):
    print(f"Clicked at {event.x}, {event.y}")

root.bind("<Button-1>", on_click)
```

## Advanced Widgets

### Canvas Widget
Used for drawing shapes, images, and other complex layouts.

```python
canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

canvas.create_line(0, 0, 200, 100, fill="blue")
canvas.create_rectangle(50, 50, 150, 100, fill="red")
```

### Message Box
Displays a message box to the user.

```python
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "This is a message box")

button = tk.Button(root, text="Show Message", command=show_message)
button.pack()
```

### Listbox
Displays a list of items from which the user can select.

```python
listbox = tk.Listbox(root)
listbox.pack()

for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)

def get_selected_item():
    selected = listbox.curselection()
    if selected:
        print(listbox.get(selected))

button = tk.Button(root, text="Get Selected Item", command=get_selected_item)
button.pack()
```

## Running the Application

Finally, to run the Tkinter application, you need to call the `mainloop` method.

```python
root.mainloop()
```

## Complete Example

Here's a complete example that includes all the widgets and concepts mentioned above:

```python
import tkinter as tk
from tkinter import messagebox

def on_button_click():
    print("Button Clicked")

def get_entry():
    print(entry.get())

def get_text():
    print(text.get("1.0", tk.END))

def show_message():
    messagebox.showinfo("Information", "This is a message box")

def get_selected_item():
    selected = listbox.curselection()
    if selected:
        print(listbox.get(selected))

def on_click(event):
    print(f"Clicked at {event.x}, {event.y}")

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("500x500")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()

entry = tk.Entry(root)
entry.pack()

text = tk.Text(root, height=5, width=40)
text.pack()

frame = tk.Frame(root)
frame.pack()

label_in_frame = tk.Label(frame, text="Inside Frame")
label_in_frame.pack()

label.pack(side=tk.LEFT)
button.pack(side=tk.RIGHT)
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, columnspan=2)
label.place(x=50, y=50)
button.place(x=100, y=100)

root.bind("<Button-1>", on_click)

canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()
canvas.create_line(0, 0, 200, 100, fill="blue")
canvas.create_rectangle(50, 50, 150, 100, fill="red")

button = tk.Button(root, text="Show Message", command=show_message)
button.pack()

listbox = tk.Listbox(root)
listbox.pack()
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)

button = tk.Button(root, text="Get Selected Item", command=get_selected_item)
button.pack()

root.mainloop()
