sentence=input("Int string: ")
replace=input("Replacing word in sentence: ")
replace_with=input("Input the word you want to replace with: ")

if replace.lower() in sentence.lower():
    sentence=sentence.replace(replace, replace_with)

print(sentence)
