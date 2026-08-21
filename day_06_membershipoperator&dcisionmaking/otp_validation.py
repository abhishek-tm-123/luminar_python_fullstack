"""
set db_otp as 3465

read otp 

chk if db_otp == otp then 
    display otp has been verifed
else then
    display invalid otp


"""

DB_OTP = 3465

otp = int(input("enter otp"))

if otp == DB_OTP:

    print("otp has been verified...")

else:

    print("invalid otp")