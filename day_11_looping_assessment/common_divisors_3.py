num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
smallest = min(num1,num2,num3)
for i in range(1,smallest+1):
    if num1%i==0 and num2%i==0 and num3%i==0:
        print(i)