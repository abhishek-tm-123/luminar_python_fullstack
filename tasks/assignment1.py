"""PYTHON SCENARIO-BASED PRACTICE QUESTIONS
Topics: print(), input(), Arithmetic Operators, Relational Operators

============================================================
LEVEL 1 Ã¢â‚¬â€ VERY BASIC
============================================================

1. SHOPPING BILL

A customer buys a notebook and a pen. Take the price of the notebook
and pen as input and display the total amount.

Sample Input:
Notebook price: 50
Pen price: 20

Sample Output:
Total amount: 70"""


"""notebook_price=int(input("Enter notebook price:"))
pen_price=int(input("Enter pen price:"))"""

"""total_amount=notebook_price+pen_price
print("total amount:",total_amount)"""

"""2. STUDENT MARKS

Take marks of 3 subjects as input and display the total marks and average.

Sample Input:
Python: 80
MySQL: 70
Django: 90

Sample Output:
Total marks: 240
Average: 80.0"""

"""python_marks=int(input("Enter mark for python:"))
mySQL_marks=int(input("Enter mark for mySQL:"))
Django_marks=int(input("Enter mark for Django:"))

total_marks=python_marks+mySQL_marks+Django_marks
avg=total_marks/3
print("Total marks:",total_marks)
print("Average:",avg)"""

"""3. MOVIE TICKETS

A movie ticket costs Ã¢â€šÂ¹180. Ask the user for the number of tickets
and calculate the total amount.

Sample Input:
Ticket price: 180
Number of tickets: 4

Sample Output:
Total amount: 720"""

"""ticket_price=180
no_tickets=int(input("Enter number of tickets:"))

total_amount=ticket_price*no_tickets
print("Total amount:",total_amount)"""

"""4. MOBILE RECHARGE

A person has Ã¢â€šÂ¹500 in their account and spends Ã¢â€šÂ¹175 on recharge.
Calculate how much money is remaining.

Sample Input:
Balance: 500
Recharge amount: 175

Sample Output:
Remaining balance: 325"""

"""balance=500
recharge_amount=175

remaining=balance-recharge_amount

print("remaining balance",remaining)"""

"""5. TEMPERATURE CONVERSION

Take temperature in Celsius and convert it to Fahrenheit.

Formula:
F = (C Ãƒâ€” 9/5) + 32

Sample Input:
Celsius: 30

Sample Output:
Fahrenheit: 86.0"""

"""C=int(input("Enter a celsius:"))

F = (C * 9/5) + 32
print("Fahrenheit:",F)"""

"""============================================================
LEVEL 2 Ã¢â‚¬â€ ARITHMETIC + RELATIONAL OPERATORS
============================================================"""

"""6. AGE COMPARISON

Take the ages of two people and check whether both people are
of the same age.

Sample Input:
Age of person 1: 25
Age of person 2: 25

Sample Output:
Both people are the same age: True"""

"""Age1=int(input("Enter age of person 1:"))
Age2=int(input("Enter age of person 2:"))
same_age=Age1==Age2
print("Both people are the same age:", same_age)"""

"""7. EXAM RESULT CHECK

Take a student's marks and check whether the marks are greater
than or equal to 40.

Sample Input:
Marks: 65

Sample Output:
Passed: True"""

"""Marks=int(input("Enter marks:"))
passed=Marks>=40
print("Passed:",passed)"""

"""8. DRIVING ELIGIBILITY

Take a person's age and check whether the age is greater than
or equal to 18.

Sample Input:
Age: 20

Sample Output:
Eligible to drive: True"""

"""Age=int(input("Enter age:"))
eligible=Age>=18
print("Eligible to drive:",eligible)"""

"""9. PRODUCT PRICE COMPARISON

Take the prices of two products and check whether the first product
is more expensive than the second product.

Sample Input:
Product 1 price: 1500
Product 2 price: 1200

Sample Output:
Product 1 is more expensive: True"""

"""Product1_price=int(input("Enter product 1 price:"))
Product2_price=int(input("Enter product 2 price:"))
more_expensive=Product1_price>Product2_price
print("Product 1 is more expensive:",more_expensive)"""

"""10. PASSWORD LENGTH

Take a number representing the length of a password. Check whether
the password length is at least 8 characters.

Sample Input:
Password length: 10

Sample Output:
Password is long enough: True"""

"""Password_length=int(input("Enter password length:"))
long_enough=Password_length>=8
print("Password is long enough:",long_enough)"""



