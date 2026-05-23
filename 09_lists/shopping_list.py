Empty_list = []

while True:
    print("=========== Shopping List=================")
    print("1. Add item on the list")
    print("2. Remove the item from the list")
    print("3. Show the item from the list")
    print("4. Exit the list")

    choice = input("Enter Your choice")

    if choice == 1:
        item = input("Enter the name of the item:")
        Empty_list.append(item)
        print(item,"Added on the list succesfully")

    elif choice == 2:
        remove_item = input("Enter the item which u want to delete from the list:")
        
        if remove_item in Empty_list :
          Empty_list.remove(remove_item)
          print( remove_item ," Removed Successfully!")

        else:
            print("items is not present in the list")

    elif choice == 3:
        if len(Empty_list) == 0:
            print("No items is present in the list")

        else:
            print("Shopping List")
            for item in Empty_list:
                print("-", Empty_list)


    elif choice== 4:
        print("Exiting the program")
        break

    else:
        print("INVALID CHOICE!. PLEASE TRY AGAIN LATER")
