from tkinter import *
from ImgFileProcessing import ImgFileProcessing
from PIL import ImageTk, Image

root = Tk()

img = ImgFileProcessing('images/cat.jpg')
imparsed = ImageTk.PhotoImage(Image.fromarray(img.get_image()))
imloc = Label(root, image=imparsed)
imloc.grid(row=0, column=0)

root.mainloop()
