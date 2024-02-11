l = [8,100,20,40,3,7]
x = 10
nl = []
def smaller(l,x): 
    for i in l:
        if i < x:
            nl.append(i)
    return nl

smaller(l,x)
print(nl)


def getsmaller(l,x):
    return [i for i in l if i < x]

l = [0, 2, 4, 6, 8, 10]
x = 8
print(getsmaller(l,x))