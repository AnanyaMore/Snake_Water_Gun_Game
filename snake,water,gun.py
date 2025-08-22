import random 

def check(comp,user):
    if (comp == user):
        return 0
    if (comp ==0 and user == 1):
        return -1
    if (comp ==1 and user == 2):
        return -1
    if (comp ==2 and user == 0):
        return -1
    
comp = random.randiant(0,2)
user = int(input("0 for Snake,1 for Water, 2 for Gun \n"))

print("User =" ,user)
print("Computer =",comp)

score = check(comp,user)
if (score ==0 ):
    print("It's Draw")
elif (score == -1):
    print("You Lose")
else:
    print("You Won")    