"""============================================================
LEVEL 3 Ã¢â‚¬â€ REAL-WORLD SCENARIOS
============================================================"""

"""11. RESTAURANT BILL

A restaurant bill contains food, drinks and dessert.
Take these values as input and calculate:
- Total bill
- Whether the bill is greater than Ã¢â€šÂ¹700

Sample Input:
Food: 450
Drinks: 150
Dessert: 200

Sample Output:
Total bill: 800
Bill is greater than 700: True"""

"""Food=int(input("Enter food price:"))
Drinks=int(input("Enter drinks price:"))
Dessert=int(input("Enter dessert price:"))
Total_bill=Food+Drinks+Dessert
Greater_than_700=Total_bill>700
print("Total bill:",Total_bill)
print("Bill is greater than 700:",Greater_than_700)"""

"""12. SALARY CALCULATION

Take an employee's basic salary, travel allowance and food allowance.
Calculate the total salary.

Sample Input:
Basic salary: 25000
Travel allowance: 3000
Food allowance: 2000

Sample Output:
Total salary: 30000"""

"""Basic_salary=int(input("Enter basic salary:"))
Travel_allowance=int(input("Enter travel allowance:"))
Food_allowance=int(input("Enter food allowance:"))
Total_salary=Basic_salary+Travel_allowance+Food_allowance
print("Total salary:",Total_salary)"""

"""13. SHOPPING DISCOUNT

Take the original price and discount amount as input.
Calculate the final price.

Sample Input:
Original price: 2000
Discount: 300

Sample Output:
Final price: 1700"""

"""Orginal_price=int(input("Enter original price:"))
Discount=int(input("Enter discount:"))
Final_price=Orginal_price-Discount
print("Final price:",Final_price)"""


"""14. BANK BALANCE

Take the current balance and withdrawal amount.
Calculate the remaining balance and check whether the remaining
balance is greater than or equal to Ã¢â€šÂ¹1000.

Sample Input:
Current balance: 5000
Withdrawal amount: 2500

Sample Output:
Remaining balance: 2500
Balance is at least 1000: True"""

"""Current_balance=int(input("Enter current balance:"))
Withdrawal_amount=int(input("Enter withdrawal amount:"))
Remaining_balance=Current_balance-Withdrawal_amount
Balance_at_least_1000=Remaining_balance>=1000
print("Remaining balance:",Remaining_balance)
print("Balance is at least 1000:",Balance_at_least_1000)"""

"""15. ELECTRICITY BILL

Take the number of units consumed and the price per unit.
Calculate the electricity bill. Also check whether the bill
is greater than Ã¢â€šÂ¹1000.

Sample Input:
Units consumed: 250
Price per unit: 5

Sample Output:
Electricity bill: 1250
Bill is greater than 1000: True"""

"""Unit_consumed=int(input("Enter units consumed:"))
Price_per_unit=int(input("Enter price per unit:"))
Electricity_bill=Unit_consumed*Price_per_unit
Bill_is_greater_than_1000=Electricity_bill>1000
print("Electricity bill:",Electricity_bill)
print("Bill is greater than 1000:",Bill_is_greater_than_1000)"""

"""============================================================
LEVEL 4 Ã¢â‚¬â€ THINKING QUESTIONS
============================================================"""

"""16. COMPARE TWO STUDENTS

Take the marks of Student A and Student B.

Display:
- Student A's total
- Student B's total
- Whether both students got the same marks
- Whether Student A scored more than Student B

Sample Input:
Student A marks: 85
Student B marks: 75

Sample Output:
Student A marks: 85
Student B marks: 75
Both students have the same marks: False
Student A scored more: True"""

"""StudentA_marks=int(input("Enter Student A marks:"))
StudentB_marks=int(input("Enter Student B marks:"))
StudentA_total=StudentA_marks
StudentB_total=StudentB_marks
print("Student A marks:", StudentA_total)
print("Student B marks:", StudentB_total)
Both_students_same=StudentA_total==StudentB_total
StudentA_scored_more=StudentA_total>StudentB_total
print("Both students have the same marks:", Both_students_same)
print("Student A scored more:", StudentA_scored_more)"""

"""17. TRAVEL EXPENSE

A person travels using a car.

Take:
- Distance travelled
- Mileage of the car
- Petrol price

Calculate approximately how much money was spent on fuel.

Formula:
Fuel consumed = Distance / Mileage
Fuel cost = Fuel consumed Ãƒâ€” Petrol price

Sample Input:
Distance: 300
Mileage: 15
Petrol price: 100

Sample Output:
Fuel consumed: 20.0
Fuel cost: 2000.0"""

