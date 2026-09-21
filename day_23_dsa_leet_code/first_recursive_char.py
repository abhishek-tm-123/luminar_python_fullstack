"""
First recursive char in a string

step1: set s as leetcode
step2: set a list as lst
step3: repeat for each char in s 
    step4: check if char not in lst then
        step5: append char to lst
    else: display char 
          break


"""


s = "leetcode"

lst = []

for char in s :

    if char not in lst:
        lst.append(char)
    else:
        print("first recursive char",char)
        break
