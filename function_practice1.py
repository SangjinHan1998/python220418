# basic
# 1. definition
def printHello():
    print("Hello hahaha")

# 2. call
printHello()

# function having parameter
def sum(a, b):
    print(a + b)
    
sum(33, 44) # 33은 a, 44는 b로 들어간다. 

# 3. function having return value
import random
def getRandomNumber():
    number = random.randint(1, 10)
    return number 

print(getRandomNumber())

# function having parameter and return-value
def add(a, b):
    result = a + b
    return result

print(add(5, 51))