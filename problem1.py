def calc_max(c):
    if len(c)==2:
        if c[0]>c[1]:
            return c[0]
        else:
            return c[1]
    else:
        if calc_max(c[:-1])<c[-1]:
            return c[-1]
        else:
            return calc_max(c[:-1])

l=[3,5,2,6,4,1,8]
print(calc_max(l))