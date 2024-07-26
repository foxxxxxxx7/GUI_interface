from tkinter import *

def submit():
    username = entry.get()
    print("Hello", username)
    #entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()  # instatiate an instance of a window
window.title("Fox's first window")

icon = PhotoImage(file='Fox Logo PNG.png')
icon2 = PhotoImage(file= 'Fox Logo tiny.png')
photo = PhotoImage(file='Profile Circular Small.png')
window.iconphoto(True, icon)
window.config(background="#FFFFFF")

entry = Entry(window,
              font=("Arial", 50),
              fg = "Blue",
              bg="black",
              show="*" #Usful for passwords
              )
#entry.insert(0,"Default Text")
entry.pack(side=LEFT)

submit_button = Button(window, text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)

# count = 0
# def click():
#     global count
#     count+=1
#     print("The button has been clicked", count, "Times!")
#
# button = Button (window,
#                  text="Click Here!",
#                  command=click,
#                  font=("Helvetica",20),
#                  fg="white",
#                  bg="black",
#                  activeforeground="white",
#                  activebackground="black",
#                  state=ACTIVE,
#                  image=icon2,
#                  compound='bottom')
#
# button.pack()

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
