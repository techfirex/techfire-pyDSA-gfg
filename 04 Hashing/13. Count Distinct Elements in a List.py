# l = [10,20,10,30,30,20]
# op - 3
# l = [10,10,10]
# op - 1
# l = [10,20,30]
# op - 3

# ========================
# Method 1 - simple

# l = [10,20,10,30,30,20]

# def countDistict(l):
#     res = 1
#     for i in range(1,len(l)):
#         if l[i] not in l[0:i]:
#             res = res + 1
#     return res

# print(countDistict(l))


# ========================
# Method 2 - using set // efficient
# def countDistict2(l):
#     s = set(l)
#     return len(s)

# l = [10,20,10,30,30,20]
# print(countDistict2(l))

# =========================
# short code
def countDistict3(l):
    return len(set(l))

l = [10,20,10,30,30,20]
print(countDistict3(l))