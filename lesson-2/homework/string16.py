string=input("Input the word: ")
character=input("input any character in alphabet: ")
string1=[]

for char in string:
    if char.title()==character.title():
        continue
    else:
        string1.append(char)

string="".join(string1)
print(string)
