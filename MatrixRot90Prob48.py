matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

# Get the shape of matrix

n = len(matrix)

# Row exchanges
i = 0
j = n - 1

while i < j:
    for k in range(n):
        (matrix[i][k], matrix[j][k]) = (matrix[j][k], matrix[i][k])
    i = i + 1
    j = j - 1

print(matrix)

# Transpose the exchanged matrix
i = 0
k = 0
while i < n:
    for k in range(i, n):
        (matrix[i][k], matrix[k][i]) = (matrix[k][i], matrix[i][k])
    i = i + 1

print(matrix)


