"""PYTHON BEGINNER ASSESSMENT
25 SIMPLE IF...ELSE TASKS
================================

Instructions:
- Read each problem carefully.
- Take input using input().
- Use if...else wherever required.
- Do not use loops or functions unless you want to practice them separately.
- Try to solve each problem yourself before checking the sample.


TASK 1: Positive or Negative
--------------------------------
Question:
Write a program to check whether a number is positive or negative.

Sample Input:
Input: -5

Sample Output:
Output: Negative

Your Code:

num = int(input("Input :"))
if num > 0:
    print("Output :Positive")
else:
    print("Output :Negative")

TASK 2: Even or Odd
--------------------------------
Question:
Write a program to check whether a number is even or odd.

Sample Input:
Input: 8

Sample Output:
Output: Even

Your Code:

num = int(input("Input :"))
if num % 2 == 0:
    print("Output : Even")
else:
    print("Output : Odd")


TASK 3: Voting Eligibility
--------------------------------
Question:
Write a program to check whether a person is eligible to vote. Age should be 18 or above.

Sample Input:
Input: 20

Sample Output:
Output: Eligible to vote

Your Code:

age = int(input("Enter your age :"))
if age>18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



TASK 4: Pass or Fail
--------------------------------
Question:
Write a program to check whether a student passed or failed. Mark 40 or above is a pass.

Sample Input:
Input: 35

Sample Output:
Output: Fail

Your Code:

mark = int(input("enter your mark :"))
if mark>=40 :
    print("pass")
else:
    print("Fail")


TASK 5: Greater Number
--------------------------------
Question:
Write a program to find whether the first number or second number is greater.

Sample Input:
Input: 15, 10

Sample Output:
Output: First number is greater

Your Code:

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

if num1 > num2:
    print("first number is greater")
else:
    print("second number is greater")



TASK 6: Temperature Check
--------------------------------
Question:
Write a program to check whether the temperature is hot or normal. Consider 30Ã‚Â°C or above as hot.

Sample Input:
Input: 32

Sample Output:
Output: Hot

Your Code:

temp = int(input("enter the temperature :"))
if temp>=30:
    print("Hot")
else:
    print("normal")



TASK 7: Freezing Point
--------------------------------
Question:
Write a program to check whether the temperature is below freezing point. Use 0Ã‚Â°C as the freezing point.

Sample Input:
Input: -3

Sample Output:
Output: Below freezing point

Your Code:

temp = int(input("enter the temperature :"))
if temp < 0:
    print("below freezing point") 
else:
    print("above freezing point")


TASK 8: Number is Zero
--------------------------------
Question:
Write a program to check whether a number is zero or not.

Sample Input:
Input: 0

Sample Output:
Output: Number is zero

Your Code:

num = int(input("enter a number :"))
if num == 0:
    print("Number is zero")




TASK 9: Password Check
--------------------------------
Question:
Write a program to check whether a password is correct. Use 'python123' as the correct password.

Sample Input:
Input: python123

Sample Output:
Output: Correct password

Your Code:

correct_password = "python123"
password = input("enter password :")

if password == correct_password:
    print("Correct password")
else:
    print("incorrect password")


TASK 10: Largest of Two
--------------------------------
Question:
Write a program to find the largest of two numbers.

Sample Input:
Input: 25, 40

Sample Output:
Output: 40 is the largest

Your Code:

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

if num1 > num2:
    print(num1,"is largest")
else:
    print(num2,"is largest")

TASK 11: Smallest of Two
--------------------------------
Question:
Write a program to find the smallest of two numbers.

Sample Input:
Input: 12, 7

Sample Output:
Output: 7 is the smallest

Your Code:
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

if num1 < num2:
    print(num1,"is smallest")
else:
    print(num2,"is smallest")

TASK 12: Age Category
--------------------------------
Question:
Write a program to check whether a person is an adult or minor. Age 18 or above is adult.

Sample Input:
Input: 16

Sample Output:
Output: Minor

Your Code:
age = int(input("Enter your age :"))
if age>=18:
    print("Adult")
else:
    print("Minor")



TASK 13: Discount Eligibility
--------------------------------
Question:
Write a program to check whether a customer gets a discount. Give a discount when purchase amount is 1000 or more.

Sample Input:
Input: 1200

Sample Output:
Output: Discount available

Your Code:
ammount = int(input("Enter the ammount:"))
if ammount>1000:
    print("Discount available")
else:
    print("Discount is not available")



TASK 14: Number Divisible by 5
--------------------------------
Question:
Write a program to check whether a number is divisible by 5.

Sample Input:
Input: 25

Sample Output:
Output: Divisible by 5

Your Code:
num = int(input("Enter the number:"))
if num%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")


TASK 15: Number Divisible by 10
--------------------------------
Question:
Write a program to check whether a number is divisible by 10.

Sample Input:
Input: 27

Sample Output:
Output: Not divisible by 10

Your Code:

num = int(input("Enter the number:"))
if num%10==0:
    print("divisible by 10")
else:
    print("not divisible by 10")

TASK 16: Salary Bonus
--------------------------------
Question:
Write a program to check whether an employee gets a bonus. Give a bonus when salary is below 30000.

Sample Input:
Input: 25000

Sample Output:
Output: Bonus available

Your Code:
salary = int(input("Enter the salary:"))
if salary<30000:
    print("Bonus available")
else:
    print("bonus is not available")


TASK 17: Exam Result
--------------------------------
Question:
Write a program to check whether a student gets distinction. Mark 75 or above is distinction.

Sample Input:
Input: 82

Sample Output:
Output: Distinction

Your Code:
mark = int(input("Enter the mark:"))
if mark>=75:
    print("Distinction")
else:
    print("no Distinction")

TASK 18: Shopping Amount
--------------------------------
Question:
Write a program to check whether free delivery is available. Free delivery is given for orders of 500 or more.

Sample Input:
Input: 450

Sample Output:
Output: Delivery charge applicable

Your Code:
price = int(input("Enter the price:"))
if price>=500:
    print("Free delivery")
else:
    print("Delivery charge applicable")

TASK 19: Login Check
--------------------------------
Question:
Write a program to check whether both username and password are correct. Use username 'admin' and password '1234'.

Sample Input:
Input: admin, 1234

Sample Output:
Output: Login successful

Your Code:

db_username = "admin"
db_password = "1234"
username = input("enter username:")
password = input("enter password:")

if username==db_username and password==db_password:
    print("login successful")
else:
    print("login failed")

TASK 20: Day Check
--------------------------------
Question:
Write a program to check whether a given day number is a weekend. Consider 6 and 7 as weekend days.

Sample Input:
Input: 6

Sample Output:
Output: Weekend

Your Code:

day = int(input("enter the day number:"))
if day==6 or day==7:
    print("Weekend")
else:
    print("not Weekend")


TASK 21: Number Range
--------------------------------
Question:
Write a program to check whether a number is between 1 and 100.

Sample Input:
Input: 75

Sample Output:
Output: Number is between 1 and 100

Your Code:

num = int(input("enter a number :"))
if num>1 and num<100 :
    print("Number is between 1 and 100")
else:
    print("Number is not between 1 and 100")


TASK 22: Driving Age
--------------------------------
Question:
Write a program to check whether a person can apply for a driving licence. Age should be 18 or above.

Sample Input:
Input: 17

Sample Output:
Output: Cannot apply

Your Code:

age = int(input("Enter your age :"))
if age>=18:
    print("Can apply")
else:
    print("Cannot apply")



TASK 23: Water Level
--------------------------------
Question:
Write a program to check whether a water tank needs filling. If water level is below 20%, display 'Fill the tank'.

Sample Input:
Input: 15

Sample Output:
Output: Fill the tank

Your Code:
water = int(input("Enter the water level:"))
if water<20:
    print("Fill the tank")
else:
    print("water level is good")


TASK 24: Movie Ticket
--------------------------------
Question:
Write a program to check whether a person gets a child ticket. Age below 12 gets a child ticket.

Sample Input:
Input: 10

Sample Output:
Output: Child ticket

Your Code:
age = int(input("Enter your age :"))
if age<12:
    print("Child ticket")
else:
    print("Not Child ticket")



TASK 25: Simple Calculator
--------------------------------
Question:
Write a program to take two numbers and an operator (+ or -). Perform the operation using if...else.

Sample Input:
Input: 20, 8, +

Sample Output:
Output: 28

Your Code:

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
operator = input("enter operator (+ or -) :")

if operator=="+":
    result = num1+num2
    print(result)
else:
    result = num1-num2
    print(result)

"""