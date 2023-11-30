# Using an identity function that returns its argument, 
# we can also sum natural numbers using exactly the same summation function.
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1    #注意这里最后相当于是把term代成了cube，相当于代入了函数，这个特性貌似是C语言中难以实现的。
    return total

def cube(x):
    return x*x*x

def identity(x):
    return x

def sum_cubes(n):
    return summation(n, cube)

def sum_naturals(n):
    return summation(n, identity)

# result = sum_cubes(3)
result = sum_naturals(10)

print(result)