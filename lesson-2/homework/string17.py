vowels="aeiou"
string2=[]

string=input("Int any string: ")

for char in string:
    if char in vowels:
        string2.append("*")
    else:
        string2.append(char)

string="".join(string2)
print(string)
