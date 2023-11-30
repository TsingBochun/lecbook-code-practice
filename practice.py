def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

sum_naturals(100)
print(sum_naturals(100))