"""Distance=int(input("Enter distance travelled:"))
Mileage=int(input("Enter mileage of the car:"))
Petrol_price=int(input("Enter petrol price:"))
Fuel_consumed=Distance/Mileage
Fuel_cost=Fuel_consumed*Petrol_price
print("Fuel consumed:", Fuel_consumed)
print("Fuel cost:", Fuel_cost)"""

"""18. EMPLOYEE SALARY

Take:
- Basic salary
- Bonus
- Deduction

Calculate:

Final Salary = Basic Salary + Bonus - Deduction

Then check whether the final salary is greater than Ã¢â€šÂ¹30,000.

Sample Input:
Basic salary: 28000
Bonus: 5000
Deduction: 2000

Sample Output:
Final salary: 31000
Salary is greater than 30000: True
"""
"""Basic_salary=int(input("Enter basic salary:"))
Bonus=int(input("Enter bonus:"))
Deduction=int(input("Enter deduction:"))
Final_salary=Basic_salary+Bonus-Deduction
Salary_is_greater_than_30000=Final_salary>30000
print("Final salary:", Final_salary)
print("Salary is greater than 30000:", Salary_is_greater_than_30000)"""

"""19. ONLINE SHOPPING

Take:
- Product price
- Quantity
- Delivery charge

Calculate the final bill. Then check whether the final bill
is greater than Ã¢â€šÂ¹5000.

Sample Input:
Product price: 1500
Quantity: 4
Delivery charge: 200

Sample Output:
Final bill: 6200
Bill is greater than 5000: True"""

"""Product_price=int(input("Enter product price:"))
Quantity=int(input("Enter quantity:"))
Delivery_charge=int(input("Enter delivery charge:"))
Final_bill=Product_price*Quantity+Delivery_charge
Bill_is_greater_than_5000=Final_bill>5000
print("Final bill:", Final_bill)
print("Bill is greater than 5000:", Bill_is_greater_than_5000)"""

"""20. CLASSROOM ASSESSMENT

Take marks of a student in:
- Python
- MySQL
- Django

Calculate:
- Total
- Average
- Whether the total is greater than or equal to 150
- Whether Python marks are greater than MySQL marks

Sample Input:
Python: 70
MySQL: 60
Django: 80

Sample Output:
Total: 210
Average: 70.0
Total is greater than or equal to 150: True
Python marks are greater than MySQL marks: True"""

"""Python_marks=int(input("Enter python marks:"))
MySQL_marks=int(input("Enter mySQL marks:"))
Django_marks=int(input("Enter Django marks:"))
Total=Python_marks+MySQL_marks+Django_marks
Average=Total/3
Total_greater_than_or_equal_150=Total>=150
Python_greater_than_MySQL=Python_marks>MySQL_marks
print("Total:", Total)
print("Average:", Average)
print("Total is greater than or equal to 150:", Total_greater_than_or_equal_150)
print("Python marks are greater than MySQL marks:", Python_greater_than_MySQL)"""

"""============================================================
BONUS CHALLENGE
============================================================"""

"""21. ONLINE SHOPPING Ã¢â‚¬â€ COMPLETE SCENARIO

A customer purchases 3 shirts. Each shirt costs Ã¢â€šÂ¹750.
The customer also pays Ã¢â€šÂ¹100 delivery charge.

Take the shirt price, quantity and delivery charge as input.
Calculate the total bill. Then check whether the total bill
is greater than Ã¢â€šÂ¹2000.

Sample Input:
Shirt price: 750
Quantity: 3
Delivery charge: 100

Sample Output:
Total bill: 2350
Bill is greater than 2000: True
"""
"""Shirt_price=int(input("Enter shirt price:"))
Quantity=int(input("Enter quantity:"))
Delivery_charge=int(input("Enter delivery charge:"))
Total_bill=Shirt_price*Quantity+Delivery_charge
Bill_is_greater_than_2000=Total_bill>2000
print("Total bill:", Total_bill)
print("Bill is greater than 2000:", Bill_is_greater_than_2000)"""

"""IMPORTANT:
Do not use if/else, loops, functions, lists or other topics
that have not yet been taught.

Focus only on:
- input()
- print()
- Variables
- +, -, *, / arithmetic operators
- >, <, >=, <=, ==, != relational operators"""