def unique(string):
    res = " "
    for st in string:
        if st not in res:
            res = res + st
    return res

