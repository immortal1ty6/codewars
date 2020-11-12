def abbrev_name(name):
    name1, name2 = name.upper().split(' ')
    a = name1[0]
    b = name2[0]
    return '{}.{}'.format(a,b)
