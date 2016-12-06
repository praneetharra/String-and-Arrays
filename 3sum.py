def threeSum(nums):
    result = []
    d = {}
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            d[(i,j)] = [nums[i]+nums[j],i,j] #[sum, index i, index j] to make sure value at an index is not used second time in the sum
            
    for i in range(len(nums)):
        for j in d:
            if i not in d[j][1:] and nums[i]+d[j][0] == 0:
                pair3 = sorted([nums[i], nums[d[j][1]], nums[d[j][2]]])
                if pair3 not in result:
                    result.append(pair3)
    return result
    
threeSum([-1, 0, 1, 2, -1, -4])
