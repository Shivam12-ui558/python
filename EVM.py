from tkinter import *

root = Tk()
root.title("EVM")
root.geometry("500x300")

v1 = 0
v2 = 0

# Variable to store the voter's name
voter_name = ""

def set_name():
    global voter_name
    voter_name = name_entry.get()
    name_label.config(text=f"Welcome, {voter_name}!")

def vote1():
    global v1
    if voter_name:
        v1 += 1
        print(f"{voter_name} voted for Party 1. Total Votes: {v1}")
    else:
        print("Please enter your name.")

def vote2():
    global v2
    if voter_name:
        v2 += 1
        print(f"{voter_name} voted for Party 2. Total Votes: {v2}")
    else:
        print("Please enter your name.")

def show_result():
    global v1, v2
    
    if v1 > v2:
        result_text = f"Party 1 Wins! (Votes: {v1})"
    elif v2 > v1:
        result_text = f"Party 2 Wins! (Votes: {v2})"
    else:
        result_text = f"It's a Tie! (Party 1: {v1} votes, Party 2: {v2} votes)"
    
    result_label.config(text=result_text)
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)

# Name entry
name_label = Label(root, text="Enter your name:", height=2)
name_label.grid(row=0, column=1)

name_entry = Entry(root)
name_entry.grid(row=0, column=2)

set_name_button = Button(root, text="Enter Name", command=set_name)
set_name_button.grid(row=0, column=3)

Label(root, text="Party 1", height=2, width=10).grid(row=1, column=1)
btn1 = Button(root, text="Vote", command=vote1)
btn1.grid(row=1, column=2)

Label(root, text="Party 2", height=2, width=10).grid(row=2, column=1)
btn2 = Button(root, text="Vote", command=vote2)
btn2.grid(row=2, column=2)

Button(root, text="Show Result", command=show_result).grid(row=3, column=1, columnspan=2)

result_label = Label(root, text="", height=2, width=30, fg="blue")
result_label.grid(row=4, column=1, columnspan=2)

root.mainloop()
