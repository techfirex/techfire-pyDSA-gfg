l = [10,41,30,15,80]

even = []
odd = []
# def seprate(l):
#     for i in l:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even, odd

# even,odd = seprate(l)
# print(even)
# print(odd)

def separate_comp(l):
    even = [i for i in l if i % 2 == 0]
    odd = [i for i in l if i % 2 != 0]
    return even, odd

even,odd = separate_comp(l)
print(even)
print(odd)