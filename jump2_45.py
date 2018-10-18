nums = [2, 3, 1, 1, 4]
preexistingpath = {}

def pathdfs(start):
    if start in preexistingpath.keys():
        return preexistingpath[start]

    minJumpcount = 9223372036854775807
    for jumpindex in range(min(nums[start],(len(nums) - 1 - start)), 0, -1):
        jumpcount = pathdfs(start + jumpindex)
        if jumpcount != -1:
            if jumpcount < minJumpcount:
                minJumpcount = jumpcount

    if minJumpcount != 9223372036854775807:
        preexistingpath[start] = minJumpcount + 1
    return minJumpcount + 1


preexistingpath[len(nums) - 1] = 0
print(pathdfs(0))

