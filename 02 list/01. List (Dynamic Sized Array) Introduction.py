l = [10,20,30,40,50]

print(l)
print(l[3])
print(l[-1])
print(l[-2])


l.append(30)
print(l)

l.insert(1,15)
print(l)

print(15 in l)

print(l.count(30))
print(l.index(30))

# [10, 15, 20, 30, 40, 50, 30]
print(l.index(30,4,7))

# ------------------------------------------------------
l2 = [10, 15, 20, 30, 40, 50, 60, 70, 80]

l2.remove(20)
print(l2)

print(l2.pop(1))
print(l2.pop(2))
print(l2)

del l2[1]
print(l2)

del l2[0:2]
print(l2)

# --------------------------------------------------------
l3 = [10, 40, 20, 50]
print(max(l3))
print(min(l3))
print(sum(l3))

l3.reverse()
print(l3)

l3.sort()
print(l3)

