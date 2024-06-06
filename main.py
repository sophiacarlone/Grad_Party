#Sophia Carlone

##IMPORTS
from tkinter import *
from tkinter import ttk

##GLOBALS
arrived = ["Alina", "Amanda", "Amelia", "Andrea", "Ceilidh", "Dinh", "Favour", "Katie", "Lee", "Sam", "Trevor"]
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
    # print(guest.get())
    arrived.append(guest.get())
    # textBox.delete(0, END)
    # guest_list.insert(END,textBox.get())
    print(arrived)
    #TODO add the extra for graduation


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
# extras = Frame(root, bg="skyblue")
# extras.columnconfigure(0, weight=1)
# extras.columnconfigure(0, weight=1)
# currentGuests = Button(extras, text="Who's Here?").grid(column=0, row=0)
# FAQs = Button(extras, text="FAQs").grid(column=1, row=0)
# extras.pack(side=BOTTOM)


# #guest frame
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
# guest_list=Listbox(root, yscrollcommand=scrollbar.set)
# for name in arrived:
#     guest_list.insert(END, name)
# guest_list.pack(side=BOTTOM, fill=BOTH)
# scrollbar.config(command=guest_list.yview)
# # guest_frame = Frame(root, width=width, height= 400, bg="white", bd=50)
# # guest_frame.pack(side="bottom", padx = 20, pady=20)

root.mainloop()

    

# print("Welcome! Please enter your name!")
# guest = input()
# arrived.append(guest)
# len(graduated)
# # FindGraduated(guest)
# if FindGraduated(guest, 0, len(graduated)-1):
#     print("You graduated too! Congrats!")
# print("Do you want to see all the guests that have arrived? (Y/N)")
# answer = input()
# if answer == "Y":
#     PrintGuests()
