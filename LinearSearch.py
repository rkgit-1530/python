list=[]
length=int(input("Enter the Length of the list: "))
for i in range(length):
    num=int(input(f"Enter Number {i+1}:"))
    list.append(num)
print(list)
target=int(input("Enter a Target: "))
for i in range(len(list)):
    if target==list[i]:
        print("Target Found at index ",i)
        break
else:
    print("Not Found")
