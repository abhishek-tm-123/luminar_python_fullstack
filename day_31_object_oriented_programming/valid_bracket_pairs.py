string = input("enter string :")
brackets = {"{":"}","(":")","[":"]"}
stack=[]
is_valid = True
for ch in string:
    if ch in brackets.keys():
        stack.append(ch)
    elif ch in brackets.values():
        if brackets[stack.pop()] == ch:
            pass
        else:
            is_valid = False
            break

if is_valid:
    print("valid")
else:
    print("not valid")