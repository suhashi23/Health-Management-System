#Health Management System
# 3 clients - Suhashi,Sudeshna and Anjali

def getdate():
    import datetime
    return datetime.datetime.now()

import datetime
def gettime():
    return datetime.datetime.now()
def log(k):
    if k==1:
        c=int(input("enter 1 for exercise and 2 for food"))
        if(c==1):
            value=input("type here exercise\n")
            with open("Suhashi-ex.txt","a") as f:
                f.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
        elif(c==2):
            value=input("type here food\n")
            with open("Suhashi-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
    elif k==2:
        c=int(input("enter 1 for exercise and 2 for food"))
        if(c==1):
            value=input("type here exercise\n")
            with open("Sudeshna-ex.txt","a") as f:
                f.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
        elif(c==2):
            value=input("type here food\n")
            with open("Sudeshna-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
    elif k==3:
        c=int(input("enter 1 for exercise and 2 for food"))
        if(c==1):
            value=input("type here exercise\n")
            with open("Anjali-ex.txt","a") as f:
                f.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
        elif(c==2):
            value=input("type here food\n")
            with open("Anjali-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
    else:
        print("Enter a valid input 1(Suhashi), 2(Sudeshna) and 3(Anjali)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("Suhashi-ex.txt") as f:
                for i in f:
                    print(i, end="")
        elif(c==2):
            with open("Suhashi-food.txt") as f:
                for i in f:
                    print(i, end="")
    elif k==2:
        c=int(input("enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("Sudeshna-ex.txt") as f:
                for i in f:
                    print(i, end="")
        elif(c==2):
            with open("Sudeshna-food.txt") as f:
                for i in f:
                    print(i, end="")
    elif k==3:
        c=int(input("enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("Anjali-ex.txt") as f:
                for i in f:
                    print(i, end="")
        elif(c==2):
            with open("Anjali-food.txt") as f:
                for i in f:
                    print(i, end="")
    else:
        print("Enter a valid input (Suhashi,Sudeshna,Anjali)")
print("Health Management System: ")
a=int(input("Press 1 for log the value and 2 for retrieve the value "))

if a==1:
    b= int(input("Press 1 for Suhashi 2 for Sudeshna and 3 for Anjali"))
    log(b)
else:
    b=int(input("Press 1 for Suhashi 2 for Sudeshna and 3 for Anjali "))
    retrieve(b)