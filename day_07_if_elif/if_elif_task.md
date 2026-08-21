# Python If–Elif–Else Assessment



# LEVEL 1 – Basic If / Else

## Question 1 – Positive or Negative

Write a program to check whether a number is positive or negative.

### Sample Input

```text
Enter number: 25
```

### Sample Output

```text
Positive number
```

---

## Question 2 – Even or Odd

Write a program to check whether a number is even or odd.

### Sample Input

```text
Enter number: 18
```

### Sample Output

```text
Even number
```

---

## Question 3 – Eligible to Vote

Write a program to check whether a person is eligible to vote.

Age must be 18 or above.

### Sample Input

```text
Enter age: 21
```

### Sample Output

```text
Eligible to vote
```

---

## Question 4 – Pass or Fail

Write a program to check whether a student has passed an examination.

A student passes if the mark is 40 or above.

### Sample Input

```text
Enter mark: 65
```

### Sample Output

```text
Passed
```

---

## Question 5 – Greater Number

Write a program to compare two numbers and display which number is greater.

### Sample Input

```text
Enter first number: 25
Enter second number: 18
```

### Sample Output

```text
25 is greater
```

---

# LEVEL 2 – Introducing Elif

## Question 6 – Positive, Negative or Zero

Write a program to check whether a number is:

* Positive
* Negative
* Zero

### Sample Input

```text
Enter number: -10
```

### Sample Output

```text
Negative
```

---

## Question 7 – Grade Calculator

Write a program to display the grade based on the mark.

| Mark     | Grade |
| -------- | ----- |
| 90–100   | A     |
| 75–89    | B     |
| 60–74    | C     |
| 40–59    | D     |
| Below 40 | F     |

### Sample Input

```text
Enter mark: 82
```

### Sample Output

```text
Grade B
```

---

## Question 8 – Age Category

Write a program to identify a person's age category.

| Age         | Category       |
| ----------- | -------------- |
| 0–12        | Child          |
| 13–19       | Teenager       |
| 20–59       | Adult          |
| 60 or above | Senior Citizen |

### Sample Input

```text
Enter age: 16
```

### Sample Output

```text
Teenager
```

---

## Question 9 – Temperature

Write a program to classify the temperature.

| Temperature | Result |
| ----------- | ------ |
| Below 15    | Cold   |
| 15–30       | Normal |
| Above 30    | Hot    |

### Sample Input

```text
Enter temperature: 35
```

### Sample Output

```text
Hot
```

---

## Question 10 – Number Comparison

Write a program to compare two numbers.

Display:

* First number is greater
* Second number is greater
* Both numbers are equal

### Sample Input

```text
Enter first number: 25
Enter second number: 25
```

### Sample Output

```text
Both numbers are equal
```

---

# LEVEL 3 – Multiple Conditions

## Question 11 – Electricity Bill Category

Write a program to display the electricity usage category.

| Units     | Category        |
| --------- | --------------- |
| 0–100     | Low Usage       |
| 101–300   | Medium Usage    |
| 301–500   | High Usage      |
| Above 500 | Very High Usage |

### Sample Input

```text
Enter units: 350
```

### Sample Output

```text
High Usage
```

---

## Question 12 – Simple Calculator

Get two numbers and an operator from the user.

Supported operators:

* `+`
* `-`
* `*`
* `/`

Use `if`, `elif`, and `else` to perform the operation.

### Sample Input

```text
Enter first number: 20
Enter second number: 5
Enter operator: /
```

### Sample Output

```text
Result: 4.0
```

---

## Question 13 – Traffic Signal

Get a traffic signal color from the user.

* `red` → Stop
* `yellow` → Get Ready
* `green` → Go
* Anything else → Invalid signal

### Sample Input

```text
Enter signal: green
```

### Sample Output

```text
Go
```

---

## Question 14 – Day Number

Get a number from 1 to 7 and display the corresponding day.

| Number | Day       |
| ------ | --------- |
| 1      | Monday    |
| 2      | Tuesday   |
| 3      | Wednesday |
| 4      | Thursday  |
| 5      | Friday    |
| 6      | Saturday  |
| 7      | Sunday    |

### Sample Input

```text
Enter day number: 6
```

### Sample Output

```text
Saturday
```

---

## Question 15 – Month Number

Get a month number from the user and display the month name.

### Sample Input

```text
Enter month number: 8
```

### Sample Output

```text
August
```

