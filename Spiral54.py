matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

m = len(matrix)
n = len(matrix[0])
total = m * n
totalCountIndex = 0
maxIncj = n - 1
maxInci = m - 1
i = 0
j = 0
mainIterator = 0
returnList = []

while totalCountIndex < total:
    if mainIterator % 2 == 0:
        steps = 0
        while steps <= maxIncj:
            if mainIterator % 4 == 0:
                returnList.append(matrix[i][j])
                if j < n - 1:
                    j = j + 1
            else:
                if j > 0:
                    j = j - 1
                returnList.append(matrix[i][j])
            steps = steps + 1
        if mainIterator % 4 == 0 and mainIterator != 0:
            maxIncj = maxIncj - 1
        totalCountIndex = totalCountIndex + maxIncj + 1
        steps = 0

    else:
        stepsi = 0
        while stepsi <= maxInci:
            if ((mainIterator - 1) % 4 == 0):
                if i < n - 1:
                    i = i + 1
                    returnList.append(matrix[i][j])
            else:
                if i > 0:
                    i = i - 1
                    returnList.append(matrix[i][j])
            stepsi = stepsi + 1
        stepsi = 0
        totalCountIndex = totalCountIndex + maxInci
        maxInci = maxInci - 1
    mainIterator = mainIterator + 1
print(returnList)




