hrs = input("Enter Hours:",)
rate = input("Enter hourly rate:",)
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Please Enter numeric input")
    quit()
if h <= 40:
    gross_pay = h * r
else :
     gross_pay = ((40 *r) + (h-40) * (1.5* r))
print( gross_pay)