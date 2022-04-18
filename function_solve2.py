# quiz 6.1.3
# How to get lotto

import random

def get_random_number():
    number = random.randint(1, 45)
    return number 

lotto_num = []  # lotto number storage location list

for i in range(6):
    random_number = get_random_number() # execute function get_random_number() by random_number
    lotto_num.append(random_number) # add data in lotto_num until i = 6.

lotto_num.sort()    # ascending order    
for num in lotto_num:
    print(num, end = " ")

print("\n")
    
# if you allow duplication, That is right code. But We don't allow duplication.

def get_random_number1():
    number1 = random.randint(1, 45)
    return number1 

lotto_num1 = []  

count = 0 # current number selected

while True:
    if count == 6:  # count = 6, break
        break
    random_number1 = get_random_number1()
    if random_number1 not in lotto_num1: # if same random_number1 doesn't not exist in lotto_num1 
        lotto_num1.append(random_number1)   # add random_number1
        count += 1

lotto_num1.sort()    # ascending order    
for num1 in lotto_num1:
    print(num1, end = " ")

    
