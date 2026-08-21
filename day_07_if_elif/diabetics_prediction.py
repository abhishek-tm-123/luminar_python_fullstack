"""
sl<100 => normal

100-sl-125 => prediabetes

sl>125=>diabetic

read sugar_level

ch if sugar_level < 100 then display normal

chk elif sugar_level >= 100 and sugar_level <=125 then display prediabtes

else display diabetic

"""

sugar_level = int(input("enter sugar level"))

if sugar_level<100:

    print("Normal")

elif sugar_level>=100 and sugar_level <=125:

    print("prediabete")

else:
    print("diabetic")