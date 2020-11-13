def points(games):
    result = 0
    for a in games:
        b = a.split(':')
        if b[0]>b[1]:
            result += 3
        elif b[0]==b[1]:
            result += 1
    return result
