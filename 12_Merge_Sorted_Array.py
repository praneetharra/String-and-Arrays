a = [1,4,6,7,9,13,14,15,16]
b = [2,3,4,5,8,10]
c = []


i = 0
j = 0
while (i+j)<len(a)+len(b):
    if i == len(a):
        c.append(b[j])
        j = j+1
    elif j == len(b):
        c.append(a[i])
        i = i+1
    elif a[i]<=b[j]:
        c.append(a[i])
        i = i+1
    else:
        c.append(b[j])
        j = j+1

print(c)

#O(m+n)
