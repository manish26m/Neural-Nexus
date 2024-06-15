import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")  # Adjust the window size
        
        self.menubar = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without question", command=exit)
        
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)
        self.actionmenu.add_separator()
        self.actionmenu.add_command(label="clear message",command=self.clearM)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        
        self.root.config(menu=self.menubar)
        
        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.root, font=("Arial", 16),height=5, width=30)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="Show message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        self.clearbtn = tk.Button(self.root, text="Clear message", font=("Arial", 18), command=self.clearM)
        self.clearbtn.pack(padx=10, pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))
    
    def shortcut(self, event):
        if event.state == 8 and event.keysym == "Return":
            self.show_message()
    
    def on_closing(self):
        if messagebox.askyesno(title="quit??", message="Wanna leave us so soon"):
            self.root.destroy()
    
    def clearM(self):
        self.textbox.delete("1.0", tk.END)
    
MyGUI()
