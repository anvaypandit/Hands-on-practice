board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

def validaterow(rowNumber):
    validationHash = [0, 0, 0, 0, 0, 0, 0, 0, 0,0]
    for number in board[rowNumber-1]:
        if number != '.':
            if validationHash[int(number)] == 1:
                return False
            else:
                validationHash[int(number)] = 1
    return True

def validatecolumn(columnNumber):
    validationHash = [0, 0, 0, 0, 0, 0, 0, 0, 0,0]
    for numIndex in range(9):
        if board[numIndex][columnNumber-1] != '.':
            if validationHash[int(board[numIndex][columnNumber-1])] == 1:
                return False
            else:
                validationHash[int(board[numIndex][columnNumber-1])] = 1
    return True

def validategrids(gridEndRowNumber):
    # Grid Part 1
    for gridnumber in range(3):
        validationHash = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for rowIndex in range(3):
            for columnIndex in range(3):
                calColumnIndex = gridEndRowNumber-columnIndex-1 +(3*gridnumber)
                calRowIndex = gridEndRowNumber-rowIndex-1 +(3*gridnumber)
                if board[calRowIndex][calColumnIndex] != '.':
                    if validationHash[int(board[calRowIndex][calColumnIndex])] == 1:
                        return False
                    else:
                        validationHash[int(board[calRowIndex][calColumnIndex])] = 1
    return True


for index in range(1,10):
    # Validate the row
    if not (validaterow(index) and validatecolumn(index)):
        print(False)
        break
    if index % 3 == 0:
        if not validategrids(index):
            print(False)
            break

print(True)



