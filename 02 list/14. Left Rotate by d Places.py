l1 = [1,2,3,4,5]
l2 = [10,20,30,40]

# Using Direct Methods
# 1. Using Slicing
l1 = [1,2,3,4,5]
d = 2
l1 = l1[d:] + l1[:d]
print(l1)

# 2. Using Deque Method
from collections import deque
l4 = [10,20,30,40,50]
d = 2
dq = deque(l4)
dq.rotate(-d)
l = list(dq)
print(l)

# Using own method
# 1. simple method using append and pop // O(n*d)
def leftRotate(l,d):
    for i in range(0,d):
        l.append(l.pop(0))

l5 = [10,20,30,40,50]
d = 3
leftRotate(l5,d)
print(l5)

# 2. O(n) Time and O(1) auxiliary space
def leftRotate2(l,d):
    n = len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)

def reverse(l,b,e):
    while b < e:
        l[b], l[e] = l[e], l[b]
        b = b + 1
        e = e - 1