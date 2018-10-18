def helper(n):
    if n == 1:
        return "1"
    else:
        prev = helper(n - 1)
        count = 1
        nextnumstring = ""

        for index in range(1, len(prev)):
            if prev[index - 1] == prev[index]:
                count = count + 1
            else:
                nextnumstring = nextnumstring + str(count) + prev[index - 1]
                count = 1


        nextnumstring = nextnumstring + str(count) + prev[len(prev)-1]

    return nextnumstring


print(helper(6))
