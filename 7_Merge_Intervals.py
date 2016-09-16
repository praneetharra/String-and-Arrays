l = [[1,3],[2,6],[8,10],[15,18]]
l.sort()

for i in range(len(l)):
    if i+1 == len(l):
        break
    elif l[i][1] >= l[i+1][0]:
        l[i+1][0] = l[i][0]
        l[i] = []
res = []
for i in l:
    if i != []:
        res.append(i)
print(res)
