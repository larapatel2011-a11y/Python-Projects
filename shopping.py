shopping = {}

print("Option 1 in view list. Option 2 is add to list. Option 3 is remove from list. Option 4 is change value. Option 5 is exit")

while True:
    choice = int(input("Choos an option: "))

    if choice == 1:
        for key,value in shopping.items():
            print(key,value)
    elif choice == 2:
        adding = input("What do you want to add?: ")
        number = int(input("How many do you want to add?: "))
        shopping[adding] = number
    elif choice == 3:
        delete = input("which do you want to delete?: ")
        del shopping[delete]
    elif choice == 4:
        change = input("Which key do you want to change?: ")
        new = input("what do you want to change it to")
        shopping[change]= new
    elif choice == 5:
        break

