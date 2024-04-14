import random
data=["Rock","Paper","Scissor"]
comp=random.choice(data)
a=int(input("Enter your choice:\n1 for Rock\n2 for Paper\n3 for Scissor\nYour Choice is: "))
print("Computer's choice is",comp)
print("\n")
if (comp=="Rock" and a==1)or(comp=="Paper" and a==2)or(comp=="Scissor" and a==3):
    print("Ohh! its a tie")
if (comp=="Rock" and a==2)or(comp=="Paper" and a==1)or(comp=="Scissor" and a==1):
    print("Unfortunately you've lost. Better luck next time")
if (comp=="Rock" and a==3)or(comp=="Paper" and a==3)or(comp=="Scissor" and a==2):
    print("Congratulations on winning")
