def computepay(h, r):
    if h <= 40:
      gross_pay = h * r
    else :
     gross_pay = ((40 *r) + (h-40) * (1.5* r))
    return gross_pay
h= float(input("hrs"))
r= float(input("rate"))
print(computepay(h, r))
