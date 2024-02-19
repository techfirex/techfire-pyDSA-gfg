# Hashing
# mainly used to impliment dictionary (where there is a key and value pairs)
# also used to impliment sets (where only keys there)
# it provides search, insert, delete operations in O(1) on average
# all the values are unique values (if key already exists and you insert it again then it will overwrite the previous key)
# delete operation is delete the key and its corresponding value

# watch video for comparing Hashing with other data structures like array, AVL tree, red black tree, binary tree etc along with its complexity
# For sorted array // three operations takes O(n) time
# For unsorted array // insert and delete takes O(1) time and search will take O(n)

# not useful for
# 1 finding the closest values
# 2 sorted data (for 1 and 2 case we used AVL tree, red black tree is best)
# 3 prefix searching (for that we use 'trie' data structure)