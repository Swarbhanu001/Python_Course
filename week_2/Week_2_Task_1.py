L = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, L)))
print(result)