import tkinter as tk
from tkinter import messagebox
class MyGUI:
    def __init__(self):
        self.root=tk.Tk()
        self.label=tk.Label(self.root,text="Your Message",font=('Arial',18))
        self.label.pack(padx=10,pady=10)

        self.textbox=tk.Text(self.root,font=("Arial",16))
        self.textbox.bind("<KeyPress>",self.shortcut)#keybord commands
        self.textbox.pack(padx=10,pady=10)

        self.check_state=tk.IntVar()#stores value of check

        self.check=tk.Checkbutton(self.root,text="Show Messagebox",font=("Arial",16),variable=self.check_state)
        self.check.pack(padx=10,pady=10)

        self.button=tk.Button(self.root,text="Show message",font=("Arial",18),command=self.show_message)
        self.button.pack(padx=10,pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW",self.onclosing)#asks user if you want to leave or not

        self.root.mainloop()
    def show_message(self):
        
        if self.check_state.get()==0:#using get we get the answer
            
            print(self.textbox.get("1.0",tk.END))
            #1.0- begining of message, end=ending from 1.0 i.e start to end of message

        else:
            ##MESSAGE BOX EWIDGET:-
            messagebox.showinfo(title="Message",message=self.textbox.get("1.0",tk.END))
    
    def shortcut(self,event):#keyborad shortcut
        if event.state==8 and event.keysym=="Return":
            self.show_message()
            
    def onclosing(self):
        print("HELLO WORD")
        self.root.destroy()
    
MyGUI()