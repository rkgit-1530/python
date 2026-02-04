list=[22,11,33,4,55,66,7,88,9,0]
# length=int(input("Enter the Length of the list: "))
# for i in range(length):
#     num=int(input(f"Enter Number {i+1}:"))
#     list.append(num)
count=0
print("Unsorted list is: ",list)

for i in range(len(list)):
    for j in range(len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            count+=1
print("Number of swaps:",count)
print("Sorted List is:",list)