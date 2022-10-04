n = int(input("Check this number: "))
factors = []
if n <= 1:
    print(f"Check this number: It's a prime number.")
else:
    for factor in range(2, n):
        if n % factor == 0:
            factors.append(factor)
    if len(factors) == 0:
        print(f"It's a prime number.")
    else:
        print(f"It's not a prime number.")