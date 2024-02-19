# Direct Address Table 
# It has problem for huge data

# Hashing
# universe of keys ----> Hash Func ----> Hash Table (Array of Table)
# here hash func do some magic and reduce huge data into small and then stored in table

# ==========================================
# How Hash Function Works?
# convert large keys to small values
# there are some requirement to make hash func like keys should generate same index on every func call

# should always map a large key to same small key
# should generate values from 0 to m-1
# should be fast, O(1) for integers and O(len) for string of lengh "len"
# should uniformly distribute large keys into hash table slots

# =====================================================
# Example of Hash Functions
# 1. h(large_key) = large_key % m

# 2. for strings, weighted sum
#     str[] = "abcd"
#     str[0] * x^0 + str[1] * x^1 + str[2] * x^2 + str[3] * x^4
#     then modulo division by m

# 3. Universal Hashing
#     you have group of hash functions and you choose randomly any hash function to hash the data
#     set of hash functions and then randomly choose any one hash function for data