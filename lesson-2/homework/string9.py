string=input("Input string: ")
reverse=[]

for i in range(1, len(string)+1):
    reverse.append(string[-i])

reverse="".join(reverse)
print(reverse)
