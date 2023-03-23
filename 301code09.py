A = int(input("Enter a value for A: "))
B = int(input("Enter a value for B: "))

# if statement using the equals conditional
if A == B:
    print("A is equal to B")

# if statement using the less than conditional
if A < B:
    print("A is less than B")

# if statement using the greater than or equal to conditional and elif keyword
if A >= B:
    print("A is greater than or equal to B")
elif A != B:
    print("A is not equal to B")

# if statement using both elif and else
if A > B:
    print("A is greater than B")
elif A < B:
    print("A is less than B")
else:
    print("A is equal to B")
