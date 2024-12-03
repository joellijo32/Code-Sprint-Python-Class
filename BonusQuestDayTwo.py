# Bonus Quest On Day Two

names = []
while True: 
    print("\nEnter 1 to Add a Name\nEnter 2 to Remove a Name\nEnter 3 to Check for a Name\nEnter 4 to Display the Names\nEnter 5 to Exit: \nYour Choice : ",end="")
    choice = (input())
    if choice.isnumeric() : 
        if (len(choice) > 1) or (int(choice) not in [1,2,3,4,5]) : 
            print("\nINVALID INPUT\n")
            break
        else:
                choice = int(choice)
                #Entering
                if choice == 1: 
                    print("\nEnter the Name: ",end="")
                    names.append(input())
                    print("The name has been added.\n")
                    continue
                
                #Remove
                elif choice == 2: 
                    print("\nEnter the Name to Remove: ",end="")
                    name_to_remove = input()
                    if name_to_remove not in names : 
                        print(f"{name_to_remove} is NOT in the List. Invalid Input.\n")
                    else: 
                        names.remove(name_to_remove)
                        print(f"{name_to_remove} has been Removed from the List.\n")

                #Checking
                elif choice == 3: 
                    print("\nEnter the Name to Check: ",end="")
                    name_to_check = input()
                    if name_to_check in names: 
                        print(f"{name_to_check} is Present in the List.\n")
                    else: 
                        print(f"{name_to_check} is NOT Present in the List.\n")


                #Print
                elif choice == 4: 
                    print("\nThe Names in the List are: \n")
                    counter = 0
                    for i in names: 
                        if counter == 0: 
                            print(i,end="")
                            counter = 1
                        else: 
                            print(", " , i,end="")
                    print("\n")


                elif choice == 5: 
                    print("\nThank You\n")
                    break
                
                
                else: 
                    print("\nINVALID INPUT\n")
                    continue
        

            
    elif choice.isalnum(): 
        print("\nINVALID INPUT\n")
        break



