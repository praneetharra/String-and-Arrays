inpt = [-1, 2, 1, -4] 
trgt = 1
res = sum([abs(i) for i in inpt])

inpt.sort()

for i in range(len(inpt)):
    if i+2==len(inpt):
        break
    elif abs(inpt[i]+inpt[i+1]+inpt[i+2] - trgt)<res:
        res = abs(inpt[i]+inpt[i+1]+inpt[i+2] - trgt)

print(res)

#O(nlogn)
