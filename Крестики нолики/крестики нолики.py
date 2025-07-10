board = [i for i in range(1,10)]
wins = [ [0,1,2], [3,4,5], [6,7,8],
         [0,3,6], [1,4,7], [2,5,8],
         [0,4,8], [2,4,6]
]
def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print("-" * 13)

def move_player(player):
    while True:
        try:
            move = int(input(f'Ход игрока {player} \n Введите позицию (1-9):')) - 1
            if not 0 <= move <= 8:
                print('Позиция должна быть от 1 до 9!')
            elif board[move] in ("X", "O"):
                print('Эта клетка уже занята!')
            else:
                board[move] = player
                break
        except ValueError:
            print('Введите число (1-9)')
        except IndexError:
            print('Позиция должна быть от 1 до 9!')

def check_win(player):
    return any(all(board[i] == player for i in combo) for combo in wins)

def check_draw():
    return all(isinstance(i, str) for i in board)

def restart_game():
    global board
    board = [i for i in range(1,10)]
    game()

def ask_restart():
    while True:
        answer = input('Хотите начать игру заново (да/нет)? - ').lower()
        if answer == 'да':
            restart_game()
            break
        elif answer == 'нет':
            print('Спасибо за игру!')
            break
        else:
            print('Пожалуйста, введите "да" или "нет"')

def game():
    current_player = 'X'
    draw_board(board)
    while True:
        move_player(current_player)
        draw_board(board)
        if check_win(current_player):
            print(f'Победил игрок {current_player}!!!')
            print('Умный человек в очках скачать фото')
            ask_restart()
            break
        if check_draw():
            print('Ничья ;(')
            print('Умный человек в очках скачать фото')
            ask_restart()
            break
        current_player = "O" if current_player == "X" else 'X'

game()