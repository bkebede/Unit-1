p1win = "Player 1 wins."
p2win = "Player 2 wins."

while 1:
    print("Let's play rock, paper, scissors.")
    p1 = input("Player 1 chooses... ")
    p2 = input("Player 2 chooses... ")

    if (p1 == p2 and (p1 == "rock" or p1 == "paper" or p1 == "scissors")):
        print("Tie.")
    elif (p1 == "rock"):
        if (p2 == "scissors"):
            print("Player 1 wins!")
        elif (p2 == "paper"):
            print("Player 2 wins!")
        else:
            print("Invalid input.")
    elif (p1 == "scissors"):
        if (p2 == "paper"):
            print("Player 1 wins!")
        elif (p2 == "rock"):
            print("Player 2 wins!")
        else:
            print("Invalid input.")
    elif (p1 == "paper"):
        if (p2 == "rock"):
            print("Player 1 wins!")
        elif (p2 == "scissors"):
            print("Player 2 wins!")
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
    
