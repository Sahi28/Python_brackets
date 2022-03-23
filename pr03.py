inList = []
n = int(input("Enter number of numbers: "))
for i in range(n):
    a = input("Enter number: ")
    a = int(a.replace(',',''))
    inList.append(a)
inList.sort()
# b = inList[0]
# c = inList[n-1]
# temp = 1
# b = b.replace('',',')
# c = c.replace('',',')
# inList[0] = inList[0].replace('',',')
# inList
# b = [b[i:i+temp] for i in range(0,len(b),temp)]
# c = [c[i:i+temp] for i in range(0,len(b),temp)]
# # b = b.split(b',')
# c = c.split(b',')
print("The smallest number is:",inList[0])
print("The largest number is:",inList[n-1])
print(inList)