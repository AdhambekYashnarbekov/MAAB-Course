sentence=input("Input the sentence: ")
count=1

for space in sentence:
    if space==" ":
        count+=1

print(f"Sentence has {count} words.")
