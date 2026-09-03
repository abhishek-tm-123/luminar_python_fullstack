"""================================================================================
          PRACTICE QUESTION BANK: DECISION MAKING & LOOPING CONCEPTS
                  Foundational Programming & Logic Building
================================================================================

Target Audience: Beginner to Intermediate Programming Students
Topics Covered : Conditional Statements (if-else), Loops (for, while),
                 Mathematical Logic, Number Theory, Digit Manipulation

--------------------------------------------------------------------------------
TABLE OF CONTENTS
--------------------------------------------------------------------------------
1. Module 1: Accumulators & Series Summation
   - Q1: Sum of First N Natural Numbers
   - Q2: Sum of N Odd Numbers
   - Q3: Sum of Even Numbers in a Range

2. Module 2: Conditional Logic & Calendar Algorithms
   - Q4: Leap Year Determination & Range Output (1800 to 2026)

3. Module 3: Divisibility & Number Theory
   - Q5: Divisors / Factors of a Given Number
   - Q6: Common Divisors of Two Numbers
   - Q7: Greatest Common Divisor (GCD / HCF) of Two Numbers
   - Q8: Prime Number Verification & Prime Range Search

4. Module 4: Sequences & Digit Analysis
   - Q9: Fibonacci Series Generation
   - Q10: Armstrong Number Verification (Multi-digit Support)

5. Summary Checklist for Mastery

================================================================================
MODULE 1: ACCUMULATORS & SERIES SUMMATION
================================================================================

--------------------------------------------------------------------------------
QUESTION 1: Sum of First N Natural Numbers
--------------------------------------------------------------------------------
Description:
Write a program that takes a positive integer N as input and calculates the 
sum of all numbers from 1 to N using a loop.

Key Learning Objective:
Understanding basic loop accumulators and running totals.

Sample Input 1:
Enter N: 5

Sample Output 1:
Sum of numbers from 1 to 5 = 15
Explanation: 1 + 2 + 3 + 4 + 5 = 15

Sample Input 2:
Enter N: 10

Sample Output 2:
Sum of numbers from 1 to 10 = 55
Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

Sample Input 3:
Enter N: 1

Sample Output 3:
Sum of numbers from 1 to 1 = 1

answer :

n=int(input("Enter N: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum of numbers from 1 to",n,"=",sum)


--------------------------------------------------------------------------------
QUESTION 2: Sum of N Odd Numbers
--------------------------------------------------------------------------------
Description:
Write a program to calculate the sum of odd numbers. 
(Implement both variations: (a) First N odd numbers, and (b) Odd numbers up to N).

Key Learning Objective:
Combining conditional logic (`if number % 2 != 0`) inside loops, or using loop step values.

Sample Input 1 (First N Odd Numbers):
Enter N: 5

Sample Output 1:
First 5 odd numbers: 1, 3, 5, 7, 9
Sum = 25

Sample Input 2 (Odd Numbers up to N):
Enter Limit N: 10

Sample Output 2:
Odd numbers up to 10: 1, 3, 5, 7, 9
Sum = 25

Sample Input 3 (First N Odd Numbers):
Enter N: 7

Sample Output 3:
First 7 odd numbers: 1, 3, 5, 7, 9, 11, 13
Sum = 49

answer for (a) First N odd numbers:

n=int(input("Enter N:"))
sum=0
print("First ",n," odd numbers:")
for i in range(1,2*n,2):
    print(i)
    sum=sum+i
print("Sum =",sum)

answer for (b) Odd numbers up to N:

limit = int(input("Enter limit N:"))
sum = 0
print("Odd numbers upto ",limit," :")
for i in range(1,limit+1):
    if i%2!=0:
        print(i)
        sum=sum+i
print("Sum =",sum)

--------------------------------------------------------------------------------
QUESTION 3: Sum of Even Numbers
--------------------------------------------------------------------------------
Description:
Write a program that accepts a limit N and calculates the sum of all even numbers 
from 1 up to N.

Key Learning Objective:
Modulo arithmetic (`number % 2 == 0`) and conditional summation.

Sample Input 1:
Enter N: 10

Sample Output 1:
Even numbers up to 10: 2, 4, 6, 8, 10
Sum of even numbers = 30

Sample Input 2:
Enter N: 7

Sample Output 2:
Even numbers up to 7: 2, 4, 6
Sum of even numbers = 12

Sample Input 3:
Enter N: 1

Sample Output 3:
No even numbers in the range 1 to 1.
Sum = 0

answer:

limit=int(input("enter N:"))
sum=0
if limit<2:
    print("No even numbers in the range 1 to",limit)
else:
    for i in range(1,limit+1):
        if i%2==0:
            print(i)
            sum=sum+i
print("Sum =",sum)



================================================================================
MODULE 2: CONDITIONAL LOGIC & CALENDAR ALGORITHMS
================================================================================

--------------------------------------------------------------------------------
QUESTION 4: Leap Year Determination & Range Output (1800 to 2026)
--------------------------------------------------------------------------------
Description:
Part A: Write a program to check if a given year is a Leap Year.
Part B: Print all leap years between 1800 and 2026 (inclusive) and count how 
        many leap years exist in this period.

Leap Year Rules:
1. If a year is divisible by 4, it is a leap year UNLESS:
2. It is divisible by 100, then it is NOT a leap year UNLESS:
3. It is divisible by 400, then it IS a leap year.

Formula: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

Sample Input 1:
Enter Year: 1900

Sample Output 1:
1900 is NOT a Leap Year (Divisible by 100 but not by 400).

Sample Input 2:
Enter Year: 2000

Sample Output 2:
2000 IS a Leap Year (Divisible by 400).

Sample Input 3:
Enter Year: 2024

Sample Output 3:
2024 IS a Leap Year.

Sample Output for Range (1800 to 2026):
Leap years between 1800 and 2026:
1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844, 1848, 1852, 
1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1904, 1908, 1912, 
1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 
1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 
2020, 2024

Total leap years found: 55

answer for Part A:

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "IS a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")

answer for part B:

leap_years = 0
for i in range(1800, 2027):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i, end=", ") 
        leap_years += 1
        
print("\nTotal leap years found:", leap_years)



================================================================================
MODULE 3: DIVISIBILITY & NUMBER THEORY
================================================================================

--------------------------------------------------------------------------------
QUESTION 5: Divisors / Factors of a Given Number
--------------------------------------------------------------------------------
Description:
Write a program to find and display all positive divisors (factors) of a given number N.

Key Learning Objective:
Looping from 1 to N (or 1 to N/2) and testing exact divisibility (`N % i == 0`).

Sample Input 1:
Enter Number: 8

Sample Output 1:
Divisors of 8: 1, 2, 4, 8

Sample Input 2:
Enter Number: 6

Sample Output 2:
Divisors of 6: 1, 2, 3, 6

Sample Input 3:
Enter Number: 13

Sample Output 3:
Divisors of 13: 1, 13

answer :

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=", ")


--------------------------------------------------------------------------------
QUESTION 6: Common Divisors of Two Numbers
--------------------------------------------------------------------------------
Description:
Write a program that takes two integers A and B and finds all numbers that divide 
both A and B with no remainder.

Key Learning Objective:
Simultaneous conditional checking using logical AND (`A % i == 0 and B % i == 0`).

Sample Input 1:
Enter Number 1: 8
Enter Number 2: 24

Sample Output 1:
Common divisors of 8 and 24: [1, 2, 4, 8]

Sample Input 2:
Enter Number 1: 12
Enter Number 2: 18

Sample Output 2:
Common divisors of 12 and 18: [1, 2, 3, 6]

Sample Input 3:
Enter Number 1: 15
Enter Number 2: 28

Sample Output 3:
Common divisors of 15 and 28: [1]

answer :

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
smallest = min(num1, num2)
print("common divisors of ",num1,"and",num2,end=" :")
for i in range(1,smallest+1):
    if num1%i==0 and num2%i==0 :
        print(i,end=", ")

--------------------------------------------------------------------------------
QUESTION 7: Greatest Common Divisor (GCD / HCF) of Two Numbers
--------------------------------------------------------------------------------
Description:
Write a program to find the Greatest Common Divisor (GCD) of two numbers A and B.
(Implement using both loop iteration and the Euclidean Algorithm).

Key Learning Objective:
Updating maximum divisor tracker or executing Euclidean modulo reduction.

Sample Input 1:
Enter Number 1: 8
Enter Number 2: 24

Sample Output 1:
GCD of 8 and 24 is: 8

Sample Input 2:
Enter Number 1: 54
Enter Number 2: 24

Sample Output 2:
GCD of 54 and 24 is: 6

Sample Input 3:
Enter Number 1: 17
Enter Number 2: 13

Sample Output 3:
GCD of 17 and 13 is: 1

answer:

num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))
smallest = min(num1,num2)
gcd = 0
for i in range(2,smallest+1):
    if num1%i==0 and num2%i==0:
        gcd = i

print(gcd)

--------------------------------------------------------------------------------
QUESTION 8: Prime Number Verification & Prime Range Search
--------------------------------------------------------------------------------
Description:
Part A: Check whether a given integer N is a prime number.
Part B: Display its total divisor count or list of factors to explain WHY it is or isn't prime.

Definition: A prime number is an integer greater than 1 that has exactly two 
distinct positive divisors: 1 and itself.

Sample Input 1:
Enter Number: 8

Sample Output 1:
Factors of 8: [1, 2, 4, 8] (4 factors)
Result: 8 is NOT a Prime Number âŒ

Sample Input 2:
Enter Number: 19

Sample Output 2:
Factors of 19: [1, 19] (2 factors)
Result: 19 IS a Prime Number âœ…

Sample Input 3:
Enter Number: 9

Sample Output 3:
Factors of 9: [1, 3, 9] (3 factors)
Result: 9 is NOT a Prime Number âŒ

Sample Input 4:
Enter Number: 13

Sample Output 4:
Factors of 13: [1, 13] (2 factors)
Result: 13 IS a Prime Number âœ…

Sample Input 5:
Enter Number: 1

Sample Output 5:
Factors of 1: [1] (1 factor)
Result: 1 is NOT a Prime Number (Prime numbers must be > 1) âŒ

answer:
"""
num = int(input("Enetr number:"))
count=0
print("factors ",end=":")
for i in range(1,num+1):
    if num%i==0:
        count+=1
        print(i,end=", ")
