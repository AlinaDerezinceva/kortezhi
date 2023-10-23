def del_from_tuple(tpl, x):
    lst = list(tpl)
    if x in tpl:
        lst.remove(x)
    return tuple(lst)
print(del_from_tuple((1, 4, 6), 5))
print(del_from_tuple((1, 2, 3, 5, 7), 8))
print(del_from_tuple((5, 4, 2, 7, 3, 6), 3))

