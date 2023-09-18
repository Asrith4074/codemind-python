def is_happy_number(number):
    visited=set()
    
    while True:
        if number==1:
            return True
        elif number in visited:
            return False
        else:
            visited.add(number)
            number=sum(int(digit)**2 for digit in str(number))
number=int(input())
if is_happy_number(number):
    print(True)
else:
    print(False)