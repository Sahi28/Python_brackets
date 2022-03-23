marksList = []
sortList = []
tempList = []
n = int(input("Enter number of students: "))
for i in range (n):
    a = input("Ener the marks of student: ")
    marksList.append(a)
sortList = marksList.copy()
sortList.sort(reverse=True)
for i in range(n):
    tempList.append(marksList.index(sortList[i]))
print (tempList)