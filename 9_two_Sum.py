inpt = [2, 7, 11, 15]
trgt = 9
res = []

for i in inpt:
    if trgt-i in inpt:
        res.append([inpt.index(i),inpt.index(trgt-i)])

return res
        
#runs in O(n)
