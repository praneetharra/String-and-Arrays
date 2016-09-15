#using operator module
import operator
ops = {'+':operator.add, '-':operator.sub, '*' : operator.mul, '/' : operator.div}

def reverse_polish(in_list):
    res = 0
    i = 0
    while i < len(in_list):
        if in_list[i] in ['+','-', '*', '/']:
            ind_op = in_list.index(in_list[i])
            res = ops[in_list[i]](float(in_list[ind_op-2]),float(in_list[ind_op-1]))
            in_list[ind_op-2] = res
            i = ind_op-2 
            del in_list[ind_op]
            del in_list[ind_op-1]
            
        else:
            i = i+1
                
    return in_list[0]
    

a = ["4", "13", "5", "/", "+"]
reverse_polish(a)

#*************************************************************************************************************

#Without using operator module
def reverse_polish(in_list):
    res = 0
    i = 0
    while i < len(in_list):
        if in_list[i] in ['+','-', '*', '/']:
            if in_list[i] == '+':
                ind_op = in_list.index(in_list[i])
                res = float(in_list[ind_op-2]) + float(in_list[ind_op-1])
                in_list[ind_op-2] = res
                i = ind_op-2 
                del in_list[ind_op]
                del in_list[ind_op-1]
                
            elif in_list[i] == '-':
                ind_op = in_list.index(in_list[i])
                res = float(in_list[ind_op-2]) - float(in_list[ind_op-1])
                in_list[ind_op-2] = res
                i = ind_op-2 
                del in_list[ind_op]
                del in_list[ind_op-1]
                
            elif in_list[i] == '*':
                ind_op = in_list.index(in_list[i])
                res = float(in_list[ind_op-2]) * float(in_list[ind_op-1])
                in_list[ind_op-2] = res
                i = ind_op-2 
                del in_list[ind_op]
                del in_list[ind_op-1]
                
            else:
                ind_op = in_list.index(in_list[i])
                res = float(in_list[ind_op-2]) / float(in_list[ind_op-1])
                in_list[ind_op-2] = res
                i = ind_op-2 
                del in_list[ind_op]
                del in_list[ind_op-1]
        else:
            i = i+1
                
    return in_list[0]
    

a = ["4", "13", "5", "/", "+"]
reverse_polish(a)
