'''

mystr = "Sky is the limit"
print(len(mystr))
print(mystr[::]) ###  ===> [0:length of string:1] ==> the last  place is for place from string
                 ###                                   bydefault its 1
print(mystr[0:16:1])
print(mystr[::15])
print(mystr[::59])
print(mystr[-4::])  ### ===> from end of the string
print(mystr[-4:0:-2])
print(mystr[12::])
'''
mystr = "sky is the limit"  ### if spaces are there then its not alphanum.
print(mystr.isnumeric())
print(mystr.endswith("limited"))  ### checks the string end
print (mystr.count("i"))  ##### to check count of "i" in sentennce
print(mystr.capitalize())   ### makes first letter capital
print(mystr.find("is"))  ### find from where "is" starts
print(mystr.upper())
print(mystr.lower())
print(mystr.replace("is","was"))