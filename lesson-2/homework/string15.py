sentence=input("Enter sentence: ")
acronyms=[]
acronyms.append(sentence[0])

for i in range(len(sentence)):
    if sentence[i]==" ":
        acronyms.append(sentence[i+1])

acronyms="".join(acronyms)
print(acronyms)


        
