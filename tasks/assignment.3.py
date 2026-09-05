# # LEVEL 1 â€“ Basic If / Else

# ## Question 1 â€“ Positive or Negative

# Write a program to check whether a number is positive or negative.

# ### Sample Input

# ```text
# Enter number: 25
# ```

# ### Sample Output

# ```text
# Positive number
# ```

# ---

# n = float(input("Enter number: "))

# if n > 0:
#     print("Positive number")
# else:
#     print("Negative number")

## Question 2 â€“ Even or Odd

# Write a program to check whether a number is even or odd.

# ### Sample Input

# ```text
# Enter number: 18
# ```

# ### Sample Output

# ```text
# Even number
# ```

# n=int(input("Enter number: "))
# if n%2==0:
#     print("Even number")
# else:
#     print("Odd number")


## Question 3 â€“ Eligible to Vote

# Write a program to check whether a person is eligible to vote.

# Age must be 18 or above.

# ### Sample Input

# ```text
# Enter age: 21
# ```

# ### Sample Output

# ```text
# Eligible to vote
# ```

# n=int(input("Enter age: "))
# if n>=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


## Question 4 â€“ Pass or Fail

# Write a program to check whether a student has passed an examination.

# A student passes if the mark is 40 or above.

# ### Sample Input

# ```text
# Enter mark: 65
# ```

# ### Sample Output

# ```text
# Passed
# ```

# ---

# n=int(input("Enter mark: "))
# if n>=40:
#     print("Passed")
# else:
#     print("Failed")

# ## Question 5 â€“ Greater Number

# Write a program to compare two numbers and display which number is greater.

# ### Sample Input

# ```text
# Enter first number: 25
# Enter second number: 18
# ```

# ### Sample Output

# ```text
# 25 is greater
# ```

# ---

# n=int(input("Enter first number: "))
# m=int(input("Enter second number: "))
# if n>m:
#     print(n,"is greater")
# elif m>n:
#     print(m," is greater")
# else:
#     print("Both numbers are equal")

# # LEVEL 2 â€“ Introducing Elif

# ## Question 6 â€“ Positive, Negative or Zero

# Write a program to check whether a number is:

# * Positive
# * Negative
# * Zero

# ### Sample Input

# ```text
# Enter number: -10
# ```

# ### Sample Output

# ```text
# Negative
# ```

# ---

# n=int(input("Enter number: "))
# if n>0:
#     print("Positive")
# elif n<0:
#     print("Negative")
# else:
#     print("Zero")

# ## Question 7 â€“ Grade Calculator

# Write a program to display the grade based on the mark.

# | Mark     | Grade |
# | -------- | ----- |
# | 90â€“100   | A     |
# | 75â€“89    | B     |
# | 60â€“74    | C     |
# | 40â€“59    | D     |
# | Below 40 | F     |

# ### Sample Input

# ```text
# Enter mark: 82
# ```

# ### Sample Output

# ```text
# Grade B
# ```

# ---

# n=int(input("Enter mark: "))
# if n>=90 and n<=100:
#     print("Grade A")
# elif n>=75 and n<=89:
#     print("Grade B")
# elif n>=60 and n<=74:
#     print("Grade C")
# elif n>=40 and n<=59:
#     print("Grade D")
# else:
#     print("Grade F")

# ## Question 8 â€“ Age Category

# Write a program to identify a person's age category.

# | Age         | Category       |
# | ----------- | -------------- |
# | 0â€“12        | Child          |
# | 13â€“19       | Teenager       |
# | 20â€“59       | Adult          |
# | 60 or above | Senior Citizen |

# ### Sample Input

# ```text
# Enter age: 16
# ```

# ### Sample Output

# ```text
# Teenager
# ```

# ---

# n=int(input("Enter age: "))
# if n>=0 and n<=12:
#     print("Child")
# elif n>=13 and n<=19:
#     print("Teenager")
# elif n>=20 and n<=59:
#     print("Adult")
# else:
#     print("Senior Citizen")

# ## Question 9 â€“ Temperature

# Write a program to classify the temperature.

# | Temperature | Result |
# | ----------- | ------ |
# | Below 15    | Cold   |
# | 15â€“30       | Normal |
# | Above 30    | Hot    |

# ### Sample Input

# ```text
# Enter temperature: 35
# ```

# ### Sample Output

# ```text
# Hot
# ```

# ---

