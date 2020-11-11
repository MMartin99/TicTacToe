def menu():
    # Main menu
    import time
    print (    "                 88888888888                    88888888888                     88888888888 "   )   
    time.sleep(0.2)          
    print(           "                    888     Y8P                   888                             888     "      )
    time.sleep(0.2)         
    print(           "                    888                           888                             888     "             )  
    time.sleep(0.2)
    print(           "                    888     888  .d8888b          888   8888b.   .d8888b          888   .d88b.   .d88b. " )
    time.sleep(0.2)
    print(           "                    888     888 d88P              888      88b d88P               888  d88  88b d8P  Y8b" )
    time.sleep(0.2)
    print(           "                    888     888 888               888  .d888888 888               888  888  888 88888888 ")
    time.sleep(0.2)
    print(           "                    888     888 Y88b.             888  888  888 Y88b.             888  Y88..88P Y8b.   "  )
    time.sleep(0.2)
    print(           "                    888     888  Y8888P           888  Y888888   Y8888P            888    Y88P    Y8888 " )
    time.sleep(0.2)                                                                                   
    print(              "                                        .d8888b.                                                        "  )
    time.sleep(0.2) 
    print(             "                                        d88P  Y88b                                                     "    )
    time.sleep(0.2) 
    print(             "                                       888    888                                                      "    )
    time.sleep(0.2)
    print(            "                                       888           8888b.   88888b.d88b.   .d88b.                        "   )
    time.sleep(0.2)
    print(             "                                       888  88888        88b  888  888  88b d8P  Y8b                      "    )
    time.sleep(0.2)
    print(             "                                       888    888 .  d888888  888  888  888 88888888                     "     )
    time.sleep(0.2)
    print(             "                                        Y88b  d88P  888  888  888  888  888 Y8b.                         "     )
    time.sleep(0.2)
    print(             "                                         Y8888P88    Y888888  888  888  888  Y8888  "   )
   
    time.sleep(3)
    print('\033c')

    print ("                          888b     d888          d8b               888b     d888")                            
    print ("                          8888b   d8888          Y8P               8888b   d8888")                            
    print ("                          88888b.d88888                            88888b.d88888")                            
    print ("                          888Y88888P888  8888b.  888 88888b.       888Y88888P888  .d88b.  88888b.  888  888") 
    print ("                          888 Y888P 888      88b 888 888  88b      888 Y888P 888 d8P  Y8b 888  88b 888  888") 
    print ("                          888  Y8P  888 .d888888 888 888  888      888  Y8P  888 88888888 888  888 888  888") 
    print ("                          888   y   888 888  888 888 888  888      888   y   888 Y8b.     888  888 Y88b 888") 
    print ("                          888       888  Y888888 888 888  888      888       888   Y8888  888  888   Y88888") 
    
    
    
    time.sleep(1)
    
    print ("\t                                            _____________________________")
    print ("                                                         Select game mode")
    print ("\t                                            _____________________________")
    time.sleep(0.2)
    print ("                                                     1. Player vs Player")
    time.sleep(0.2)
    print ("                                                     2. Player vs AI")
    time.sleep(0.2)
    print ("                                                     3. Quit game")
    print ("\t                                            _____________________________")

    time.sleep(1)
    
    while True:
        choice = input("                                Wanna play with a friend or an AI? [1 or 2] Or want to quit? [3]:")
        choice = int(choice)
        while True:
            if choice == 1:
                print("\t                                                                                  ")
                print ("                                                        You choosed the P v P mode")
                play_game()
                break

            elif choice == 2:
                print("\t                                                                                  ")
                print ("                                                        You gonna play against an AI")
                break

            elif choice == 3:
                print("\t                                                                                        ")
                print ("                       ________             __                      ___                __          _           ")           
                print ("                      /_  __/ /  ___ ____  / /__  __ _____  __ __  / _/__  ____  ___  / /__ ___ __(_)__  ___  _")   
                print ("                       / / / _ \/ _ `/ _ \/  '_/ / // / _ \/ // / / _/ _ \/ __/ / _ \/ / _ `/ // / / _ \/ _ `/ ") 
                print ("                      /_/ /_//_/\_,_/_//_/_/\_\  \_, /\___/\_,_/ /_/ \___/_/   / .__/_/\_,_/\_, /_/_//_/\_, /  ") 
                print ("                                                  /_/                         /_/            /_/         /_/   ")
                print ("                                     _______       ______           ______         __                                  ")
                print ("                                    /_  __(_)___  /_  __/__ _____  /_  __/__  ___ / /       ")             
                print ("                                     / / / / __/   / / / _ `/ __/   / / / _ \/ -_)_/        ")             
                print ("                                    /_/ /_/\__/   /_/  \_,_/\__/   /_/  \___/\__(_)         ")                                 
                time.sleep(3)
                print('\033c')
                quit()

            else:
                print("\t                                                                                  ")
                print ("                                                        Invalid caracter. Try again...") 
                break




board = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", ".",]


game_still_going = True

winner = None

current_player = "X"

def display_board():
    print("––––––––––––")
    print(board[0], "|" ,board[1], "|" ,board[2], "|")
    print("––––––––––––")
    print(board[3], "|" ,board[4], "|" ,board[5], "|")
    print("––––––––––––")
    print(board[6], "|" ,board[7], "|" ,board[8], "|")
    print("––––––––––––")
    print("")
    
def play_game():
    display_board()
    
    while game_still_going:
        handle_turn(current_player)
        check_if_gameover()
        flip_player()
        

    # The game has ended
        if winner == "X" or winner == "O":
            print(winner + " has WON!")
            game_again = input("Would you like to play again? (y/n)")
            if game_again == "y":
                display_board()
                
                
            elif game_again == "n":
                print("\t                                                                                        ")
                print ("                       ________             __                      ___                __          _           ")           
                print ("                      /_  __/ /  ___ ____  / /__  __ _____  __ __  / _/__  ____  ___  / /__ ___ __(_)__  ___  _")   
                print ("                       / / / _ \/ _ `/ _ \/  '_/ / // / _ \/ // / / _/ _ \/ __/ / _ \/ / _ `/ // / / _ \/ _ `/ ") 
                print ("                      /_/ /_//_/\_,_/_//_/_/\_\  \_, /\___/\_,_/ /_/ \___/_/   / .__/_/\_,_/\_, /_/_//_/\_, /  ") 
                print ("                                                  /_/                         /_/            /_/         /_/   ")
                print ("                                     _______       ______           ______         __                                  ")
                print ("                                    /_  __(_)___  /_  __/__ _____  /_  __/__  ___ / /       ")             
                print ("                                     / / / / __/   / / / _ `/ __/   / / / _ \/ -_)_/        ")             
                print ("                                    /_/ /_/\__/   /_/  \_,_/\__/   /_/  \___/\__(_)         ")                                
                quit()
            else:
                print("Invalid caracter try again!")    
        elif winner == None:
            print("It's a TIE!")


def handle_turn(player):
    print(player +"'s turn.")
    position = input("Choose a position! 1-9 ")
    if position == "quit":
        quit()
   


    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid position. Choose again! ")
        position = int(position) - 1

        if board[position] == ".":
            valid = True
        elif board[position] == "quit":
            quit()
        else:
            print("It's a used position, choose another one!")
       
    board[position] = player
    display_board()
    

def check_if_gameover():
    check_for_winner()
    check_if_tie()



def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
        

        


def check_rows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != "."
    row2 = board[3] == board[4] == board[5] != "."
    row3 = board[6] == board[7] == board[8] != "."

    if row1 or row2 or row3:
        game_still_going = False
        

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]



def check_columns():
    global game_still_going

    column1 = board[0] == board[3] == board[6] != "."
    column2 = board[1] == board[4] == board[7] != "."
    column3 = board[2] == board[5] == board[8] != "."

    if column1 or column2 or column3:
        game_still_going = False
        
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    


def check_diagonals():
    global game_still_going

    diagonal1 = board[0] == board[4] == board[8] != "."
    diagonal2 = board[6] == board[4] == board[2] != "."
  
    if diagonal1 or diagonal2:
        game_still_going = False
        
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    


def check_if_tie():
    global game_still_going
    if "." not in board:
        game_still_going = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


menu()
