l1 = [10,5,20,8]
l2 = [30,30,20]
l3 = [40]
l4 = [10,20,5,50]

# --------------------------------------------------
# simple solution
# print(max(l))

# -------------------------------------------- Time complexity O(n2) / quadrtic
def getmax(l):
    for x in l:
        for y in l:
            if y > x:
                break
        else:
            return x
    return None

print(getmax(l1))
print(getmax(l2))
print(getmax(l3))
print(getmax(l4))

# -------------------------------------------- Time complexity O(n) / linear 
def getmax2(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(len(l)):
            if l[i] > res:
                res = l[i]
        return res

print(getmax2(l1))
print(getmax2(l2))
print(getmax2(l3))
print(getmax2(l4))


