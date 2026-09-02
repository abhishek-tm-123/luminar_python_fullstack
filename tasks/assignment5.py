"""PYTHON FOR LOOP â€“ BEGINNER PRACTICE QUESTIONS
================================================

Objective:
Practice Python for loops using range(), user input, counting, summing,
and simple patterns.

Instructions:
- Write a separate Python program for each question.
- Use a for loop wherever the question asks you to repeat an operation.
- Try to solve the questions without using while loops.

================================================
SECTION 1: BASIC FOR LOOP
================================================

Q1. Print Numbers from 1 to 10
Write a Python program to print numbers from 1 to 10 using a for loop.

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

for i in range(1,11):
    print(i)



Q2. Print Numbers from 1 to N
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
for i in range(1,n+1):
    print(i)


Q3. Print Numbers from N to 1
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
for i in range(n,0,-1):
    print(i)


Q4. Print Even Numbers from 1 to 20
Write a program to print all even numbers between 1 and 20.

Sample Output:
2
4
6
8
10
12
14
16
18
20

answer:

for i in range(1,21):
    if i%2==0:
        print(i)

Q5. Print Odd Numbers from 1 to 20
Write a program to print all odd numbers between 1 and 20.

Sample Output:
1
3
5
7
9
11
13
15
17
19

answer:

for i in range(1,21):
    if i%2!=0:
        print(i)

================================================
SECTION 2: FOR LOOP WITH USER INPUT
================================================

Q6. Print Multiples of 5
Ask the user to enter N. Print the first N multiples of 5.

Sample Input:
5

Sample Output:
5
10
15
20
25

answer:


n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i*5)


Q7. Print Multiples of a Number
Ask the user to enter a number and print its first 10 multiples.

Sample Input:
7

Sample Output:
7
14
21
28
35
42
49
56
63
70

answer:

n=int(input("enter a number:"))
for i in range(1,11):
    print(i*n)



Q8. Print a Number Repeatedly
Ask the user to enter a number N and print the number N times.

Sample Input:
3

Sample Output:
3
3
3

answer:

n=int(input("enter a number:"))
for i in range(1,n+1):
    print(n)



Q9. Print Numbers with Their Squares
Ask the user to enter N. Print each number from 1 to N along with its square.

Sample Input:
5

Sample Output:
1 1
2 4
3 9
4 16
5 25

answer:


n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i,i**2)



Q10. Print Numbers with Their Cubes
Ask the user to enter N. Print each number from 1 to N along with its cube.

Sample Input:
4

Sample Output:
1 1
2 8
3 27
4 64

answer:


n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i,i**3)

================================================
SECTION 3: SUM AND COUNT
================================================

Q11. Sum of Numbers from 1 to N
Ask the user to enter N and find the sum of numbers from 1 to N.

Sample Input:
5

Sample Output:
Sum = 15

answer:

n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum =",sum)



Q12. Sum of Even Numbers
Ask the user to enter N and find the sum of all even numbers from 1 to N.

Sample Input:
10

Sample Output:
Sum = 30

answer:

n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print("Sum =",sum)


Q13. Sum of Odd Numbers
Ask the user to enter N and find the sum of all odd numbers from 1 to N.

Sample Input:
10

Sample Output:
Sum = 25

answer:

n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    if i%2!=0:
        sum+=i
print("Sum =",sum)



Q14. Count Even Numbers
Ask the user to enter N and count how many even numbers are present between 1 and N.

Sample Input:
10

Sample Output:
Even count = 5

answer:

n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
print("Even count =",count)



Q15. Count Odd Numbers
Ask the user to enter N and count how many odd numbers are present between 1 and N.

Sample Input:
10

Sample Output:
Odd count = 5

n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if i%2!=0:
        count+=1
print("Odd count =",count)


================================================
SECTION 4: MULTIPLICATION TABLES
================================================

Q16. Multiplication Table
Ask the user to enter a number and print its multiplication table from 1 to 10.

Sample Input:
5

Sample Output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

answer:

n=int(input("enter a number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)



Q17. Tables from 1 to 5
Print multiplication tables for numbers 1 to 5. Print each table from
1 to 10.

Sample Output:
Table of 1
1 x 1 = 1
...
1 x 10 = 10

Table of 2
2 x 1 = 2
...
2 x 10 = 20

Continue up to Table of 5.

answer:

for i in range(1,6):
    print("Table of",i)
    print("\n")
    for j in range(1,11):
        print(i,"x",j,"=",i*j)



================================================
SECTION 5: SIMPLE LOGIC WITH FOR LOOP
================================================

Q18. Print Numbers Divisible by 3
Ask the user to enter N and print all numbers from 1 to N that are
divisible by 3.

Sample Input:
15

Sample Output:
3
6
9
12
15

answer:

n=int(input("enter a number:"))
for i in range(1,n+1):
    if i%3==0:
        print(i)


Q19. Print Numbers Divisible by 5
Ask the user to enter N and print all numbers from 1 to N that are
divisible by 5.

Sample Input:
25

Sample Output:
5
10
15
20
25

answer:

n=int(input("enter a number:"))
for i in range(1,n+1):
    if i%5==0:
        print(i)


Q20. Count Numbers Divisible by 3
Ask the user to enter N and count how many numbers from 1 to N are
divisible by 3.

Sample Input:
15

Sample Output:
Count = 5

answer:

n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if i%3==0:
        count+=1
print("Count =",count)



Q21. Find the Sum of Numbers Divisible by 5
Ask the user to enter N and find the sum of all numbers from 1 to N
that are divisible by 5.

Sample Input:
20

Sample Output:
Sum = 50

answer:

n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    if i%5==0:
        sum+=i

print("Sum=",sum)



Q22. Print Positive Numbers
Ask the user to enter 5 numbers. Print only the positive numbers.

Sample Input:
10
-5
7
-2
4

Sample Output:
10
7
4

answer:

print("enter 5 numbers:")
for i in range(1,6):
    n=int(input())
    if n>0:
        print(n)



Q23. Count Positive Numbers
Ask the user to enter 5 numbers and count how many are positive.

Sample Input:
10
-5
7
-2
4

Sample Output:
Positive count = 3

answer:

print("enter 5 numbers:")
count=0
for i in range(1,6):
    n=int(input())
    if n>0:
        count+=1

print("Positive count =", count)


Q24. Find the Largest Number
Ask the user to enter 5 numbers and find the largest number using a
for loop.

Sample Input:
12
45
7
89
23

Sample Output:
Largest = 89

answer:

print("enter 5 numbers:")
largest=0
for i in range(1,6):
    n=int(input())
    if n>largest:
        largest=n
print("Largest =", largest)



Q25. Find the Smallest Number
Ask the user to enter 5 numbers and find the smallest number using a
for loop.

Sample Input:
12
45
7
89
23

Sample Output:
Smallest = 7

answer:

print("Enter 5 numbers:")

smallest = None

for i in range(5):
    n = int(input())

    if smallest is None or n < smallest:
        smallest = n

print("Smallest =", smallest)



================================================
SECTION 6: BEGINNER CHALLENGE
================================================

Q26. Factorial of a Number
Ask the user to enter a number and find its factorial using a for loop.

Sample Input:
5

Sample Output:
Factorial = 120

answer:

n=int(input("enter a number:"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("Factorial =", factorial)



Q27. Reverse Counting by 2
Ask the user to enter N and print numbers from N down to 1, decreasing
by 2 each time.

Sample Input:
10

Sample Output:
10
8
6
4
2

answer:

n=int(input("enter a number:"))
for i in range(n,0,-2):
    print(i)



Q28. Sum of 5 User Inputs
Ask the user to enter 5 numbers and find their total.

Sample Input:
10
20
30
40
50

Sample Output:
Total = 150

answer:

print("enter 5 numbers:")
total = 0
for i in range(5):
    n = int(input())
    total += n
print("Total =", total)



Q29. Find the Average of 5 Numbers
Ask the user to enter 5 numbers and calculate their average.

Sample Input:
10
20
30
40
50



Sample Output:
Average = 30.0

answer:

print("enter 5 numbers:")
total = 0
for i in range(5):
    n = int(input())
    total += n
print("Average =", total / 5)


Q30. Count Numbers Greater Than 50
Ask the user to enter 5 numbers. Count how many numbers are greater
than 50.

Sample Input:
25
75
60
40
90

Sample Output:
Count = 3

answer:
print("enter 5 numbers:")
count = 0
for i in range(5):
    n = int(input())
    if n > 50:
        count += 1

print("Count =", count)


================================================
BONUS PRACTICE
================================================

Try solving these without looking at previous solutions.

1. Print numbers from 10 to 50.
2. Print all multiples of 4 from 1 to 40.
3. Find the sum of numbers from 10 to 20.
4. Count numbers divisible by 2 between 1 and 50.
5. Print the squares of even numbers from 1 to 10.
6. Print the cubes of odd numbers from 1 to 10.
7. Find the sum of squares from 1 to N.
8. Find the sum of cubes from 1 to N.
9. Print numbers from N to 1 using a step of -1.
10. Ask for 10 numbers and find how many are positive, negative, and zero.

================================================
END OF PRACTICE
================================================"""