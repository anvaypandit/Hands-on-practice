#s = "(()"
s = "(()"

stack = [-1]
maxCount = 0
count = 0
for index, para in enumerate(s):
    if para == '(':
        stack.append(index)
    else:
        try:
            stack.pop()
            count = index - stack[0]
            if count > maxCount:
                maxCount = count
        except IndexError:
            stack.append(index)
            continue

print(maxCount)



