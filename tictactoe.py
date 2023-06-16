import random

A = [["-","-","-"],["-","-","-"],["-","-","-"]]
j = 0

while True:
    if j % 2 == 0:
        print("Player 1's turn")
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    else:
        print("Player 2's turn")
        row = random.randint(0, 2)
        col = random.randint(0, 2)

    if j % 2 == 0:
        A[row][col] = "X"
    else:
        A[row][col] = "O"

    # Print the current state of the game board
    print("Current state of the game board:")
    for i in range(3):
        print(A[i])
    print()

    # Check for win conditions
    if ((A[0][0] == "O" and A[0][1] == "O" and A[0][2] == "O") or
        (A[1][0] == "O" and A[1][1] == "O" and A[1][2] == "O") or
        (A[2][0] == "O" and A[2][1] == "O" and A[2][2] == "O") or
        (A[0][0] == "O" and A[1][0] == "O" and A[2][0] == "O") or
        (A[0][1] == "O" and A[1][1] == "O" and A[2][1] == "O") or
        (A[0][2] == "O" and A[1][2] == "O" and A[2][2] == "O") or
        (A[0][0] == "O" and A[1][1] == "O" and A[2][2] == "O") or
        (A[0][2] == "O" and A[1][1] == "O" and A[2][0] == "O")):
        print("Player 2 (O) wins!")
        break
    elif ((A[0][0] == "X" and A[0][1] == "X" and A[0][2] == "X") or
          (A[1][0] == "X" and A[1][1] == "X" and A[1][2] == "X") or
          (A[2][0] == "X" and A[2][1] == "X" and A[2][2] == "X") or
          (A[0][0] == "X" and A[1][0] == "X" and A[2][0] == "X") or
          (A[0][1] == "X" and A[1][1] == "X" and A[2][1] == "X") or
          (A[0][2] == "X" and A[1][2] == "X" and A[2][2] == "X") or
          (A[0][0] == "X" and A[1][1] == "X" and A[2][2] == "X") or
          (A[0][2] == "X" and A[1][1] == "X" and A[2][0] == "X")):
        print("Player 1 (X) wins!")
        break
    elif j == 8:
        print("Tie!")
        break

    j += 1