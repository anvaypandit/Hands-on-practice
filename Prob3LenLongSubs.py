s = 'dvdf'
buffList = []
lenLongSubString = 0
currSubLength = 0

for char in s:
    if char not in buffList:
        buffList.append(char)
        currSubLength = currSubLength + 1
    else:
        buffList.clear()
        currSubLength = 1
    if currSubLength > lenLongSubString:
        lenLongSubString = currSubLength


print(lenLongSubString)
