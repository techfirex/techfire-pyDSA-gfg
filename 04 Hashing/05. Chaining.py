# hash(key) = key % 7
# keys = 50,21,58,17,15,49,56,22,23,25

# for more understanding watch video for above example hashtable

# ==================================
# Hashtable (here, Array of Linked List Headers)
# 0   21 --> 49 --> 56
# 1   50 --> 15 --> 22
# 2   58 --> 23
# 3   17
# 4   25
# 5
# 6

# =================================
# Performance
# m = No. of Slots in Hash Table
# n = No. of Keys to be Inserted
# load factor (alpha) = n/m
# expected chain length = 

# worst case O(n) - every keys goes into same slot

# average case O(1) - we dont know how it would be, so we made assumptions that all the keys are uniformly distributed. 
# in this case,
# Expected Chain Length = load factor (Alpha)
# Expected Time to Search = O(1 + Alpha) 
# Expected Time to Insert/Delete = O(1 + Alpha) 
# // 1 for hash function computation and alpha for chain length

# =================================
# hashtable is small, load factor is big then you have "more collision".


# ===================================
# Data Structure for Store Chains
#     1. Linked List 
#     Time Complexity = (Search O(l), Delete O(l), Insert O(l))
#     Demerits //LL is not Cache Friendly, Use extra space for storing next refrences/pointers 
    
#     2. Dynamic Sized Arrays (Vectors in C++, ArrayList in JAVA, List in Python)
#     Time Complexity = (Search O(l), Delete O(l), Insert O(l))
#     Merit // Cache Friendly 

#     3. Self Balancing BST (AVL Tree, RedBlack Tree)
#     Time Complexity = (Search O(logl), Delete O(logl), Insert O(logl))
#     Demerit // Not Cache Friendly