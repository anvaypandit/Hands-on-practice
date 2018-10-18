nums = [1,2,3]
target = 3

left = 0
right = len(nums) - 1
returnIndexes = [-1, -1]

if len(nums) == 1:
    if target == nums[0]:
        return [0, 0]
    else:
        return returnIndexes
if len(nums) == 2:
    if nums[0] == target:
        if nums[1] == target:
            return [0, 1]
        else:
            return [0, 0]
    elif nums[1] == target:
        return [1, 1]
    else:
        return returnIndexes

while (left < right):
    mid = int((left + right) / 2)
    if nums[mid] == target:
        returnIndexes[0] = mid
        returnIndexes[1] = mid
        break
    if mid == left:
        break
    elif target > nums[mid]:
        left = mid
    elif target < nums[mid]:
        right = mid

if -1 not in returnIndexes:
    left = mid
    right = mid
    while (left >= 0) or right < len(nums):
        if left >= 0:
            if nums[left] == target:
                left = left - 1
                continue
        if right < len(nums):
            if nums[right] == target:
                right = right + 1
                continue
        break
    returnIndexes[0] = left + 1
    returnIndexes[1] = right - 1

return returnIndexes