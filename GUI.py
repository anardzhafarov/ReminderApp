from tkinter import *

def submit(event):
    return user_input.get()

def submit_per_button():
    return user_input.get()

def delete():
    user_input.delete(0, END)

window = Tk()
window.title("Reminder")
window.geometry("600x600")
window.config(bg="#B3CEE5")

text_bar_frame = Frame(window, bg="#B3CEE5")
text_bar_frame.grid(row=0, column=0, padx=150, pady=5)

user_input = Entry(text_bar_frame)
user_input.config(font=("Times New Roman", 13))

user_input.bind("<Return>", submit)
user_input.grid(row=1, column=0)

submit_button = Button(text_bar_frame, text="Submit", command=submit_per_button)
submit_button.grid(row=1, column=2)

delete_button = Button(text_bar_frame, text="Delete", command=delete)
delete_button.grid(row=1, column=1)

# text_label = Label(text_bar_frame, text="Put in the number of events")
# text_label.grid(row=0, column=0, padx=50)

window.mainloop()
