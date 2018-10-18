num = [1,2,3]

def helper(numset,start):
    if len(numset) == 2:
        return [[numset[0],numset[1]],[numset[1],numset[0]]]

    baseperm = helper(numset[:(start+1)],start + 1)
    resultSet = [[]]
    for eachnumber in num:
        for eachbaseperm in baseperm:
            appendperm = eachnumber + eachbaseperm
            resultSet.append(appendperm)



