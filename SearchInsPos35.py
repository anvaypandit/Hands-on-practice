nums = [1,3,6,7,9,11,12,18,19]
target = 8

left = 0
right = len(nums)
rtindex = -1

while(left < right):
    if nums[left] == target:
        rtindex = left + 1
        break
    if nums[right] == target:
        rtindex = right - 1
        break
    mid = int((left + right)/2)
    if nums[mid] == target:
        right = mid + 1
        break

    if target < nums[mid]:
        right = mid - 1
    elif target > nums[mid]:
        left = mid + 1

print(left + 1 )