print("\n")
if count == 2 and num >2:
    print(num,"is prime number")
else:
    print(num,"is not prime number")


"""


================================================================================
MODULE 4: SEQUENCES & DIGIT ANALYSIS
================================================================================

--------------------------------------------------------------------------------
QUESTION 9: Fibonacci Series Generation
--------------------------------------------------------------------------------
Description:
Write a program to generate the first N terms of the Fibonacci series.
The series begins with 0 and 1. Each subsequent term is the sum of the two preceding terms.

Key Learning Objective:
State management across loop iterations (variable swap `a, b = b, a + b`).

Sample Input 1:
Enter number of terms N: 10

Sample Output 1:
Fibonacci Series (10 terms):
0 1 1 2 3 5 8 13 21 34

Sample Input 2:
Enter number of terms N: 5

Sample Output 2:
Fibonacci Series (5 terms):
0 1 1 2 3

Sample Input 3:
Enter number of terms N: 1

Sample Output 3:
Fibonacci Series (1 term):
0

answer:

limit = int(input("enter number of terms:"))
prev=0
curr=1
for i in range(1,limit+1):
    print(prev)
    next=prev+curr
    prev,curr = curr,next


--------------------------------------------------------------------------------
QUESTION 10: Armstrong Number Verification (Narcissistic Number)
--------------------------------------------------------------------------------
Description:
Write a program to check whether a given integer is an Armstrong number.
An Armstrong number of D digits is a number equal to the sum of its digits 
each raised to the power of D.

Formula: N = d_1^D + d_2^D + ... + d_D^D

Key Learning Objective:
Extracting digits using modulo (`n % 10`), reducing number (`n // 10`), 
and computing powers dynamically based on total digit count.

Sample Input 1:
Enter Number: 153

Sample Output 1:
Number of digits (D): 3
Calculation: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
Result: 153 IS an Armstrong Number âœ…

Sample Input 2:
Enter Number: 370

Sample Output 2:
Number of digits (D): 3
Calculation: 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370
Result: 370 IS an Armstrong Number âœ…

Sample Input 3:
Enter Number: 1634

Sample Output 3:
Number of digits (D): 4
Calculation: 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
Result: 1634 IS an Armstrong Number âœ…

Sample Input 4:
Enter Number: 123

Sample Output 4:
Number of digits (D): 3
Calculation: 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
Result: 123 is NOT an Armstrong Number âŒ

answer:

num=int(input("Enter number:"))
digit_count=len(str(num))
print("Number of digits :",digit_count)
sum=0
temp=num
while temp!=0:
    last_digit = temp%10
    exponent=last_digit**digit_count
    sum=sum+exponent
    temp=temp//10

if num==sum:
    print(num,"is Amstrong number")
else:
    print(num,"is not Amstrong number")



================================================================================
SUMMARY CHECKLIST FOR STUDENTS
================================================================================
After completing these 10 core questions, students should be able to:
[ ] Distinguish between when to use `for` loops vs `while` loops.
[ ] Construct complex boolean conditionals (`and`, `or`, `not`).
[ ] Extract and manipulate digits of numbers dynamically using integer arithmetic.
[ ] Keep track of running totals, counts, minimums, and maximums inside loops.
[ ] Identify prime numbers and divisors efficiently.
[ ] Implement classic mathematical algorithms like Fibonacci state swapping and GCD.
================================================================================"""