

import random

while True:
    GameBoard = [" "] * 9
    player = "X"
    winning_positions = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    while True:
        menu = input("1.Two Players  2.Computer  3.Exit: ")
        match menu:
            case "1":
                mode = "two"
                break
            case "2":
                mode = "computer"
                break
            case "3":
                mode = "exit"
                break
            case _:
                print("Wrong choice!")
    if mode == "exit":
        print("Goodbye!")
        break
    while True:
        print("Current Game Board:")
        print(*GameBoard[0:3], sep=" | ")
        print(*GameBoard[3:6], sep=" | ")
        print(*GameBoard[6:9], sep=" | ")

        if mode == "two" or player == "X":
            print(player,"turn")
            while True:
                position = input("Enter your position from 0-8: ")
                if not position.isdigit():
                    print("Wrong number!")
                    continue
                position = int(position)
                if position > 8:
                    print("Wrong number!")
                    continue
                if GameBoard[position] == " ":
                    GameBoard[position] = player
                    break
                else:
                    print("Choose another position!")
        else:
            list_empty = []
            for i in range(9):
                if GameBoard[i] == " ":
                    list_empty.append(i)
            position = random.choice(list_empty)
            print("Computer chose:", position)
            GameBoard[position] = player
        print("Game Board:")
        print(*GameBoard[0:3], sep=" | ")
        print(*GameBoard[3:6], sep=" | ")
        print(*GameBoard[6:9], sep=" | ")
        winner = ""
        for positions in winning_positions:
            if all(GameBoard[i] == player for i in positions):
                winner = player
                break
        if winner != "":
            print("Winner is:", winner)
            break
        elif " " not in GameBoard:
            print("It is a draw! No winner.")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
