# fx to draw tic tac toe board
def board(rows):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(rows[0], rows[1], rows[2]))
    print('\t_____|_____|_____')

    
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(rows[3], rows[4], rows[5]))
    print('\t_____|_____|_____')

    
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(rows[6], rows[7], rows[8]))
    print("\t     |     |")
  
# fx to check if any player has won
def win(play_position, player_turn):
 
    # All possible winning combinations
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in solution:
        if all(y in play_position[player_turn] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 
# fx to check if the board is drawn
def draw(play_position):
    for spot in play_position:
        if spot != 'x' and spot != 'y':
            return False
    return True                

# fx for game
def game(player_turn):
    rows = [' ' for x in range(9)]

    # identifies the space already occupied by x or o
    play_position = {'X':[], 'O':[]} 
 
    # while loop to execute game
    while True:
        board(rows)

        # use try block for move input 
        try:
            print("Player ", player_turn, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Invalid input! Try Again")
            continue    

        # check valid move
        if move < 1 or move > 9:
            print("Invalid input! Try Again")
            continue

        # check for occupied space
        if rows[move-1] != ' ':
            print("Space already filled. Try again!!")
            continue

        # update board to include current move
        rows[move-1] = player_turn

        # update space according to current move
        play_position[player_turn].append(move)

        
        # call fx for checking win
        if win(play_position, player_turn):
            draw(rows)
            print("Player ", player_turn, " has won the game!!")     
            print("\n")
            return player_turn
 
        # call fx for checking draw 
        if draw(play_position):
            board(rows)
            print("It's a draw")
            print("\n")
            return 'Draw'
 
        # Switch player moves
        if player_turn == 'X':
            player_turn = 'O'
        else:
            player_turn = 'X'



if __name__ == "__main__":

    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")
     
    # Stores the player who chooses X and O
    player_turn = player1
 
    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}
 
    # Stores the letter choice
    letter = ['X', 'O']
 
    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:
 
        # Player choice Menu
        print("Turn to choose for", player_turn)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        # Try exception for CHOICE input
        try:
            choice = int(input())   
        except ValueError:
            print("Invalid Input! Try Again\n")
            continue

        # condition for player turn
        if choice == 1:
            player_choice['X'] = player_turn
            if player_turn == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = player_turn
            if player_turn == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1 

        elif choice == 3:
            print("Thanks for playing")
            break

        else:
            print("Invalid Choice! Try Again\n")

        # display winner
        winner = game(letter[choice-1])
        if winner != 'Draw' :
            win_player = player_choice[winner]