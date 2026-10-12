s = input("enter a string:")

stack=[]

for ch in s:
    if ch not in stack :
        stack.append(ch)
    else:
        stack.pop()

print(stack)
    