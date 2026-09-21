"""
first non recursive char


set s as leetcode

repeat s for each char from s
    check if count(char) == 1
        print(char) then exit
else
    print(-1)


"""
"""
s="leetcode"

for ch in s:
    if s.count(ch) == 1:
        print(s.find(ch))
        break
else:
    print(-1)"""


s="leetcode"

for ch in s:
    if s.count(ch)==1:
        print(s.find(ch))
        break
    else:
        print(-1)