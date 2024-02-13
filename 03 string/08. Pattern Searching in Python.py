txt1 = "geeks for geeks"
txt2 = "AAAAA"

pos = txt1.find("geeks")
while pos >= 0:
    print(pos)
    pos = txt1.find("geeks",pos+1)

# --------------------------------------------------    

txt = input("Enter Text: ")
pat = input("Enter Pat: ")

pos = txt.find(pat)
while pos >= 0: # if pat not matched then find will return -1 so loop breaks there
    print(pos)
    pos = txt.find(pat, pos+1)