# l=[20,12,40,25]
# n=len(l)
# print(l)
# for i in range(n-1):
#     min_index=i
#     for j in range(i+1,n):
#         if l[j]<l[min_index]:
#             min_index=j
#     l[i],l[min_index]=l[min_index],l[i]
# print(l)


l = [20,12,40,25]

n = len(l)

for i in range(n-1):
    minindex = i
    for j in range(i+1, n):
        if l[j] < l[minindex]:
            minindex = j
    l[i], l[minindex] = l[minindex], l[i]

print(l)
