vowels='aeiou'
consonantes='bcdfghjklmnpqrstvwxyz'

vowel_list=[]
consonantes_list=[]
others=[]

word=input("Enter whatever word you want: ")

for char in word:
    if char in vowels:
        vowel_list.append(char)
    elif char in consonantes:
        consonantes_list.append(char)
    else:
        others.append(char)

print(f"There is {len(vowel_list)} vowels in the word {word} and they are:\n>>> {vowel_list}")
print(f"There is {len(consonantes_list)} consonantes in the word {word} and they are:\n>>> {consonantes_list}")
print(f"There is {len(others)} other type of symbols in the word {word} and they are:\n>>> {others}")