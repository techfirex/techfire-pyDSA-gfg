l1 = [10,20,30,40]
l2 = [1,2,3]

# Using Direct Method
# 1. slicing
l1 = l1[1:] + l1[0:1]
print(l1)

# 2. using append and pop
l2.append(l2.pop(0))
print(l2)


# using own method
def rotateByOne(l):
    n = len(l)
    x = l[0]
    for i in range(1,n):
        l[i-1] = l[i]
    l[n-1] = x

l5 = [10,20,30,40]
rotateByOne(l5)
print(l5)