#I/P: arr, target
#O/P: index of the target num else -1


check_list = [1,23,45,70]

def linear_search(given_list, target):
    for i in range(len(check_list)):
        if check_list[i] == target:
            return i
    return -1
    

print(linear_search(check_list, 45))