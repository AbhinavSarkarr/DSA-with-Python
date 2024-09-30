def last_occurence(nums, target):
    s, e = 0, len(nums) - 1
    index = -1
    while(s<=e):
        mid = (s+e)//2
        if(nums[mid]<target):
            s = mid+1
        elif(nums[mid]==target):
            index = mid 
            s = mid+1
        else:
            e = mid-1
    return index
    

print(last_occurence([1,2,3,4,5,5,5,5,5,6,7,8,9], 5))
