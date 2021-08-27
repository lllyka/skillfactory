def privet():
    print('''Добро пожаловать!
    Это игра Крестики-Нолики!
    Чтоб сделать ход введите
    номер клетки куда хотите поставить символ:
    ''')
board = list(range(1,10))


def new_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)


def hodi(tictac):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + tictac+"? ")
        if player_answer.isdigit():
            player_answer = int(player_answer)
        else:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = tictac
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


def checkwin(board):
    wincoord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in wincoord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
privet()


def main(board):
    counter = 0
    win = False
    while not win:
        new_board(board)
        if counter % 2 == 0:
            hodi("X")
        else:
            hodi("O")
        counter += 1
        if counter > 4:
            tmp = checkwin(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    new_board(board)


main(board)
