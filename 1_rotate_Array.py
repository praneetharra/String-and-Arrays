def rotateArray(in_list, step):
    temp = in_list[:step]
    output = in_list[step:]+temp
    return output


a = [1,2,3,4,5,6,7]
b = 3

rotateArray(a, b)
