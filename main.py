#Sophia Carlone

arrived = []
graduated = ["Alina", "Amanda", "Amelia", "Andrea", "Ceilidh", "Dinh", "Favour", "Katie", "Lee", "Sam", "Trevor"]

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

while(1):
    print("Welcome! Please enter your name!")
    guest = input()
    arrived.append(guest)
    len(graduated)
    # FindGraduated(guest)
    if FindGraduated(guest, 0, len(graduated)-1):
        print("You graduated too! Congrats!")
    print("Do you want to see all the guests that have arrived? (Y/N)")
    answer = input()
    if answer == "Y":
        PrintGuests()
