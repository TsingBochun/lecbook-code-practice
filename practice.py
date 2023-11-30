# The second, sum_cubes, computes the sum of the cubes of natural numbers up to n.
def sum_cubes(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + k*k*k, k + 1
        return total

print(sum_cubes(100))