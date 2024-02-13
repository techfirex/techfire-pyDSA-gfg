s1 = "listen"
s2 = "silent"

s3 = "aacb"
s4 = "acab"

s5 = "aab"
s6 = "abb"

# Naive Solution // Using Sorting // Time Complexity O(nlogn)

def areAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    return (s1 == s2)

print(areAnagram(s5,s6))


# Using own Method // Efficient Solution // Time Complexity O(n)
def areAnagram2(s1,s2):
    if len(s1) != len(s2):
        return False

    count = [0]*256

    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    
    for x in count:
        if x != 0:
            return False
    return True

print(areAnagram(s1,s2))