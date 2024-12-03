# Q1 : Prime Number Checking

def isPrime(number): 
    for i in range(2,number//2): 
        if number % i == 0 : 
            return False
    return True

print("\nEnter a Number: ",end="")
input_number = int(input())
if isPrime(input_number): 
    print(f"\n{input_number} is a Prime Number.\n")
else: 
    print(f"\n{input_number} is NOT a Prime Number.\n")

# Q2 : Time printing of a 12 hour clock

import time
print("\nPrinting the Clock: \n")
periods = ["AM","PM"]
for period in periods: 
    for hour in range(1,13): 
        for minute in range(61): 
            for seconds in range(61):
                print(f"{hour} : {minute} : {seconds}  {period}")
                time.sleep(1)