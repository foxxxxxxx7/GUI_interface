from tkinter import *

window = Tk()  # instatiate an instance of a window
window.title("Fox's first window")

icon = PhotoImage(file='Fox Logo PNG.png')
icon2 = PhotoImage(file= 'Fox Logo tiny.png')
photo = PhotoImage(file='Profile Circular Small.png')
window.iconphoto(True, icon)
window.config(background="#FFFFFF")

count = 0
def click():
    global count
    count+=1
    print("The button has been clicked", count, "Times!")

button = Button (window,
                 text="Click Here!",
                 command=click,
                 font=("Helvetica",20),
                 fg="white",
                 bg="black",
                 activeforeground="white",
                 activebackground="black",
                 state=ACTIVE,
                 image=icon2,
                 compound='bottom')

button.pack()

# label = Label(window,
#               text="Fox's Label",
#               font=('Gothic', 40, 'italic'),
#               fg='white',
#               bg='black',
#               relief=FLAT,
#               bd=15,
#               padx=30,
#               pady=30,
#               image=photo,
#               compound='bottom')
# label.pack()
# label.place(x=300, y=325)

window.mainloop()  # shows window on screen, listens for events
