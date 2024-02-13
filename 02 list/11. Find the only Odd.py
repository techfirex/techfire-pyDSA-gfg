l1 = [10,30,30,10,30,30,20]
l2 = [10,10,10,10,10,20,20]
l3 = [10,10,20,30,30,20,40]
l4 = [10]

# Method 1: Using Count Method
def findOdd(l):
    res = None
    for i in l:
        count = l.count(i)
        if count % 2 != 0:
            res = i
            break
    return res

print(findOdd(l1))
print(findOdd(l2))
print(findOdd(l3))



# Method 2: Using Bitwise XOR // efficient Method
def findOdd2(l):
    res = 0
    for i in l:
        res = res ^ i # XOR 
    return res

print(findOdd2(l1))
print(findOdd2(l2))
print(findOdd2(l3))