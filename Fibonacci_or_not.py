import math

def isPerfectSquare(number):
    squareRoot=int(math.sqrt(number))
    return squareRoot*squareRoot==number
    
def isFibonacci(number):
    return isPerfectSquare(5*number*number+4) or isPerfectSquare(5*number*number-4)

number = int(input())

if isFibonacci(number):
    print(True)
else:
    print(False)