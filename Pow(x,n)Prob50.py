x = 8.05371
n = -1


def splitmultiplyrecursive(x, n, isodd):
    # Start the split computation
    if n == 2:
        return x * x
    else:
        # Check in n is odd or even
        if not isodd:
            halfproduct = splitmultiplyrecursive(x, n / 2, bool((n/2) % 2))
            return halfproduct * halfproduct
        else:
            product = splitmultiplyrecursive(x, n - 1, bool((n/2) % 2))
            return product * x


if n > 2147483647 or n < -2147483648:
    print(0)
elif n == 0:
    print(1)

# Special cases of x
    if x == 1:
        print(1)
    elif x == 0:
        print(0)

# Check if n is negative
if n < 0:
    isNegative = True
else:
    isNegative = False

# Check if n is odd
if n % 2 == 0:
    isOdd = False
else:
    isOdd = True

if isNegative:
    print(1/(splitmultiplyrecursive(x, -n, isOdd)))
else:
    print(splitmultiplyrecursive(x, n, isOdd))

