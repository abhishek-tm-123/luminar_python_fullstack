"""
read cibil_score

chk if cibil_score < 550 then display poor
chk elif cibil_score >=550 and cibil_score < 650 display average
chk elif cbil_score >=650 and cibil_score < 750 diaply Good
else display excellent


"""


cibil_score = int(input("enter cibil score"))

if cibil_score < 550:
    
    print("POOR")

elif cibil_score>=550 and cibil_score<650:

    print("average")

elif cibil_score >=650 and cibil_score<750:

    print("Good")

else:

    print("excellent...")