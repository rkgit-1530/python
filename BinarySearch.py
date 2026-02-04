list=[]
length=int(input("Enter the Length of the list: "))
for i in range(length):
    num=int(input(f"Enter Number {i+1}:"))
    list.append(num)

print(list)
# isFound=False
low=0
high=length-1
target=int(input("Enter a Target: "))
Result=-1
while (low<=high):
    mid=(low+high)//2
    if list[mid]==target:
        Result=mid
        low=mid+1 # to find last occurrence
      #  high=mid-1  to find first occurrence
    elif(target<list[mid]):
        high=mid-1
    else:
        low=mid+1
print(Result)
# if(isFound):
#     print("Number Found")
# else:
#     print("Number not Found")
