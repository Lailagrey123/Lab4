def middle(a, b, c):

    if a<b and b<c:
        return b
    elif a>b and b>c:
        return b
    elif b>a and a>c:
        return a
    elif b>a and a<c:
        return a
    else:
        return c
    
