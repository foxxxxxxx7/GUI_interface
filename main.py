from tkinter import *

window = Tk() # instatiate an instance of a window
window.geometry("690x690")
window.title("Fox's first window")

icon = PhotoImage(file='Fox Logo PNG.png')
window.iconphoto(True, icon)
window.config(background="#FF0827")

window.mainloop() # shows window on screen, listens for events
