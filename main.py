from tkinter import *
# from tkinter import colorchooser
# from tkinter import messagebox
from tkinter import filedialog

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

# def submit_listbox():
#     selected_items = []
#
#     for index in listbox.curselection():
#         selected_items.insert(index, listbox.get(index))
#
#     if not selected_items:
#         print("You have ordered: Nothing")
#     else:
#         print("You have ordered: ")
#         for index in selected_items:
#             print(index)
# def add_listbox():
#     listbox.insert(listbox.size(), entryBox.get())
#     listbox.config(height=listbox.size())
#
#
# def delete_listbox():
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)
#     listbox.config(height=listbox.size())

# def click_messagebox():
    #messagebox.showinfo(title= "This is the title ye hear",
                        #message="This is the message ye hear",)

    # messagebox.showwarning(title="WARNING!",
    #                     message="This is the warning ye hear",)

    # messagebox.showerror(title="ERROR!",
    #                        message="This is the error ye hear", )

    # if messagebox.askokcancel(title="Ask ok cancle",
    #                         message = "Do that thingamidig?"):
    #     print("You did the thing!")
    # else:
    #     print("You didn't do the thing")

    # if messagebox.askretrycancel(title="Ask ok retry",
    #                           message="Do you want to retry the thing?"):
    #     print("You retry the thing!")
    # else:
    #     print("You didn't retry the thing")

    # if messagebox.askyesno(title="ask yes or no",message="Is that a yes or a no?"):
    #     print("Yessssss")
    # else:
    #     print("Nooooo")

    # answer = messagebox.askquestion(title="Ask Question", message="DO you like the smell of petrol?")
    # if (answer == "yes"):
    #     print("me too")
    # else:
    #     print("liar")

    # answer=messagebox.askyesnocancel(title= "Yes, no or cancel", message="Do you like things?", icon="warning")
    # if(answer==True):
    #     print("you do?")
    # elif(answer==False):
    #     print("You don't?")
    # else:
    #     print("You dodge?")

# def click_colorchooser():
#     # color = colorchooser.askcolor()
#     # print(color)
#     # colorHex = color[1]
#     # print(colorHex)
#     # window.config(background=colorHex)
#     window.config(background=colorchooser.askcolor()[1])

# def submit_text():
#     input = text.get("1.0",END)
#     print(input)


def openFile():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\robfo\\PycharmProjects\\GUI_interface",
                                           title="Open Which File?",
                                           filetypes= (("text_files", "*.txt"), ("all_files", "*.*")))
    file = open(file_path, 'r')
    print(file.read())
    file.close()

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\robfo\\PycharmProjects\\GUI_interface",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All file", ".*")
                                    ])
    if file is None:
        return
    # file_text = str(text.get(1.0, END))
    file_text = input("Enter your text fool:")
    file.write(file_text)
    file.close()

def cut():
    print("You cut the text!")

def copy():
    print("you copy the text!")

def paste():
     print("you paste the text!")


window = Tk()  # instatiate an instance of a window
window.title("Fox's first window")
# window.geometry("500x500")

openImage = PhotoImage(file='burger.png')
saveImage = PhotoImage(file='steak.png')
exitImage = PhotoImage(file='fire.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound=LEFT)
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound=LEFT)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

# button = Button(text="save", command=saveFile)
# button.pack()
#
# text = Text(window)
# text.pack()

# button = Button(text="Open", command=openFile)
# button.pack()
#
# #
# text=Text(window,
#           bg="light yellow",
#           font=("ink free", 25),
#           height=8,
#           width=20,
#           padx=20,
#           pady=20,
#           fg="purple")
# text.pack()
# button = Button(window,text="submit",command=submit_text)
# button.pack()

# button = Button(window,
#                 command=click_colorchooser,
#                 text="Click me!")
# button.pack()

# button = Button(window,
#                 command=click_messagebox,
#                 text="Click me!")
# button.pack()

# listbox = Listbox(window,
#                   bg="#f7ffde",
#                   fg="black",
#                   font=("Constantia", 20),
#                   width=10,
#                   selectmode=MULTIPLE,
#
#                   )
# listbox.pack()
#
# listbox.insert(0, "pizza")
# listbox.insert(1, "pasta")
# listbox.insert(2, "garlic bread")
# listbox.insert(3, "soup")
# listbox.insert(4, "salad")
#
# listbox.config(height=listbox.size())
#
# entryBox = Entry(window)
# entryBox.pack()
#
# addButton = Button(window, text="add", command=add_listbox)
# addButton.pack()
#
# deleteButton = Button(window, text="delete", command=delete_listbox)
# deleteButton.pack()
#
# submitButton = Button(window, text="submit", command=submit_listbox)
# submitButton.pack()

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
