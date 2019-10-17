# Unit 1

### Turtle Python

This was my first project and first experience with Python. I used the turtle feature within python to create a tree. It was interesting using a pen to kind of draw what you wanted and I found some new features through research that I utilized such as the stamp() code. 

    ben.forward(100)
    ben.undo()
    ben.forward(130)
    ben.right(90)
    ben.stamp()
    
It was interesting playing around with the turtle feature and seeing how I could manipulate it to make a picture. 

### Tree Project

This project was more interactive than the previous Turtle project, because it was intended to prompt a user to answer questions. 

Using extrapolation of a small area, I found a rough estimate of how many trees are in Sacramento and then prompted the user to do the same thing. At the end, I compared the user's result to mine. 


    tree = input("How many trees did you spot in 300 square feet? ") #Prompt user to write how many trees spotted over 300 square feet
    tree = int(tree) #Assign integer value to trees
    nol = 2788000000 / 90000 #Calculate the number of 300 square foot lots by dividing the total square feet of Sacramento by 300 square feet
    total = (nol * tree) #30977.77 is the number of 300 square foot lots in Sacramento, multiply by trees found to calculate total trees in Sacramento
    actual = 1301066 #Counted 42 trees in 300 square feet, multiply by number of 30 square foot lots in Sacramento to estimate total trees
    print("The total you calculated =" ,total, "compared to my calculation =", actual) #Print our calculation and user's calculation and compare it

### Rock, Paper, Scissors 

This was a fun project too as it was interactive and created a game simulating the classic rock, paper, scissiors. These types of projects are my favorite as you can use it to play a game and see how your work delivers some sort of end project that is usable. 

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
        


### How have I organized my portfolio and why is it in this order?


### Link to About Me Page
https://bkebede.github.io/
