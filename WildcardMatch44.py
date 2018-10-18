
s = "acdcb"
p = "a*cdcb"

# Two D array for Dp
memo = [[False for i in range(len(s)-1)] for j in range(len(p)-1)]

def isMatchHelper(s,p,i,j):

    match = False
    # Check for the match in case the pattern is not a wild char
    if p[j] != '*':
        if p[j] in [s[i], '?']:
            p[i][j] = True  
            isMatchHelper(s,p,i+1,j+1)
    else:
        # The code comes here when its the wild card *, then there are three possible subproblems
        restMatch = match and (s,p,i+1,j+1)
        if(!restMatch):
            restMatch = match and isMatchHelper(s,p,i,j+1)
        if(!restmatch):
            restMatch = match and isMatchHelper(s,p,i+1,j)
        return restMatch




