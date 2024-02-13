arr1 = [10, 5, 8, 20]
arr2 = [20, 10, 20, 8, 12]
arr3 = [10, 10, 10]
arr4 = [5, 20, 12, 10, 20, 10, 12]

# -------------------------------------------- Time complexity O(n) / linear
# naive solution (two traversals)

def getSecMax(l):
    if len(l) <= 1:
        return None

    lar = getmax(l)
    slar = None

    for i in l:
        if i != lar:
            if slar == None:
                slar = i
            else:
                slar = max(slar, i)
    return slar

def getmax(l):
    res = l[0]
    for i in range(len(l)):
        res = max(res, l[i])
    return res

# print(getSecMax(arr1))
# print(getSecMax(arr2))
# print(getSecMax(arr3))
# print(getSecMax(arr4))


# -------------------------------------------- Time complexity O(n) / linear
# efficient solution (one traversals)
arr5 = [5, 12, 15, 20, 20, 15, 18]


def getSecMax2(l):
    if len(l) <= 1:
        return None

    lar = l[0]
    slar = None

    for x in l[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x:
                slar = x
    return slar

print(getSecMax2(arr5))