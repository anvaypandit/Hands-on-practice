def revNum(i,nums):
    j = len(nums) - 1
    while i < j:
        (nums[i], nums[j]) = (nums[j], nums[i])
        i = i + 1
        j = j - 1

nums = [1,5,1]

if len(nums) == 0 or len(nums) == 1:
    print(nums)

i = len(nums) - 1
while i > 0:
    if nums[i] <= nums[i-1]:
        i = i - 1
        continue
    else:
        j = i
        #Find the correct non-decreasing position
        while j < len(nums):
            if nums[j] > nums[i-1]:
                j = j + 1
                continue
            else:
                (nums[i-1],nums[j-1]) = (nums[j-1],nums[i-1])
                revNum(i,nums)
            break
    if j == len(nums):
        (nums[i - 1], nums[j - 1]) = (nums[j - 1], nums[i - 1])
        revNum(i, nums)
    break

if(i == 0):
    revNum(nums)
    print(nums)
else:
    print(nums)


