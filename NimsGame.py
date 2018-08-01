import random
def userPlay(marbles):
    numOfMarbles = int(input("Please enter the number of marbles: "))
    while numOfMarbles > marbles//2:
        numOfMarbles = int(input('Wrong, Please enter the number of marbles: '))
    return numOfMarbles


def playNovice(marbles):
    numOfMarbles = random.randint(1,marbles//2)
    return numOfMarbles


def playExpert(marbles):
    n = int(input("number of marbles"))
    numOfMarbles = marbles - ((2**n)-1) 
    return marbles - numOfMarbles 
                
marbles = 100
Turn = input("Enter the person playing")
Mode = input("Enter the mode")

while marbles > 1:
    if Turn == 'User':
        userTake = userPlay(marbles)
        marbles = marbles - userTake
        print("The number of marbles is: ", marbles)
        Turn = 'Computer'
    elif Mode == 'Novice':
        compTake = playNovice(marbles)
        marbles = marbles - compTake
        print("The number of marbles is: ", marbles)
        Turn = 'User'
    else:
        Turn == 'Computer'
        marbles = playExpert(marbles)
        print("The number of marbles is: ", marbles)                
print("The winner is ", Turn)
