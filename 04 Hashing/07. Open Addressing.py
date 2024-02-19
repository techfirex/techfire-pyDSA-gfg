# Open Addressing
# Condition: No. of Slots in Hash Table >= No. of Keys to be Inserted

# ==========================================
# Cache Friendly, Use Single Array only (Not to use chains of any data structure)
# Three ways to do...
# a. Linear Probing
#     hash(key) = key % 7 // normal we do
#     hash(key, i) = (h(key) + i) % m
# b. Quadratic Probing 
# c. Double Hashing

# ===========================================
# example of linear probing // linearly search for next empty slot when there is a collision.

# hash(key) = key % 7
# key = [50,51,49,16,56,15,19]

# 0   49   
# 1   50
# 2   51
# 3   16
# 4   56
# 5   15
# 6   19 

# =========================================
# second example: linearly search in circular manner if end slots are occupied then start from 0 to search
# key = [48,42,50,55,53]

# 0   42
# 1   50
# 2   55
# 3
# 4   53
# 5
# 6   48

# ============================================
# How to Handle Deletion in Open Addressing?

# for delete we have to know how to search...

# linearly search for key
# circular search for key
# stop if key matched
# stop if empty slot comes - key not found 
# stop if you complete one circular search and comes at your start position and key not matched - key not found // case when all slots are filled but value not present // simply traverse whole hash table

# search algorithm:
# we compute hash function
# we go to that index and compare
# if we find, we return True. 
# Otherwise we linearly search.
# we stop when one of the three cases are arrived.
# 1. empty slot
# 2. key found
# 3. traverse through whole table

# ===========================================
# Now lets see about deletetion...
# problem with simply making  slot empty when we delete
# - search becomes fail
# solution - mark it as deleted so search does not fail for further

# =========================================
# Clustering (A Problem with Linear Probing)
# this cluster impact in open addressing
# cluster suppose is "k"
# insert new and it will map same then cluster becomes "k+1"

# ==========================================
# How to Handle Clustering problem with Linear Probing // here primary clutering
# 1. Quadratic Probing
#     hash(key, i) = (h(key) + l^2) % m
#     - clustering is still there
#     - like secondary cluster
#     - it does not find empty slot even if there are empty slots - problem in QP
#     - works better when - it will find empty slot when alpha < 0.5 and m is prime, so we have to  double the table size
# 2. Double Hashing
#     hash(key,i) = (h1(key) + i*h2(key)) % m
