list=[1,2,3,4,5,6,7,8,90,10]
sorted=False
for i in range(len(list)-1):
    if(list[i]>list[i+1]):
        sorted=False
        break
    else:
        sorted=True
if(sorted):
    print("The list is sorted.")
else:
    print("The list is not sorted.")
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    print("Sorted list is:", list)
