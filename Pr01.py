openList = ['[', '(',  '{']
closeList = [']', ')','}']
myList = []
n = input("Enter the string: ")
if (len(n)%2 == 0):
    for i in range(len(n)):
        if i == 0:
            if n[i] in closeList:
                print("The first position should not be closed...")
                break
            else:
                myList.append(n[i])
    
        else:
            if n[i] in openList:
                myList.append(n[i])
                if i == len(n)-1:
                    print(f"order is incorrect at {i+1}")
                    break 
            elif n[i] in closeList:
                if (len(myList) == 0):
                    print(f"The {i+1} position is holding extra brace")
                    break
                else:
                    if closeList.index(n[i]) == openList.index(myList[-1]):
                        myList.pop()
                    else:
                        print(f"The character at postition {i+1} is incorrect.")
                        break
    else:
        if len(myList) == 0:
            print ("The order is correct..")
        else:
            print(f"The string contains {len(myList)} additional open braces")
else:
    print("It should contain even number of braces")