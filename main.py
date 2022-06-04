import random

done = False


while not done:
    choice_made=None
    
    computer=random.choice(['R','P', 'S'])
    
    #Accepts user's input
    user_input = input(
    "What's your choice? 'R' for Rock, 'P' for Paper,  'S' for Scissors, 'X' to quit Game\n")
    user_input = user_input.upper()
    
    # Validate user's input
    if user_input =='R':
        print( "Your choice Rock")
        choice_made="valid"
        
    elif user_input =='P':
        print( "Your choice Paper")
        choice_made="valid"
        
    elif user_input =='S':
        print( "Your choice Scissors")
        choice_made="valid"
        
    elif user_input =='X':
        choice_made="quit"
    else:
        print("Invalid input. Please try again!")
        
    #if user inpur is valid. compare with
    # winning conditions: R > S, S > P, P > R
    
    if choice_made=="valid":
        print( f"You have choosen \'{user_input}\' and the computer has chosen \'{computer}\'")  
        
        if (user_input ==computer):
            print("It's a tie!!!")
        else:
            if (user_input == 'R' and computer == 'S') or (user_input == 'S' and computer == 'P') or (user_input== 'P' and computer == 'R'):
                print( "You won!")
            else:
                print("You lost!!")
        
        
    if choice_made=="quit":
        print ("Thanks for Playing")
        done=True
        
    