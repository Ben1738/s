#! python3

# SD Computing Studies Assignment
import random

b=random.randint(0,100)


d=str(range(0,999999))


for i in d:
    a=int(input("guess number 1-100:"))
    if a==b:
        print("YES!")
        quit()
    if a>b:
        print('NO DUMBASS, LOWER!')
    if a<b:
        print('NO DUMBASS, HIGHER!')






