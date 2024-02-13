l1 = [10,20,30,40]
l2 = ["geeks", "ide", "courses"]

# Using Library / Direct Methods
# 1. reverse
l3 = [10,20,30,40]
l3.reverse()
print(l3)

# 2. reversed()
l4 = [10,20,30,40]
new_l = list(reversed(l4))
print(new_l)

# 3. slicing
l5 = [10,20,30,40]
new_l2 = l5[::-1]
print(new_l2)

# 4. while loop and pop
list1 = []
i = 0
while i < len(l2):
    items = l2.pop()
    list1.append(items)
# print(list1)

# 5. for loop and pop
for i in range(len(l1)):
    items = l1.pop()
    list1.append(items)
# print(list1)

# Using own method
def reverseList(l):
    s = 0
    e = len(l) - 1

    while s < e:
        l[s], l[e] = l[e], l[s]
        s = s + 1
        e = e - 1

l6 = [10,20,30,40]
reverseList(l6)
print(l6)