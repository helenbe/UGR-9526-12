def collatzConjecture(number):
    print("The squence which starts by",number,"is: ")
    while(number != 1):
        print(int(number),end=" ")
        if(number%2==0):
            number /=2
        else:
            number = 3*number + 1
    print(int(number))
def numDigit(num):
    org=num
    total=1
    while(num//10>1):
        total=total+1
        num=num//10
    print("The number",org,"has",total,"digits")
def freqOfNum(number,test):
    number=str(number)
    test=str(test)
    freq=0
    for i in number:
        if i==test:
            freq=freq+1
    print("the number",test,"is",freq,"times repeated in the number",number)
def v(n):
    fs=0
    sp=2*(n-2)
    for i in range(n-1):
        print(fs*" ","\\",sp*" ","/")
        fs+=1
        sp=sp-2
    print(fs*" ","\\/")
num1=eval(input("Enter a number for the collatz conjecture sequence: "))
collatzConjecture(num1)
num2=eval(input("Enter a number: "))
numDigit(num2)
num3=eval(input("Enter a number: "))
num4=eval(input("Enter a single number: "))
freqOfNum(num3,num4)
num5=eval(input("Enter number of line for V: "))
v(num5)
    
    
