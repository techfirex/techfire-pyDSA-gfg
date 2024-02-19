# s = "geek"
# op - False
# s = "geegg"
# op - True
# s = "abccbabb"
# op - True

# =======================
# Naive Solution // Time Complexity O(n!*n)

# ===============================
# Effiecient Solution // Time Complexity theta(n) // Linear Time
# Answer is going to True if there is at most one character with odd frequency
# like acbccab - c is in odd frequency // aaaabbbbddd - d is in odd frequency
# so it is palindrome

# else False means not palindrome
# like abcc - a and b two have odd frequency // ab - both odd // aaabbcdd - a and c odd

# use counter from collection module 
# counter is subclass of dict
# so it has all the feature of dict
# it is specifically designed for counting purpose
# pass list or str and it will give one line dict object with freq
# ex: 
# s = "geeksforgeeks"
# cnt = Counter({"g":2, "e":4, "k":2, "s":2})

# ==================code
from collections import Counter
def pelper(s):
    cnt = Counter(s)
    odd = 0

    for freq in cnt.values():
        if freq % 2 != 0:
            odd = odd + 1
            if odd > 1:
                return False
    return True

s = "geeksgeeks"
print(pelper(s))