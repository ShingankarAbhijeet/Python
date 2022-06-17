#### Create a dictionary & take input from user & return the meaning of the word from dictionary####

dict= {"dexter":"skillful","gamous":"marrige","devops":"way of life","automation":"ansible","suits":"power"}
print(dict)
print("whats the word you are looking for?")
input= input()
#print(input)
print(dict.get(input))