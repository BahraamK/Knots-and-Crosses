print('[1][2][3]')
print('[4][5][6]')
print('[7][8][9]')
def game():
    game_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    def display():
        # Displays Knots and Crosses gameboard
        print('[' + game_board[0] + ']' + '[' + game_board[1] + ']' + '[' + game_board[2] + ']')
        print('[' + game_board[3] + ']' + '[' + game_board[4] + ']' + '[' + game_board[5] + ']')
        print('[' + game_board[6] + ']' + '[' + game_board[7] + ']' + '[' + game_board[8] + ']')

    def check():
        # Check for a win condition for either player
        player1 = 'x'
        player2 = 'o'
        if game_board[0] == game_board[1] == game_board[2] == player1 or game_board[0] == game_board[1] == game_board[2] == player2:
            return True
        elif game_board[3] == game_board[4] == game_board[5] == player1 or game_board[3] == game_board[4] == game_board[5] == player2:
            return True
        elif game_board[3] == game_board[0] == game_board[6] == player1 or game_board[3] == game_board[0] == game_board[6] == player2:
            return True
        elif game_board[6] == game_board[7] == game_board[8] == player1 or game_board[6] == game_board[7] == game_board[8] == player2:
            return True
        elif game_board[1] == game_board[4] == game_board[7] == player1 or game_board[1] == game_board[4] == game_board[7] == player2:
            return True
        elif game_board[2] == game_board[5] == game_board[8] == player1 or game_board[2] == game_board[5] == game_board[8] == player2:
            return True
        elif game_board[2] == game_board[4] == game_board[6] == player1 or game_board[2] == game_board[4] == game_board[6] == player2:
            return True  
        elif game_board[0] == game_board[4] == game_board[8] == player1 or game_board[0] == game_board[4] == game_board[8] == player2:
            return True      
        else:
            return False

    def input_position():
        # Allows for only valid input position from the user
        x = int(input("Enter the position:\n"))
        if game_board[x - 1] != '-':
            print("Value already exists, please enter a new value:")
            return input_position()
        else:
            return x

    player1 = input("Player name 1: \n")
    player2 = input("Player name 2: \n")

    for i in range(9):
        if i % 2 == 0  :
            # Player 1's turn
            x = input_position()
            game_board[x - 1] = 'x'
            display()
            if check():
                print(player1 + ' wins!')
                break
        
        else:
            # Player 2's turn 
            x = input_position()
            game_board[x - 1] = 'o'
            display()
            if check():
                print(player2 + ' wins!')
                break
    else:

        print('Game over')
    # Give player choice of continuation
    Repeat = input('Would you like to restart?\n').lower()
    if Repeat == 'yes':
        game()
    else:
        print("Thanks for playing!")
        exit()
game()