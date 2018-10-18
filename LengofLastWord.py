s = "a"

length = len(s)
j = length - 1

# Incase there are unnecessary spaces in end
while j >= 0 and s[j] == ' ':
    j = j - 1

if j == -1:
    print(0)

# Count the last word till another space is encountered
start = j
while j >=0 and s[j] != ' ':
    j = j - 1
end = j

if j == -1:
    print(0)
else:
    # skip spaces and check if another word exists before
    while j >= 0 and s[j] == ' ':
        j = j - 1
    if j == -1:
        print(0)
    else:
        print(start - end)