If the number is not between 1 and 12:

```text
Invalid month
```

---

# LEVEL 4 – Real-World Problems

## Question 16 – ATM Withdrawal

Write a program for a simple ATM withdrawal.

Get:

* Account balance
* Withdrawal amount

Rules:

* If withdrawal amount is greater than balance → Insufficient balance
* Otherwise → Withdrawal successful

### Sample Input

```text
Enter balance: 10000
Enter withdrawal amount: 3000
```

### Sample Output

```text
Withdrawal successful
Remaining balance: 7000
```

---

## Question 17 – Login System

Create a simple login system.

Correct credentials:

```text
username = admin
password = 1234
```

If both are correct:

```text
Login successful
```

Otherwise:

```text
Invalid username or password
```

### Sample Input

```text
Enter username: admin
Enter password: 1234
```

### Sample Output

```text
Login successful
```

---

## Question 18 – Shopping Discount

Get the shopping amount.

Apply discounts:

| Amount         | Discount    |
| -------------- | ----------- |
| Below 1000     | No discount |
| 1000–4999      | 10%         |
| 5000–9999      | 20%         |
| 10000 or above | 30%         |

Display the discount amount and final amount.

### Sample Input

```text
Enter amount: 6000
```

### Sample Output

```text
Discount: 1200
Final amount: 4800
```

---

## Question 19 – Movie Ticket Price

Get the person's age.

Ticket prices:

* Below 5 → Free
* 5–12 → ₹100
* 13–59 → ₹200
* 60 or above → ₹120

### Sample Input

```text
Enter age: 65
```

### Sample Output

```text
Ticket price: ₹120
```

---

## Question 20 – Salary Bonus

Get an employee's salary and years of experience.

Rules:

* Experience below 2 years → No bonus
* 2–5 years → 5% bonus
* 6–10 years → 10% bonus
* Above 10 years → 15% bonus

### Sample Input

```text
Enter salary: 40000
Enter experience: 7
```

### Sample Output

```text
Bonus: 4000
Total salary: 44000
```

---

# LEVEL 5 – Challenge Questions

## Question 21 – Triangle Type

Get three sides of a triangle.

Determine whether the triangle is:

* Equilateral
* Isosceles
* Scalene

### Sample Input

```text
Enter side 1: 5
Enter side 2: 5
Enter side 3: 5
```

### Sample Output

```text
Equilateral triangle
```

---

## Question 22 – Leap Year

Write a program to check whether a given year is a leap year.

### Sample Input

```text
Enter year: 2024
```

### Sample Output

```text
2024 is a leap year
```

For example:

```text
Enter year: 2023
```

Output:

```text
2023 is not a leap year
```

---

## Question 23 – BMI Category

Get a person's:

* Weight in kilograms
* Height in meters

Calculate BMI using:

```text
BMI = weight / (height * height)
```

Classify the result:

| BMI         | Category    |
| ----------- | ----------- |
| Below 18.5  | Underweight |
| 18.5–24.9   | Normal      |
| 25–29.9     | Overweight  |
| 30 or above | Obese       |

### Sample Input

```text
Enter weight: 70
Enter height: 1.75
```

### Sample Output

```text
BMI: 22.86
Category: Normal
```

---

## Question 24 – Electricity Bill Calculator

Create an electricity bill calculator.

Units consumed:

* First 100 units → ₹5/unit
* Next 200 units → ₹7/unit
* Next 200 units → ₹10/unit
* Above 500 units → ₹15/unit

Calculate the total electricity bill.

### Sample Input

```text
Enter units: 350
```

### Sample Output

```text
Electricity Bill: ₹2000
```

> **Important:** This question requires you to understand how conditions can control different calculations, not just display messages.

---

## Question 25 – Student Result System

Create a complete student result system.

Get marks for:

* Python
* MySQL
* Django

Calculate:

```text
Total
Average
```

Then determine the result.

### Rules

If **any subject mark is below 40**:

```text
Result: Fail
```

Otherwise calculate the average:

| Average  | Grade |
| -------- | ----- |
| 90–100   | A+    |
| 80–89    | A     |
| 70–79    | B     |
| 60–69    | C     |
| 50–59    | D     |
| Below 50 | E     |

### Sample Input

```text
Enter Python mark: 85
Enter MySQL mark: 78
Enter Django mark: 92
```

### Sample Output

```text
Total: 255
Average: 85.0
Result: Pass
Grade: A
```

---
