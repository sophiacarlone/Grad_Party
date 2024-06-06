#Sophia Carlone

##IMPORTS
from tkinter import *
from tkinter import ttk

##GLOBALS
arrived = []
graduated = ["Alina", "Amanda", "Amelia", "Andrea", "Ceilidh", "Dinh", "Favour", "Katie", "Lee", "Sam", "Trevor"]


##FUNCTIONS

# def FindGraduated(guest):
#     for x in graduated:
#         # print(x)
#         if x == guest:
#             print("You graduated too! Congrats")

def FindGraduated(guest, start, end):
    if start > end:
        return False
    elif start==end:
        if guest == graduated[start]:
            return True
        else:
            return False
        
    mid = int((end-start)/2 + start)
    if guest > graduated[mid]:
        return FindGraduated(guest, mid + 1, end)
    elif guest == graduated[mid]:
        return True
    else:
        return FindGraduated(guest, start, mid - 1) 
    

def PrintGuests():
    for x in arrived:
        print(x)


def AddGuest():
    arrived.append(guest.get())
    if FindGraduated(guest.get(), 0 , len(graduated)-1):
        CongratsWindow()
    textBox.delete(0, END)

    
def FAQsWindow():
    FAQ_Window = Toplevel(root)
    FAQ_Window.title("FAQs")
    FAQ_Window.geometry("500x500")


def CongratsWindow():
    Congrats_Window = Toplevel(root)
    Congrats_Window.title("Congrats!")
    Congrats_Window.geometry("500x500")
    l = Label(Congrats_Window, text="Great Job!")
    l.pack()


def PeopleArrivedWindow():
    People_Window = Toplevel(root)
    People_Window.title("Arrived List")
    People_Window.geometry("200x200")
    #guest frame
    scrollbar = Scrollbar(People_Window)
    scrollbar.pack(side=RIGHT, fill=Y)
    guest_list=Listbox(People_Window, yscrollcommand=scrollbar.set)
    for name in arrived:
        guest_list.insert(END, name)
    guest_list.pack(fill=BOTH)
    scrollbar.config(command=guest_list.yview)


##MAIN
#root
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title("Grad Party")
root.config(bg="skyblue")
root.geometry("%dx%d" % (width, height))
label = Label(root, text="Grad Party")
#root variables
guest = StringVar()
#text
welcome = Label(root, text="WELCOME")
welcome.config(bg="skyblue", font=('Arial', 50), pady=10)
welcome.pack()
#entry box
textBox = Entry(root, textvariable=guest)
textBox.pack()
#enter guest button
enter_button = Button(root, text="Enter", command=AddGuest)
enter_button.config(guest.set(""))
enter_button.pack()
#bottom Buttons
extras = Frame(root, bg="skyblue")
extras.columnconfigure(0, weight=1)
extras.columnconfigure(0, weight=1)
currentGuests = Button(extras, text="Who's Here?", command=PeopleArrivedWindow).grid(column=0, row=0)
FAQs = Button(extras, text="FAQs", command=FAQsWindow).grid(column=1, row=0)
extras.pack(side=BOTTOM)

root.mainloop()