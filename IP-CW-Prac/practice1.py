def sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print(sum(4))

def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sum_list([7,2,4]))

def remove_adjacent(nums):
    if len(nums) > 0:
        comp = nums[0]
        for i in range(1,len(nums)):
            print(nums)
            curr = nums[i]
            if curr == comp:
                print(nums)
                nums.remove(i)
                comp = nums[i]
    return nums

print(remove_adjacent([5,3,3,7,9,1,1])) #why no work TT
