"""PYTHON WHILE LOOP â€“ BEGINNER PRACTICE ASSESSMENT
====================================================

Objective:
Practice while loops from the very beginning. These questions focus on:
- Starting a loop
- Writing the correct condition
- Updating/increasing/decreasing a variable
- Repeating until a condition becomes false
- Using if conditions inside while loops
- Basic counting and accumulation

Instructions:
1. Write a Python program for each question.
2. Use a while loop wherever specified.
3. Do not use for loops.
4. Pay special attention to the loop condition and variable update.
5. Test your program using the sample input.

----------------------------------------------------
SECTION A â€“ BASIC WHILE LOOP
----------------------------------------------------

1. Print Numbers from 1 to 10
Write a program to print numbers from 1 to 10 using a while loop.

Sample Input:
No input

Sample Output:
1
2
3
4
5
6
7
8
9
10

answer:

i=1
while i<=10:
    print(i)
    i=i+1 



2. Print Numbers from 1 to N
Ask the user to enter a number N and print all numbers from 1 to N.

Sample Input:
5

Sample Output:
1
2
3
4
5

answer:

n=int(input("enter a number:"))
i=1
while i<=n:
    print(i)
    i=i+1



3. Print Numbers from N to 1
Ask the user to enter a number N and print numbers from N down to 1.

Sample Input:
5

Sample Output:
5
4
3
2
1

answer:

n=int(input("enter a number:"))
i=n
while i>=1:
    print(i)
    i=i-1



4. Print Even Numbers from 1 to N
Ask the user to enter N and print all even numbers from 1 to N.

Sample Input:
10

Sample Output:
2
4
6
8
10

answer:

n=int(input("enter a number:"))
i=1
while i<=n:
    if i%2==0:print(i)
    i=i+1


5. Print Odd Numbers from 1 to N
Ask the user to enter N and print all odd numbers from 1 to N.

Sample Input:
10

Sample Output:
1
3
5
7
9

answer:


n=int(input("enter a number:"))
i=1
while i<=n:
    if i%2!=0:print(i)
    i=i+1



6. Print Multiples of 5
Ask the user to enter N and print multiples of 5 from 5 up to N.

Sample Input:
30

Sample Output:
5
10
15
20
25
30

answer:


n=int(input("enter a number:"))
i=5
while i<=n:
    print(i)
    i=i+5



7. Print Squares from 1 to N
Ask the user to enter N and print the square of every number from 1 to N.

Sample Input:
5

Sample Output:
1
4
9
16
25

answer:


n=int(input("enter a number:"))
i=1
while i<=n:
    print(i**2)
    i=i+1



8. Print Cubes from 1 to N
Ask the user to enter N and print the cube of every number from 1 to N.

Sample Input:
4

Sample Output:
1
8
27
64

answer:


n=int(input("enter a number:"))
i=1
while i<=n:
    print(i**3)
    i=i+1


----------------------------------------------------
SECTION B â€“ COUNTING AND TOTAL
----------------------------------------------------

9. Count from 1 to N
Ask the user to enter N and display the count of numbers from 1 to N.

Sample Input:
7

Sample Output:
Count = 7

answer:


n=int(input("enter number:"))
i=1
count=0
while i<=n:
    count=count+1
    i=i+1

print(count)



10. Find the Sum from 1 to N
Ask the user to enter N and calculate the sum of numbers from 1 to N.

Sample Input:
5

Sample Output:
Sum = 15

answer:

n=int(input("enter number:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1

print("sum =",sum)


11. Find the Sum of Even Numbers
Ask the user to enter N and find the sum of all even numbers from 1 to N.

Sample Input:
10

Sample Output:
Sum = 30

answer:

n=int(input("enter number:"))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1

print("sum =",sum)


12. Find the Sum of Odd Numbers
Ask the user to enter N and find the sum of all odd numbers from 1 to N.

Sample Input:
10

Sample Output:
Sum = 25

answer:

n=int(input("enter number:"))
i=1
sum=0
while i<=n:
    if i%2!=0:
        sum=sum+i
    i=i+1

print("sum =",sum)


13. Count Even and Odd Numbers
Ask the user to enter N. Count how many even and odd numbers exist between 1 and N.

Sample Input:
10

Sample Output:
Even Count = 5
Odd Count = 5


n=int(input("enter number :"))
even_count=0
odd_count=0
i=1

while i<=n:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
    i=i+1

print("Even count:",even_count)
print("Odd count:",odd_count)




14. Find the Product from 1 to N
Ask the user to enter N and calculate the product of all numbers from 1 to N.

Sample Input:
5

Sample Output:
Product = 120

answer:

n=int(input("enter number:"))
i=1
mul=1
while i<=n:
    mul=mul*i
    i=i+1

print("multiplication =",mul)


15. Find the Average from 1 to N
Ask the user to enter N and find the average of numbers from 1 to N.

Sample Input:
5

Sample Output:
Average = 3.0

answer:

n=int(input("enter number:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1

print("avg=",sum/n)



----------------------------------------------------
SECTION C â€“ USER INPUT WITH WHILE
----------------------------------------------------

16. Print a Number N Times
Ask the user to enter a number and how many times it should be printed.

Sample Input:
Number: 7
Times: 4

Sample Output:
7
7
7
7

answer:

n=int(input("enter number:"))
times=int(input("times:"))
i=1

while i<=times:
    print(n)
    i=i+1



17. Keep Asking Until Positive Number
Keep asking the user to enter a number until they enter a positive number.

Sample Input:
-5
0
-2
8

Sample Output:
Enter a positive number: -5
Enter a positive number: 0
Enter a positive number: -2
Enter a positive number: 8
Accepted

answer:


while True:

    num=int(input("enter positive number:"))
    if num>0:
        print("Accepted")
        break



18. Password Verification
Ask the user to enter a password. Keep asking until the correct password is entered.
Use the password: 1234

Sample Input:
1111
5555
1234

Sample Output:
Incorrect password
Incorrect password
Login successful

answer:


password_db=1234

while True:
    password=int(input("enter password:"))
    if password == password_db:
        print("login successful")
        break
    else:
        print("incorrect password")



19. Print Numbers Until Zero
Keep accepting numbers from the user. Stop when the user enters 0.

Sample Input:
5
8
3
0

Sample Output:
5
8
3
Program stopped

answer:

while True:
    num=int(input("enter number:"))
    if num==0:
        print("program stopped")
        break


20. Find Sum Until Zero
Keep accepting numbers from the user and calculate their sum. Stop when 0 is entered.

Sample Input:
10
20
5
0

Sample Output:
Sum = 35

answer:

sum=0
while True:
    num = int(input("enter number:"))
    sum=sum+num
    if num==0:
        print("sum =",sum)
        break



----------------------------------------------------
SECTION D â€“ DIGITS AND NUMBERS
----------------------------------------------------

21. Count the Digits of a Number
Ask the user to enter a positive integer and count how many digits it contains.

Sample Input:
58392

Sample Output:
Number of digits = 5

num = int(input("enter a number :"))

count=0

while num!=0:
    count+=1
    num=num//10

print("number of digits :",count)


22. Find the Sum of Digits
Ask the user to enter a number and find the sum of its digits.

Sample Input:
583

Sample Output:
Sum of digits = 16


num = int(input("enter a number :"))

sum=0

while num!=0:
    last_digit=num%10
    sum=sum+last_digit
    num=num//10

print("sum of digits :",sum)



23. Reverse a Number
Ask the user to enter a number and print its reverse.

Sample Input:
12345

Sample Output:
54321


num=int(input("enter a number:"))
rev=0
while num!=0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10

print("reverse:",rev)




24. Find the Largest Digit
Ask the user to enter a number and find the largest digit in it.

Sample Input:
58392

Sample Output:
Largest digit = 9

answer:


num = int(input("enter number :"))
largest=0
while num!=0:
    ld=num%10
    if ld>largest:
        largest=ld
    num=num//10
print("largest digit",largest)




25. Find the Smallest Digit
Ask the user to enter a number and find the smallest digit in it.

Sample Input:
58392

Sample Output:
Smallest digit = 2

num = int(input("enter number :"))
smallest=9
while num!=0:
    ld=num%10
    if ld<smallest:
        smallest=ld
    num=num//10
print("smallest digit",smallest)


26. Count Even Digits
Ask the user to enter a number and count how many of its digits are even.

Sample Input:
123456

Sample Output:
Even digits = 3

answer:

num = int(input("Enter number: "))

count = 0

while num != 0:
    ld = num % 10

    if ld % 2 == 0:
        count += 1

    num = num // 10

print("Even digits =", count)

----------------------------------------------------
SECTION E â€“ WHILE + IF CONDITIONS
----------------------------------------------------

27. Print Numbers Divisible by 3
Ask the user to enter N and print all numbers between 1 and N that are divisible by 3.

Sample Input:
15

Sample Output:
3
6
9
12
15

answer:

n = int(input("Enter number: "))

i = 1

while i <= n:
    if i % 3 == 0:
        print(i)
    i += 1


28. Count Numbers Divisible by 5
Ask the user to enter N and count how many numbers between 1 and N are divisible by 5.

Sample Input:
25

Sample Output:
Count = 5

answer:
n = int(input("Enter number: "))

i = 1
count = 0

while i <= n:
    if i % 5 == 0:
        count += 1
    i += 1

print("Count =", count)


29. Find the Largest Number Until 0
Keep accepting numbers from the user. Stop when 0 is entered and display the largest number entered.

Sample Input:
12
45
7
32
0

Sample Output:
Largest number = 45

answer:

num = int(input("Enter number: "))

largest = 0

while num != 0:
    if num > largest:
        largest = num

    num = int(input("Enter number: "))

print("Largest number =", largest)




30. Simple Number Guessing Loop
Store a secret number as 7. Ask the user to guess the number. Keep asking until the user enters the correct number.

Sample Input:
3
10
5
7

Sample Output:
Wrong guess
Wrong guess
Wrong guess
Correct! You guessed the number.

answer:

secret = 7

num = int(input("Guess the number: "))

while num != secret:
    print("Wrong guess")
    num = int(input("Guess the number: "))

print("Correct! You guessed the number.")

====================================================
BEGINNER CHECKLIST
====================================================

After completing all 30 questions, the student should be able to:

[ ] Create a while loop
[ ] Write a correct loop condition
[ ] Initialize a loop variable
[ ] Increase a variable inside a loop
[ ] Decrease a variable inside a loop
[ ] Stop a loop using a condition
[ ] Use if inside a while loop
[ ] Use a counter
[ ] Use an accumulator/sum variable
[ ] Process digits using while
[ ] Create input-driven loops
[ ] Understand when a loop should stop


TRAINER NOTE
------------

For students who struggle with "what condition should I write?", teach them
to ask these three questions before writing the while condition:

1. START â€“ Where should my variable start?
2. REPEAT â€“ Until when should I continue?
3. CHANGE â€“ What should happen to the variable after every repetition?

Example:

Task: Print 1 to 5

START:
i = 1

REPEAT:
while i <= 5:

CHANGE:
i = i + 1

This simple START â†’ REPEAT â†’ CHANGE pattern can be applied to most
beginner while-loop programs."""