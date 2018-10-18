nums = [1,2,3]
preexistingpath = {}

def pathdfs(start):
    canJump = False
    if start in preexistingpath.keys():
        return preexistingpath[start]

    for jumpindex in range(min(nums[start],(len(nums) - 1 - start)), 0, -1):
        canJump = pathdfs(start + jumpindex)
        if canJump:
            preexistingpath[start] = True
            return True

    preexistingpath[start] = canJump
    return canJump


preexistingpath[len(nums) - 1] = True
print(pathdfs(0))

