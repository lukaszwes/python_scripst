#Ciag Fibonazziego

x = int(input('Podaj ilosc elementow ciagu: '))

def Fibonacci (numElements):
    if numElements == 1:
        fibo=[0]
    elif numElements == 2:
        fibo=[0,1]
    elif numElements>2:
        fibo=[0,1]
        for x in range(3, numElements+1):
            fibo.append(fibo[x-3]+fibo[x-2])
    return fibo


print(Fibonacci(x))
    
