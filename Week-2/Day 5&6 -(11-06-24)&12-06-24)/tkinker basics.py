import tkinter as tk

root=tk.Tk()

# get up a simple graphical interface windom

root.geometry("880x500")#dimensions
root.title("My first GUI")

#WIDGETS:-
label=tk.Label(root,text="Hello India!!",font=("Arial",18))#gui display,text,font(type,size)
label.pack(padx=20,pady=20)#padding

textbox=tk.Text(root,height=3,font=('Arial',14))
textbox.pack(padx=10) 

'''myentry=tk.Entry(root)
myentry.pack()#ANother text box
'''
button=tk.Button(root,text="Click ME!",font=("Arial",18))
button.pack(padx=10,pady=10)

root2=tk.Tk()
root2.geometry("500x500")
root2.title("Calculator")

label2=tk.Label(root2,text="Hello India!!",font=("Arial",18))#gui display,text,font(type,size)
label2.pack(padx=20,pady=20)#padding

textbox2=tk.Text(root2,height=3,font=('Arial',14))
textbox2.pack(padx=10)

frames=tk.Frame(root2)
frames.columnconfigure(0,weight=1)
frames.columnconfigure(1,weight=1)
frames.columnconfigure(2,weight=1)

but1=tk.Button(frames,text="1",font=("Arial",18))
but1.grid(row=0,column=0,sticky=tk.W+tk.E)
#W-west,E-east#sticky makes sure that the butttons are totally filled to the widths

but2=tk.Button(frames,text="2",font=("Arial",18))
but2.grid(row=0,column=1,sticky=tk.W+tk.E)

but3=tk.Button(frames,text="3",font=("Arial",18))
but3.grid(row=0,column=2,sticky=tk.W+tk.E)

but4=tk.Button(frames,text="4",font=("Arial",18))
but4.grid(row=1,column=0,sticky=tk.W+tk.E)

but5=tk.Button(frames,text="5",font=("Arial",18))
but5.grid(row=1,column=1,sticky=tk.W+tk.E)

but6=tk.Button(frames,text="6",font=("Arial",18))
but6.grid(row=1,column=2,sticky=tk.W+tk.E)

frames.pack(fill="x")#streches in x dimension

anotherbtn=tk.Button(root2,text="Test")
anotherbtn.place(x=200,y=250,height=100,width=100)


root2.mainloop()
root.mainloop()
