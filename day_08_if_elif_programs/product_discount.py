"""

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
"""

bill_total = int(input("enter bill total... "))


discount = 0

if bill_total < 1000:

    discount = 0

elif bill_total < 5000:

    discount = (10/100)*bill_total

elif bill_total < 10000:

    discount = (20/100)*bill_total

else:

    discount = (30/100)*bill_total


print("Discount",discount)

print("total pay",bill_total-discount)