# n=int(input("Enter temperature: "))
# if n<15:
#     print("Cold")
# elif n>=15 and n<=30:
#     print("Normal")
# else:
#     print("Hot")

# ## Question 10 â€“ Number Comparison

# Write a program to compare two numbers.

# Display:

# * First number is greater
# * Second number is greater
# * Both numbers are equal

# ### Sample Input

# ```text
# Enter first number: 25
# Enter second number: 25
# ```

# ### Sample Output

# ```text
# Both numbers are equal
# ```

# ---

# n=int(input("Enter first number: "))
# m=int(input("Enter second number: "))
# if n>m:
#     print(n,"is greater")
# elif m>n:
#     print(m," is greater")
# else:
#     print("Both numbers are equal")


# # LEVEL 3 â€“ Multiple Conditions

# ## Question 11 â€“ Electricity Bill Category

# Write a program to display the electricity usage category.

# | Units     | Category        |
# | --------- | --------------- |
# | 0â€“100     | Low Usage       |
# | 101â€“300   | Medium Usage    |
# | 301â€“500   | High Usage      |
# | Above 500 | Very High Usage |

# ### Sample Input

# ```text
# Enter units: 350
# ```

# ### Sample Output

# ```text
# High Usage
# ```

# units=int(input("Enter units: "))
# if units>=0 and units<=100:
#     print("Low Usage")
# elif units>=101 and units<=300:
#     print("Medium Usage")
# elif units>=301 and units<=500:
#     print("High Usage")
# else:
#     print("Very High Usage")

# ---

# ## Question 12 â€“ Simple Calculator

# Get two numbers and an operator from the user.

# Supported operators:

# * `+`
# * `-`
# * `*`
# * `/`

# Use `if`, `elif`, and `else` to perform the operation.

# ### Sample Input

# ```text
# Enter first number: 20
# Enter second number: 5
# Enter operator: /
# ```

# ### Sample Output

# ```text
# Result: 4.0
# ```

# n=int(input("Enter first number: "))
# m=int(input("Enter second number: "))
# operator=input("Enter operator: ")

# if operator == "+":
#     result = n + m
# elif operator == "-":
#     result = n - m
# elif operator == "*":
#     result = n * m
# elif operator == "/":
#     result = n / m

# print("Result:", result)

# ---

# ## Question 13 â€“ Traffic Signal

# Get a traffic signal color from the user.

# * `red` â†’ Stop
# * `yellow` â†’ Get Ready
# * `green` â†’ Go
# * Anything else â†’ Invalid signal

# ### Sample Input

# ```text
# Enter signal: green
# ```

# ### Sample Output

# ```text
# Go
# ```

# user=input("Enter signal: ")
# if user=="red":
#     print("Stop")
# elif user=="yellow":
#     print("Get Ready")
# elif user=="green":
#     print("Go")
# else:
#     print("Invalid signal")

# ---

# ## Question 14 â€“ Day Number

# Get a number from 1 to 7 and display the corresponding day.

# | Number | Day       |
# | ------ | --------- |
# | 1      | Monday    |
# | 2      | Tuesday   |
# | 3      | Wednesday |
# | 4      | Thursday  |
# | 5      | Friday    |
# | 6      | Saturday  |
# | 7      | Sunday    |

# ### Sample Input

# ```text
# Enter day number: 6
# ```

# ### Sample Output

# ```text
# Saturday
# ```

# day_number=int(input("Enter day number: "))
# if day_number==1:
#     print("Monday")
# elif day_number==2:
#     print("Tuesday")
# elif day_number==3:
#     print("Wednesday")
# elif day_number==4:
#     print("Thursday")
# elif day_number==5:
#     print("Friday")
# elif day_number==6:
#     print("Saturday")
# elif day_number==7:
#     print("Sunday")
# else:
#     print("Invalid day number")
# ---

# ## Question 15 â€“ Month Number

# Get a month number from the user and display the month name.

# ### Sample Input

# ```text
# Enter month number: 8
# ```

# ### Sample Output

# ```text
# August
# ```

# If the number is not between 1 and 12:

# ```text
# Invalid month
# ```

# month_number=int(input("Enter month number: "))
# if month_number==1:
#     print("January")
# elif month_number==2:
#     print("February")
# elif month_number==3:
#     print("March")
# elif month_number==4:
#     print("April")
# elif month_number==5:
#     print("May")
# elif month_number==6:
#     print("June")
# elif month_number==7:
#     print("July")
# elif month_number==8:
#     print("August")
# elif month_number==9:
#     print("September")
# elif month_number==10:
#     print("October")
# elif month_number==11:
#     print("November")
# elif month_number==12:
#     print("December")
# else:
#     print("Invalid month")


