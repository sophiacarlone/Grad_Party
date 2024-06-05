#Sophia Carlone

arrived = []
graduated = ["Alina", "Trevor", "Ceilidh", "Lee", "Amelia", "Favour", "Dinh", "Sam", "Amanda", "Katie", "Andrea"]
graduated = graduated.sort()


def FindGraduated(guest, start, end):
    if start==end:
        if guest == graduated[start]:
            return True
        else:
            return False
        
    mid = end/2
    if guest >= graduated[mid]:
        start = mid
    else:
        end = mid - 1
    FindGraduated(guest, start, end)

print("Welcome! Please enter your name!")
guest = input()
arrived.insert(guest)
if FindGraduated(guest, 0, graduated.len()-1):
    print("You graduated too! Congrats!")
