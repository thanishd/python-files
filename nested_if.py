age=int(input("enter the number is :"))
if age>20:
    print("you can enter the theme park")
    if age>40:
        print("you can enter the ghost rider")
    elif age>30:
        print("you can enter the swimming pool")
    else:
        print("not permitted area")
else:
    print("you cant enter the theme park")
