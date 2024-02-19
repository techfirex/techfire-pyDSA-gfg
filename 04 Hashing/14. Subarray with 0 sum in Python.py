# l = [1,4,13,-3,-10,5]
# op - True
# l = [-1,4,-3,5,1]
# op - True
# l = [3,1,-2,5,6]
# op - False
# l = [5,6,0,8]
# op - True

# ==============================
# Naive Solution: Time Complexity O(n2)
# def isZeroSum(l):
#     n = len(l)
#     for i in range(n):
#         for j in range(i+1, n+1):
#             if sum(l[i:j]) == 0:
#                 return True
#     return False

# l = [4,3,-2,1,1]
# print(isZeroSum(l))

# ====================================
# Efficient Solution: Time Complexity O(n) // linear time
# Idea: Use Prefix Sum and Hashing // see video
# if sum of a[i:j] is 0, the pre_sum1 must be same as pre_sum2
def isZeroSum2(l):
    pre_sum = 0
    h = set()

    for i in range(len(l)):
        pre_sum += l[i]
        if pre_sum == 0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False

l = [4,3,-2,1,1]
l2 = [3,-2,-1]
print(isZeroSum2(l2))