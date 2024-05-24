import random

print("First to three wins!\n")
user_score=0
opponent_score=0
while(1):
    print("Enter the choice \n 1. Rock\n 2. Paper\n 3. Scissors")
    opt=int(input())
    while opt>3 or opt<1:
        opt=int(input("Enter again!"))
    opponent=random.randint(1,3)
    
    if(opponent==1):
        print("Computer entered Rock")
    elif(opponent==2):
        print("Computer entered Paper")
    else:
        print("Computer entered Scissors")



    if opt==1 and opponent==2:
        opponent_score=opponent_score+1
    elif opt==1 and opponent==3:
        user_score=user_score+1
    elif opt==2 and opponent==1:
        user_score=user_score+1
    elif opt==2 and opponent==3:
        opponent_score=opponent_score+1
    elif opt==3 and opponent==1:
        opponent_score=opponent_score+1
    elif opt==3 and opponent==2:
        user_score=user_score+1
    else:
        print("No point in this round!\n")
    
    print("Score: \n Player : "+str(user_score)+"\n Computer "+str(opponent_score) )

    if user_score==3:
        print("Player Won!!")
        break    
    if opponent_score==3:
        print("Computer Won!!")
        break

            
        


