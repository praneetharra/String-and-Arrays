def iso(a,b):
    c = {}
    #check length
    if len(a) != len(b):
        return False
        
    for i in range(len(a)):
        
        #if the key exisits
        if a[i] in c:
            #not 
            if c[a[i]] != b[i]:
                return False
                
        #doesn't exist in hashmap
        else:
            #add key value pair
            c[a[i]] = b[i]
    
    return True
    
def iso_final(a,b):
    if iso(a,b) and iso(b,a):
        return True
    else:
        return False

a = 'google'
b = 'baabee'
c = [i for i in a]
d = [i for i in a]
iso_final(a,b)
