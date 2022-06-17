 ### Program to   print total count & avg of user input nos. for infinte iterations  ####
num = 0
tot = 0
while True:
 sval = input('Enter no:')
 if sval == 'done':
  break
 try:
  fval = float(sval)
 except:
  print('Invalid input')
  continue
 num = num + 1
 tot = tot + fval
print(tot,num,tot/num)
