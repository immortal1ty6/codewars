def fake_bin(x):
    a = list(x)
    newA = []
    for b in x:
        if int(b) <5:
            newA.append("0")
        else:
            newA.append("1")
    return "".join(newA)
