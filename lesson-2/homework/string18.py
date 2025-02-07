sentence=input("Enter any sentence: ")

starts_with=sentence.split()[0]
ends_with=sentence.split()[-1]

print(f"Input: {sentence}")
print(f"Starts with: {starts_with}")
print(f"Ends with: {ends_with}")