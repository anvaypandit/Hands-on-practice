a = "248298492184091284901284902184092184092184092184092810948219048210984"

# The product of first 20
prodFirstTwenty = 1
for num in a:
    if num == '0':
        prodFirstTwenty = 0
        break
    prodFirstTwenty *= int(num)

# adjacent products