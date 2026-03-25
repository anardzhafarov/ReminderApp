from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog

window = Tk()

# window.geometry("420x420")
# window.config(background="pink")

window

window.filename = filedialog.askopenfilename(title="Select a file", initialdir="C:", filetypes=(("png files", "),("")))

window.mainloop()
