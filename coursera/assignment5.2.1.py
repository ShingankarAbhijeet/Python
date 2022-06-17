### Program to take user input & print smallest & largest no. ###
largest = None
smallest = None
while True:
    num = input('Enter no:')
    if num == 'done' :
         break
    try:
        sval = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = num
    elif int(largest) < sval:
        largest = sval
    if smallest is None:
        smallest = num
    elif sval < int(smallest):
        smallest = sval
print("Maximum is",largest)
print("Minimum is",smallest)
