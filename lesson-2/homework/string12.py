strings=[]

while True:
    string=input("Enter String: ")
    if string=="":
        break
    else:
        strings.append(string)

strings=",".join(strings)
print(strings)
