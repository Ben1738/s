#! python3

# SD Computing Studies Assignment
import random

b=random.randint(0,1)


a=input("Heads or Tails: ")
    
    
if a=='Heads' or a=='heads':
    if b==0:
        print("YAYYYYYYYY!")
        quit()
    if b==1:
        print('NO I HATe YOU!')
        quit()


if a=='Tails' or a=='tails':
    if b==1:
        print("YAYYYYYYYY!")
        quit()
    if b==0:
        print('NO I HATe YOU!')
        quit()

else:
    print('FUCK YOU, THAT IS NOT HEADS OR TAILS!!!!')
    quit()
