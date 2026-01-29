import tkinter as tk
from tkinter import Label, Entry

main  = tk.Tk(screenName = None, baseName = "Prototype1", className= "Tk", useTk=1)
#Label(main, text = "Calculator").grid(row = 0)
main.title("Prototype1")
def print_number():
    #adsdfdvfvcv


enterCell = Label(main, text = "Enter number: ", width= 6).grid(row = 0)
e1 = Entry(main)
e1.grid(row = 0, column = 1)
One = tk.Button(main, text= "1", width=8, command=print_number).grid(row = 2, column = 1)
Two = tk.Button(main, text= "2", width=8, command=print_number).grid(row = 2, column = 2)
Three = tk.Button(main, text= "3", width=8, command=print_number).grid(row = 2, column = 3)
Four = tk.Button(main, text= "4", width=8, command=print_number).grid(row = 3, column = 1)
Five = tk.Button(main, text= "8", width=8, command=print_number).grid(row = 3, column = 2)
Six = tk.Button(main, text= "6", width=8, command=print_number).grid(row = 3, column = 3)
Seven = tk.Button(main, text= "7", width=8, command=print_number).grid(row = 4, column = 1)
Eight = tk.Button(main, text= "8", width=8, command=print_number).grid(row = 4, column = 2)
Nine = tk.Button(main, text= "9", width=8, command=print_number).grid(row = 4, column = 3)
Zero = tk.Button(main, text= "0", width=8, command=print_number).grid(row = 8, column = 1)


Plus = tk.Button(main, text= "+", width=8, command=main.destroy).grid(row = 2, column = 4)
Minus = tk.Button(main, text= "-", width=8, command=main.destroy).grid(row = 3, column = 4)
Multi = tk.Button(main, text= "*", width=8, command=main.destroy).grid(row = 4, column = 4)
Submulti = tk.Button(main, text= "/", width=8, command=main.destroy).grid(row = 8, column = 2)
Result = tk.Button(main, text= "Result", width=8, command=main.destroy).grid(row = 8, column = 2 and 3)
button = tk.Button(main, text= "Exit", width=8, command=main.destroy).grid(row = 8, column = 4)

main.mainloop()