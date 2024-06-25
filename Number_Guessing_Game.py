import random as r

game_active = True
stage_1 = False
stage_2 = False

print('Welcome to the higher/lower game!')




while game_active == True:
    while stage_1 == False:
        lower_b = int(input('Enter the lower bound:'))
        upper_b = int(input('Enter the upper bound:'))
        if lower_b >= upper_b:
            print(f"I'm sorry, but it seems that the lower bound of {lower_b} is greator or equal to the upper bound of {upper_b}")
            print('Try again, but make sure the lower bound is less than the upper bounds by MORE than 1')
        elif lower_b + 1 == upper_b:
            print(f"I'm sorry, but it seems that the lower bound of {lower_b} is with in 1 of the upper bound of {upper_b}")
            print('Try again, but make sure the lower bound is less than the upper bounds by MORE than 1')
        else:
            stage_1 = True
            lower_b_between = lower_b + 1
            upper_b_between = upper_b - 1
            target_number = r.randint(lower_b_between,upper_b_between)
            stage_2 = True

    guesses = 0
    play_again = None

    while stage_2 == True:
        if guesses == 0:
            guess = int(input(f'Great, now guess a number between {lower_b} and {upper_b}:'))
            guesses += 1
            if guess == target_number:
                print('You got it first try!! Congrats!')
                while play_again == None:
                    play_again = input('Play again? (yes or no):')
                    if play_again == 'yes':
                        stage_2 = False
                        stage_1 = False
                    elif play_again == 'no':
                    
                        stage_1 = True
                        stage_2 = False
                        game_active = False
                    else:
                        print('Invalid input.\n')
                        play_again = None
                
            elif guess < target_number:
                print('Nope, too low.')
            elif guess > target_number:
                print('Nope, too high.')
        else:
            
            guess = int(input(f'Guess again. The number is between {lower_b} and {upper_b}:'))
            guesses += 1
            if guess == target_number:
                print('You got it!')
                while play_again == None:
                    play_again = input('Play again? (yes or no):')
                    if play_again == 'yes':
                        stage_2 = False
                        stage_1 = False
                    elif play_again == 'no':
                    
                        stage_1 = True
                        stage_2 = False
                        game_active = False
                    else:
                        print('Invalid input.\n')
                        play_again = None

                stage_2 = False
                stage_1 = False

            elif guess < target_number:
                print('Nope, too low.')
            elif guess > target_number:
                print('Nope, too high.')
            else:
                pass

    



