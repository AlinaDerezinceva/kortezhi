def tpl_sort(abv):
    for element in abv:
        if not isinstance(element, int):
            return ()
        return tuple(sorted(abv))
print(tpl_sort((6, 3, 5.8, 2.4, 5)))
print(tpl_sort((3, 4.6, 2, 7, 1.3)))

    
