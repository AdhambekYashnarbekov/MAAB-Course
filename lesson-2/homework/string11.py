digits="0123456789"
string=input("Enter any string: ")
answer=" "
digits_in_string=[]

for char in string:
    if char in digits:
        digits_in_string.append(char)
        answer="String has digits"
    else:
        answer="String has no digits"

print(answer)
print(f"Digits in string: {digits_in_string}")

