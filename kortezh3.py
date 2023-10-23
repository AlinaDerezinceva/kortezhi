def sieve(tpl):
    x = []
    [x.append(item) for item in reversed(tpl) if item not in x]
    return tuple(x)
print(sieve([4, 7, 5, 6, 3, 4]))
print(sieve([4, 6, 5, 7, 3, 2, 5, 4, 8, 3]))
print(sieve((1, 2, 3, 4, 5, 6, 7, 2, 4, 5)))