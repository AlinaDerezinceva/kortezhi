A = 0
B = -1
def slicer(x, y):
    C = D = A   
    if y in x:
        C = x.index(y)
    if x.count(y) > 1:
        D = x.index(y, C + 1) + 1
    else:
        D = B
    return x[C:D]
print(slicer((1, 2, 3), 7))
print(slicer((4, 5, 2, 6, 4, 4, 5, 1), 10))
print(slicer((4, 6, 2, 4, 7, 2), 6))