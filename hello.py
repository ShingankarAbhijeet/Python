print('Welcome to the world of python')


'''
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dr=dict()
largest=-1
for line in handle:
    line=line.strip()
    wd=line.split()
    if 'From' in wd:
   	    wds=wd[5]
   	    time=wds.split(':')
   	    hrs=time[0]
   	    #print(hrs)
   	    dr[hrs]=dr.get(hrs,0) +1 
#print(dr)
tmp=list()

for k,v  in dr.items():
	newt=(k,v)
	tmp.append(newt)
tmp =sorted(tmp)
for k,v in tmp:
     print(k,v)
'''


       

'''
name=input("Enter file:")
if len(name) < 1:
   name = "mbox-short.txt"
handle=open(name)
dir=dict()
for line in handle:
	line=line.strip()
	wd=line.split()
	#print(wd)
	if 'From' in wd:
	 	wds = wd[1]
	 	#print(wds)
	 	if wds in dir:
	 	   dir[wds] = dir[wds] +1
	 	else:
	 	   dir[wds] = 1
	 	#print(wds,dir[wds])
largest = -1
word=None
for k,v in dir.items():
    if v>largest:
        largest=v
        word=k
print(word,largest)		
'''		
		
    
	


'''
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
	line=line.rstrip()
	wds=line.split()

	if len(wds) < 3 or wds[0] != 'From' :
		
		continue
	else:
	   
 for w in wds:
	   	  print(wds[1])
	   count=count+1	  
	  
         		
print("There were", count, "lines in the file with From as the first word")

'''



'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line=line.rstrip()
	
	wrd=line.split()
	for i in wrd:
		if i in lst:
			continue
		else:
		    lst.append(i)
lst.sort()
print(lst)	
'''

	
	
'''
def lyrx():
	print("zukega nahi sala ")
lyrx()


x=input('provid no1:')
y=input('provide no2:')
if int(x)  > int(y):
	print(x,"is higher")
else:
	print(x, 'is  smaller' )


print('Hello World')

x=input('provid no1:')
y=input('provide no2:')
z= int(x)+int(y) 
print(z)
'''