l = [20,12,40,30,60,10]

n = len(l)
count = 0

for i in range(1, n):
    key = l[i]
    j = i - 1
    while j >= 0 and key < l[j]:
        count +=1
        l[j+1] = l[j]
        j = j - 1
    l[j + 1] = key

print(l)
print(count)


