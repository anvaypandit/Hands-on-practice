nums = [4,5,6,7,0,1,2]
left = 0
right = len(nums) - 1
target = 3
rtindex = -1

while(left <= right):
    if nums[left] == target:
        rtindex = left
        break

    if nums[right] == target:
        rtindex = right
        break

    mid = int((left + right)/2)
    if nums[mid] == target:
        rtindex = mid
        break

    # Check in which part it is and adjust left and right accordingly
    if (target > nums[mid] and target < nums[right]):
        left = mid + 1
    elif (target < nums[mid] and target > nums[left]):
        right = mid - 1
    elif target > nums[left]:
        left = left + 1
    elif target < nums[right]:
        right = right - 1



print(rtindex)