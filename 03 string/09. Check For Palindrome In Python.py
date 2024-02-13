# 10022001

s1 = "abba"
s2 = "abcba"
s3 = "geek"
s4 = "a"
s5 = "abA"

txt = input("Enter Text: ")

low = 0
high = len(txt) - 1

while low < high:
    if txt[low] != txt[high]:
        print("No")
        break
    low = low + 1
    high = high - 1
else:
    print("yes")


# Using slicing
if s1 == s1[::-1]:
    print("yes")
else:
    print("No")