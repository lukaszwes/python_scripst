#Ciag Fibonazziego

x = int(input('Podaj ilosc elementow ciagu: '))

def Fibonacci (numElements):
    first, second = 0, 1
    fibo = []
    for _ in range(numElements):
        first, second = second, first + second
        fibo.append(first)
    return fibo


print(Fibonacci(x))
    