# ---

# # LEVEL 4 â€“ Real-World Problems

# ## Question 16 â€“ ATM Withdrawal

# Write a program for a simple ATM withdrawal.

# Get:

# * Account balance
# * Withdrawal amount

# Rules:

# * If withdrawal amount is greater than balance â†’ Insufficient balance
# * Otherwise â†’ Withdrawal successful

# ### Sample Input

# ```text
# Enter balance: 10000
# Enter withdrawal amount: 3000
# ```

# ### Sample Output

# ```text
# Withdrawal successful
# Remaining balance: 7000
# ```

# balance=float(input("Enter balance: "))
# withdrawal_amount=float(input("Enter withdrawal amount: "))
# if withdrawal_amount>balance:
#     print("Insufficient balance")
# else:
#     print("Withdrawal successful")
#     print("Remaining balance: ", balance - withdrawal_amount)
# ---

# ## Question 17 â€“ Login System

# Create a simple login system.

# Correct credentials:

# ```text
# username = admin
# password = 1234
# ```

# If both are correct:

# ```text
# Login successful
# ```

# Otherwise:

# ```text
# Invalid username or password
# ```

# ### Sample Input

# ```text
# Enter username: admin
# Enter password: 1234
# ```

# ### Sample Output

# ```text
# Login successful
# ```
# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Invalid username or password")

# ---

# ## Question 18 â€“ Shopping Discount

# Get the shopping amount.

# Apply discounts:

# | Amount         | Discount    |
# | -------------- | ----------- |
# | Below 1000     | No discount |
# | 1000â€“4999      | 10%         |
# | 5000â€“9999      | 20%         |
# | 10000 or above | 30%         |

# Display the discount amount and final amount.

# ### Sample Input

# ```text
# Enter amount: 6000
# ```

# ### Sample Output

# ```text
# Discount: 1200
# Final amount: 4800
# ```
# discount = 0
# amount = int(input("Enter amount: "))

# if amount < 1000:
#     discount = 0
# elif 1000 <= amount <= 4999:
#     discount = 0.1
# elif 5000 <= amount <= 9999:
#     discount = 0.2
# else:
#     discount = 0.3

# discount_amount = amount * discount
# final_amount = amount - discount_amount

# print("Discount: ", discount_amount)
# print("Final amount: ", final_amount)

# ---

# ## Question 19 â€“ Movie Ticket Price

# Get the person's age.

# Ticket prices:

# * Below 5 â†’ Free
# * 5â€“12 â†’ â‚¹100
# * 13â€“59 â†’ â‚¹200
# * 60 or above â†’ â‚¹120

# ### Sample Input

# ```text
# Enter age: 65
# ```

# ### Sample Output

# ```text
# Ticket price: â‚¹120
# ```

# age = int(input("Enter age: "))
# if age < 5:
#     price = 0
# elif 5 <= age <= 12:
#     price = 100
# elif 13 <= age <= 59:
#     price = 200
# else:
#     price = 120
# print(f"Ticket price: â‚¹{price}")
# ---

# ## Question 20 â€“ Salary Bonus

# Get an employee's salary and years of experience.

# Rules:

# * Experience below 2 years â†’ No bonus
# * 2â€“5 years â†’ 5% bonus
# * 6â€“10 years â†’ 10% bonus
# * Above 10 years â†’ 15% bonus

# ### Sample Input

# ```text
# Enter salary: 40000
# Enter experience: 7
# ```

# ### Sample Output

# ```text
# Bonus: 4000
# Total salary: 44000
# ```

# salary = float(input("Enter salary: "))
# experience = int(input("Enter experience: "))
# if experience < 2:
#     bonus = 0
# elif 2 <= experience <= 5:
#     bonus = 0.05 * salary
# elif 6 <= experience <= 10:
#     bonus = 0.10 * salary
# else:
#     bonus = 0.15 * salary
# print(f"Bonus: {bonus}")
# print(f"Total salary: {salary + bonus}")
# ---

# # LEVEL 5 â€“ Challenge Questions

# ## Question 21 â€“ Triangle Type

# Get three sides of a triangle.

# Determine whether the triangle is:

# * Equilateral
# * Isosceles
# * Scalene

# ### Sample Input

# ```text
# Enter side 1: 5
# Enter side 2: 5
# Enter side 3: 5
# ```

