print('Enter a number')
num = input()
numint = int(num)

if(numint>0):
    print(num, 'is a positive number')

elif(numint==0):
    print(num, 'is neither a negative integer nor a positive integer')

elif(numint<0):
    print(num, 'is a negative integer')

else:
    print('An exception has occured at posneg.py 15:5')
