def display_board(board):
    print("  " + board[1] + '|' + board[2] + '|' + board[3])
    print(' -------')
    print("  " + board[4] + '|' + board[5] + '|' + board[6])
    print(' -------')
    print("  " + board[7] + '|' + board[8] + '|' + board[9])
    print()


def select_player1_marker():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Choose Player 1 (X or O) ").upper()

        if marker not in ['X', 'O']:
            print("Invalid Choice! Please Select Player 1 as X or O!  ")
            print()

    return marker


def player_index_choice(marker):
    pos = 0
    while pos not in range(1, 10):
        pos = input(f"Player {marker}: Please Select Position To Place {marker} (1-9)  ")

        if not pos.isdigit():
            print(f"Player {marker}: Invalid Choice! Please Select Valid Position (1-9)  ")
            print()
        elif int(pos) not in range(1, 10):
            print(f"Player {marker}: Invalid Choice! Please Select Valid Position (1-9)  ")
            print()
        else:
            pos = int(pos)

    return pos


def check_position_filled(board, marker, pos):
    is_pos_filled = True

    if board[pos] != ' ':
        print(f"Player {marker}: Already Filled! Please Select Different Position.")
        display_board(board)
    else:
        is_pos_filled = False

    return is_pos_filled


def update_board_list(board, marker, pos):
    board[pos] = marker
    print(f"Player {marker}: Marker Updated In The Board  ")
    display_board(board)
    return board


def check_if_player_won(board):
    winner = ''
    board_combinations = {
        'C1': [1, 2, 3],
        'C2': [4, 5, 6],
        'C3': [7, 8, 9],
        'C4': [1, 4, 7],
        'C5': [2, 5, 8],
        'C6': [3, 6, 9],
        'C7': [7, 5, 3],
        'C8': [1, 5, 9],
    }
    for combination in board_combinations.values():
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == 'X':
            winner = 'X'
            break
        elif board[combination[0]] == board[combination[1]] == board[combination[2]] == 'O':
            winner = 'O'
            break
        else:
            pass

    return winner


def reset_game(board):
    print("Restarting Game!")
    for pos in range(1, 10):
        board[pos] = ' '
    display_board(board)

    return board


def continue_playing_game():
    continue_to_play = False

    while not continue_to_play:
        continue_to_play = input("Continue Playing The Game? (Y/N)  ")

        if continue_to_play not in ['Y', 'N']:
            print("Please Select 'Y' To Continue Playing Or 'N' To Quit. (Y/N)")
            continue_to_play = True
        elif continue_to_play == 'Y':
            continue_to_play = True
        else:
            continue_to_play = False

    return continue_to_play


def check_all_positions_filled(board):
    all_pos_filled = True
    for pos in range(1, 10):
        if board[pos] == ' ':
            all_pos_filled = False

    return all_pos_filled


board_list = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player_won = False
position = 0
continue_playing = True
ready_to_play = ''
is_position_filled = True
all_positions_filled = False

print("Welcome To The TicTacToe!")

display_board(board_list)
print()

player_marker = select_player1_marker()

while continue_playing:

    ready_to_play = 'N'

    while not ready_to_play in ['Y']:
        ready_to_play = input(f"Player {player_marker}: Are You Ready To Play the Game? (Y/Q)  ")
        print()

        if ready_to_play not in ['Y', 'Q']:
            print(f"Player {player_marker}: Please Select 'Y' To Play Or 'Q' To Quit!)")
            print()

        if ready_to_play == 'Q':
            print()
            exit(0)

        while is_position_filled:
            position = player_index_choice(player_marker)
            is_position_filled = check_position_filled(board_list, player_marker, position)

        if not is_position_filled:
            board_list = update_board_list(board_list, player_marker, position)
            player_won = check_if_player_won(board_list)
            position = 0
            is_position_filled = True
            if player_marker == 'X':
                player_marker = 'O'
            else:
                player_marker = 'X'

        all_positions_filled = check_all_positions_filled(board_list)

        if all_positions_filled or player_won in ['X', 'O']:
            if all_positions_filled:
                print("It's a Tie!!!")
                print()
            else:
                print(f"Player {player_won} Won!!!")
                print()
            continue_playing = continue_playing_game()
            if continue_playing:
                reset_game(board_list)
                player_marker = select_player1_marker()
        else:
            pass