# ### Sample Output

# ```text
# Equilateral triangle
# ```

# side1 = float(input("Enter side 1: "))
# side2 = float(input("Enter side 2: "))
# side3 = float(input("Enter side 3: "))

# if side1 == side2 == side3:
#     print("Equilateral triangle")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")
# ---

# ## Question 22 â€“ Leap Year

# Write a program to check whether a given year is a leap year.

# ### Sample Input

# ```text
# Enter year: 2024
# ```

# ### Sample Output

# ```text
# 2024 is a leap year
# ```

# For example:

# ```text
# Enter year: 2023
# ```

# Output:

# ```text
# 2023 is not a leap year
# ```

# year = int(input("Enter year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")
# ---

# ## Question 23 â€“ BMI Category

# Get a person's:

# * Weight in kilograms
# * Height in meters

# Calculate BMI using:

# ```text
# BMI = weight / (height * height)
# ```

# Classify the result:

# | BMI         | Category    |
# | ----------- | ----------- |
# | Below 18.5  | Underweight |
# | 18.5â€“24.9   | Normal      |
# | 25â€“29.9     | Overweight  |
# | 30 or above | Obese       |

# ### Sample Input

# ```text
# Enter weight: 70
# Enter height: 1.75
# ```

# ### Sample Output

# ```text
# BMI: 22.86
# Category: Normal
# ```

# weight = float(input("Enter weight: "))
# height = float(input("Enter height: "))
# bmi = weight / (height * height)

# if bmi < 18.5:
#     category = "Underweight"
# elif 18.5 <= bmi <= 24.9:
#     category = "Normal"
# elif 25 <= bmi <= 29.9:
#     category = "Overweight"
# else:
#     category = "Obese"

# print(f"BMI: {bmi:.2f}")
# print(f"Category: {category}")

# ---

# ## Question 24 â€“ Electricity Bill Calculator

# Create an electricity bill calculator.

# Units consumed:

# * First 100 units â†’ â‚¹5/unit
# * Next 200 units â†’ â‚¹7/unit
# * Next 200 units â†’ â‚¹10/unit
# * Above 500 units â†’ â‚¹15/unit

# Calculate the total electricity bill.

# ### Sample Input

# ```text
# Enter units: 350
# ```

# ### Sample Output

# ```text
# Electricity Bill: â‚¹2000
# ```

# units = int(input("Enter units: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 300:
#     bill = (100 * 5) + ((units - 100) * 7)
# elif units <= 500:
#     bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)
# else:
#     bill = (100 * 5) + (200 * 7) + (200 * 10) + ((units - 500) * 15)

# print(f"Electricity Bill: â‚¹{bill}")

# > **Important:** This question requires you to understand how conditions can control different calculations, not just display messages.

# ---

# ## Question 25 â€“ Student Result System

# Create a complete student result system.

# Get marks for:

# * Python
# * MySQL
# * Django

# Calculate:

# ```text
# Total
# Average
# ```

# Then determine the result.

# ### Rules

# If **any subject mark is below 40**:

# ```text
# Result: Fail
# ```

# Otherwise calculate the average:

# | Average  | Grade |
# | -------- | ----- |
# | 90â€“100   | A+    |
# | 80â€“89    | A     |
# | 70â€“79    | B     |
# | 60â€“69    | C     |
# | 50â€“59    | D     |
# | Below 50 | E     |

# ### Sample Input

# ```text
# Enter Python mark: 85
# Enter MySQL mark: 78
# Enter Django mark: 92
# ```

# ### Sample Output

# ```text
# Total: 255
# Average: 85.0
# Result: Pass
# Grade: A
# ```

# python_mark = int(input("Enter Python mark: "))
# mysql_mark = int(input("Enter MySQL mark: "))
# django_mark = int(input("Enter Django mark: "))

# total = python_mark + mysql_mark + django_mark
# average = total / 3

# print(f"Total: {total}")
# print(f"Average: {average}")

# if python_mark < 40 or mysql_mark < 40 or django_mark < 40:
#     print("Result: Fail")
# else:
#     print("Result: Pass")

#     if average >= 90:
#         grade = "A+"
#     elif average >= 80:
#         grade = "A"
#     elif average >= 70:
#         grade = "B"
#     elif average >= 60:
#         grade = "C"
#     elif average >= 50:
#         grade = "D"
#     else:
#         grade = "E"

#     print(f"Grade: {grade}")

# ---