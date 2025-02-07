txt = 'LMaasleitbtui'
car1=[]
car2=[]

for i in range(len(txt)):
    if i%2==0:
        car1.append(txt[i])
    else:
        car2.append(txt[i])


car1=''.join(car1)
car2=''.join(car2)

print(car1, car2)

    


    



