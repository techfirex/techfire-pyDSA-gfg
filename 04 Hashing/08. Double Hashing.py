# hash(key,i) = (h1(key) + i*h2(key)) % m

# If h2(key) is relatively prime to m , then it  always find a free slot it there is one.
# Distribute keys more uniformly than linear probing and quadratic probing
# No clustering

# ========================================
# example for double hashing
# key = [49,63,56,52,54,48]

# hash(key,i) = (h1(key) + i*h2(key)) % m 
# i value increase for 1st it will 1 (after 1st if slot is filled/means collision occurs then go for 2nd), 2nd time it will 2 ....

# m = 7
# h1(key) = key % 7
# h2(key) = 6 - (key % 7) // collisoin occurs then run this, it will never return 0

# 0   49
# 1   
# 2   54
# 3   63
# 4   56
# 5   52
# 6   48

# ==================================
# Why h2(key) and m should be relatively prime?

# suppose, h2(key) = 6
# (1*6) % 7 = 6
# (2*6) % 7 = 5
# (3*6) % 7 = 4
# (4*6) % 7 = 3
# (5*6) % 7 = 2
# (6*6) % 7 = 1

# ======================================
# Algorithm of Double Hashing

# void doubleHashingInsert(key)
# {
#     if (table if full)
#         return error;
    
#     probe = h1(key), offset = h2(key);
    
#     while (table[probe] is occupied)
#         probe = (probe + offset) % m;
    
#     table[probe] = key;
# }

# // in linear probing offset is 1

# ====================================
# Performance Analysis of Search
# it works like insert

# but if search is unsuccessful..

# alpha = n/m (should be <= 1)
# Assumption: Every probe sequence looks at a random location

# (1 - alpha) fraction of the table is empty

# expected no. of probe required = 1/(1 - alpha)

# suppose, alpha = 0.8 means 80% of table is occupied and 20% of table is empty
# so we need 1/5 trial means 5 trial for unsuccessful search

# if alpha = 0.9
# then expected no. of probe required = 10