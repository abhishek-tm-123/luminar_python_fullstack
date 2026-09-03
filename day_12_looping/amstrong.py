num = int(input("Enter a number: "))
digit_count = len(str(num))
result = 0
while num !=0:
    digit = num % 10
    exponent = digit ** digit_count
    result = result + exponent
    
    num //= 10

print(result)