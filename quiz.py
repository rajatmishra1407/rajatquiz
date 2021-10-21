correct=0
def sum(a,b):
    print("enter the correct answer ")
    print(a,"+ ",b,end="=")
    k=int(input())
    if k==a+b:
        print("correct answer ")
        global correct
        correct=correct+1
    else:
        print("incorrect answer ")
def sub(a,b):
    print("enter the correct answer ")
    print(a,"- ",b,end="=")
    k=int(input())
    if k==a-b:
        print("correct answer ")
        global correct
        correct+=1
    else:
        print("incorrect answer ")

def mul(a,b):
    print("enter the correct answer ")
    print(a,"* ",b,end="=")
    k=int(input())
    if k==a*b:
        print("correct answer ")
        global correct
        correct+=1
    else:
        print("incorrect answer ")

def div(a,b):
    print("enter the correct answer ")
    print(a,"/ ",b,end="=")
    k=int(input())
    if k==a/b:
        print("correct answer ")
        global correct
        correct+=1
    else:
        print("incorrect answer ")

n=0    
import random as r
import sys as k
print("1.sum")
print("2.subtract ")
print("3.multiplication")
print("4.division")
print("5.exit")
while(True):
    choice=int(input("enter the choice "))
    if choice==1:
        a=r.randint(1,100)
        b=r.randint(1,100)
        n+=1
        sum(a,b)
    elif choice==2:
        a=r.randint(1,100)
        b=r.randint(1,100)
        n+=1
        sub(a,b)
    elif choice==3:
        a=r.randint(1,100)
        b=r.randint(1,100)
        n+=1
        mul(a,b)
    elif choice==4:
        a=r.randint(1,100)
        b=r.randint(1,100)
        n+=1
        div(a,b)
    elif choice==5:
        print("exit the quiz.")
        print("-"*20)
        print("you answered ",n,"questions with ",correct,"correct.")
        print("your scored is ",(correct/n)*100,"%.")
        print("THANK YOU.")
        k.exit(1)
    else:
        print("wrong choice try again:")

    
    


            
