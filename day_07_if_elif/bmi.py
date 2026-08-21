"""
read hiegt_in_cm

read weight_in_kg

set height_in_meter as height_in_cm / 100

set bmi as weight_in_kg / (height_in_meter**2)

chk if bmi < 19 then display  underweight

chk elif bmi > = 19 and bmi < 25 then display normal

chk elif bmi >=25 and bmi < 30 then display overweight

else display obese

"""

height_in_cm = int(input("enter height in cm. "))

weight_in_kg = int(input("enter weight in kg. "))

height_in_meter = height_in_cm / 100

bmi = weight_in_kg / (height_in_meter**2)

print("your bmi is",bmi)
if bmi<19:
    print("underweight")

elif bmi >= 19 and bmi < 25:

    print("normal")

elif bmi>=25 and bmi < 30:

    print("overweight")
else:

    print("obese")