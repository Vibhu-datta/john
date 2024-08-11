def myfunc(*args):
    list=[]
    for n in *args:
        if n % 2 == 0:
            list.append(n)
    else pass
    return list