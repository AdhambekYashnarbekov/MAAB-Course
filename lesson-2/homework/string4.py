word=input("Input a word: ")

word2=[]

for i in range(1, len(word)+1):
    word2.append(word[-i])

word2="".join(word2)


if word==word2:
    print("Polindrome")
else:
    print("Not polindrome")