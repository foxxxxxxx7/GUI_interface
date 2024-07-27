from tkinter import *


# def submit():
#     username = entry.get()
#     print("Hello", username)
#     #entry.config(state=DISABLED)
#
# def delete():
#     entry.delete(0,END)
#
# def backspace():
#     entry.delete(len(entry.get())-1,END)

# def display():
#     if(x.get()==1):
#         print("Agreed!")
#     else:
#         print("Not Agreed")

# food = ["Steak", "Burger", "Chicken"]
#
# def order():
#     if(x.get()==0):
#         print("You ordered Steak")
#     elif(x.get()==1):
#         print("you ordered a Burger")
#     elif(x.get()==2):
#         print("You ordered some Chicken")
#     else:
#         print("wtf?")

# def submit_scale():
#     print("The temperature is "+str(scale.get())+ " degrees celcius")

def submit_listbox():
    selected_items = []

    for index in listbox.curselection():
        selected_items.insert(index, listbox.get(index))

    if not selected_items:
        print("You have ordered: Nothing")
    else:
        print("You have ordered: ")
        for index in selected_items:
            print(index)
def add_listbox():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete_listbox():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


window = Tk()  # instatiate an instance of a window
window.title("Fox's first window")

listbox = Listbox(window,
                  bg="#f7ffde",
                  fg="black",
                  font=("Constantia", 20),
                  width=10,
                  selectmode=MULTIPLE,

                  )
listbox.pack()

listbox.insert(0, "pizza")
listbox.insert(1, "pasta")
listbox.insert(2, "garlic bread")
listbox.insert(3, "soup")
listbox.insert(4, "salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window, text="add", command=add_listbox)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete_listbox)
deleteButton.pack()

submitButton = Button(window, text="submit", command=submit_listbox)
submitButton.pack()

# fireImage = PhotoImage(file='fire.png')
# fireLable = Label(image=fireImage)
# fireLable.pack()
#
# scale = Scale(window,
#               from_=100,
#               to=0,
#               lengt=300,
#               orient=VERTICAL, #orientation of the scale default is vertical, can be horizontal
#               font=("Arial", 10),
#               tickinterval=10, #adds indicators for values at given intervals
#               showvalue=1, #will hide current value if =0
#               resolution=.1, #changes the increment value
#               troughcolor="Blue",
#               fg="Red",
#               bg="black",
#               )
# #scale.set(50)#alters starting position
# scale.set(((scale['from']-scale['to'])/2)+scale['to'])# clever way to have it always in the middle no matter the value of from and to
# scale.pack()
#
# snowflakeImage = PhotoImage(file='snowflake.png')
# snowflakeLabel = Label(image=snowflakeImage)
# snowflakeLabel.pack()
#
#
# button = Button(window,
#                 text='submit',
#                 command=submit_scale)
# button.pack()


# steakImage = PhotoImage(file='Steak.png')
# burgerImage = PhotoImage(file='Burger.png')
# chickenImage = PhotoImage(file='Chicken.png')
# foodImages = [steakImage,burgerImage, chickenImage ]

# icon = PhotoImage(file='Fox Logo PNG.png')
# icon2 = PhotoImage(file= 'Fox Logo tiny.png')
# photo = PhotoImage(file='Profile Circular Small.png')
# window.iconphoto(True, icon)
# window.config(background="#FFFFFF")

# x = IntVar()
#
# for index in range(len(food)):
#     radio_button = Radiobutton(window,
#                                text=food[index], # Adds tet to radio buttons
#                                variable=x, # groups radiobuttons together if they share the same variable
#                                value=index,# this assigns each radiobutton a different value
#                                padx=15,
#                                pady=5,
#                                font=("Impact", 30),
#                                image= foodImages[index],
#                                compound=LEFT,
#                                indicatoron=0,# eliminates circle indicators
#                                width=300, #sets width of radiobuttons
#                                command=order #set command of buttons to order function
#                                )
#
#     radio_button.pack(anchor=W) #W for west ('w' works too)

# x = IntVar()
# x = BooleanVar()  # this is for when onvalue (or offvalue) is TRUE instead of 1!
# x = StringVar()  # this is for when onvalue is "Yes" or "On", etc instead of 1 or TRUE!
#
# check_button = Checkbutton(window,
#                            text="Agree to the thing",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=display,
#                            font=("Comic Sans", 30),
#                            fg="Blue",
#                            bg="white",
#                            activeforeground="Blue",
#                            activebackground="white",
#                            padx=20,
#                            pady=5,
#                            image=icon2,
#                            compound=RIGHT)
#
# check_button.pack()

# entry = Entry(window,
#               font=("Arial", 50),
#               fg = "Blue",
#               bg="black",
#               show="*" #Usful for passwords
#               )
# #entry.insert(0,"Default Text")
# entry.pack(side=LEFT)
#
# submit_button = Button(window, text="submit",command=submit)
# submit_button.pack(side=RIGHT)
#
# delete_button = Button(window, text="delete",command=delete)
# delete_button.pack(side=RIGHT)
#
# backspace_button = Button(window, text="backspace",command=backspace)
# backspace_button.pack(side=RIGHT)

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
