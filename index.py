def sum(a, b, c):
    return a + b + c


def printboard(xstate, zstate):
    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
    two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
    three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
    four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
    five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
    six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
    eight = 'X' if xstate[8] else ('O' if zstate[8] else 8)

    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")


def checkmate(xstate, zstate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print("X won the match")
            return 1
        elif sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3:
            print("O won the match")
            return 0
    return -1


xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Welcome to the Tic Tac Toe game!")
turn = 1

while True:
    printboard(xstate, zstate)
    if turn == 1:
        print("X-choice")
        value = int(input("Enter your value: "))
    else:
        print("O-choice")
        value = int(input("Enter your value: "))

    # Check if the cell is already occupied
    if xstate[value] == 1 or zstate[value] == 1:
        print("Invalid move! Cell already occupied. Try again.")
        continue  # Ask the same player to choose again

    # Update the board
    if turn == 1:
        xstate[value] = 1
    else:
        zstate[value] = 1

    # Check for a winner
    cwins = checkmate(xstate, zstate)
    if cwins != -1:
        print("Match over")
        printboard(xstate, zstate)
        break

    # Check for a draw
    if all(xstate[i] == 1 or zstate[i] == 1 for i in range(9)):
        printboard(xstate, zstate)
        print("It's a draw!")
        break

    turn = 1 - turn  # Switch turns
