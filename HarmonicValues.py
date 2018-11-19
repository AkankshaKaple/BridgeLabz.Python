number = int(input('Enter the number'))
i=1
result=0
for i in range(1,number+1):
    result = result + (1/i)
    print(result)