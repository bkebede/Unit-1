# Unit 1

### Turtle Python

This was my first project and first experience with Python. I used the turtle feature within python to create a tree. It was interesting using a pen to kind of draw what you wanted and I found some new features through research that I utilized such as the stamp() code. 

    ben.forward(100)
    ben.undo()
    ben.forward(130)
    ben.right(90)
    ben.stamp()
    
It was interesting playing around with the turtle features and seeing the different ways I could manipulate it to make a picture. 

### Tree Project

This project was more interactive than the previous Turtle project, because it was intended to prompt a user to answer questions. 

Using extrapolation of an area of 300 square feet, I found a rough estimate of how many trees are in Sacramento and then prompted the user to do the same thing. At the end of the program, I provide the user a comparison of their results to the one I found. 

    tree = input("How many trees did you spot in 300 square feet? ") #Prompt user to write how many trees spotted over 300 square feet
    tree = int(tree) #Assign integer value to trees
    nol = 2788000000 / 90000 #Calculate the number of 300 square foot lots by dividing the total square feet of Sacramento by 300 square feet
    total = (nol * tree) #30977.77 is the number of 300 square foot lots in Sacramento, multiply by trees found to calculate total trees in Sacramento
    actual = 1301066 #Counted 42 trees in 300 square feet, multiply by number of 30 square foot lots in Sacramento to estimate total trees
    print("The total you calculated =" ,total, "compared to my calculation =", actual) #Print our calculation and user's calculation and compare it

### Rock, Paper, Scissors 

This was a fun project too as it was interactive and created a game simulating the classic rock, paper, scissiors. These types of projects are my favorite as you can use it to play a game and see how your work delivers some sort of end project that is usable. Using if and else if statements were critical in completing this program, because there are many different paths and options that can be taken in this game. 

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
        
### Collatz

With this project, I learned 'try and except', which seems like a very useful tool for future tasks. The try block allows me to test for errors while the except block allows me to handle that error. In the code excerpt below, I prompted the user to enter a number, but in the case that the user writes something that isn't an integer, I have a message that pops up saying that the wrong type of value was entered. This allows the program to not crash and continue running until the user does enter the correct type of value. 

    try:
        my_number = int(input('Please Enter A Number: '))
    except ValueError:
        print('Error: Invalid value, enter an integer')
        exit()
    
### Comma Code

This project was an exercise with lists and functions, as the goal was to write a function that separated the values in the list with a comma, a space as well as "and" in between the values. Learning function is an important task as functions simplify coding as they're blocks of code that have a high degree of reusability and provide better modularity for your application. Lttle tools like [-1] look at 

    spam = ['cats', 'dogs', 'fish', 'pigs']

    def list(spam):
        spam[-1] = 'and ' + spam[-1]
        mods = ''
        for i in spam:
            mods += i + ',' + ' '
        print("'" + mods[:-2] + "'.")

    list(spam)

### Encryption Project 
This piece gave me some issues when trying to complete it, as this part of the project did as well. The goal was to decode ciphertext and print out all 25 rotations. Using range() allowed me to loop through every possible key. Later, we looped through every symbol in the ciphertext string in message, while symbol checks if it is an uppercase letter while find() locates where the symbol is in letters and stores it in a vairable called num. Because this was a decryption, I subtracted the key which may cause num to be 0, so wrap arounds were put in place. String formatting was used for the 2nd last line "%s" places one string inside another one. The first %s text in the string gets replaced by the first value in the parentheses after the % at the end of the string.

    message = 'dzeevjfkrlezkvuwffksrcctcls'
    letters = 'abcdefghijklmnopqrstuvwxyz'


    for key in range(len(letters)):

 
    encoded = ''

    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol) 
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(letters)

            # add number's symbol at the end of translated
            encoded = encoded + letters[num]

        else:
            # just add the symbol without encrypting/decrypting
            encoded = encoded + symbol

    # display the current key being tested, along with its decryption
    #print('Key #%s: %s' % (key, translated))
    print(key, encoded)
    
### Questions regarding the layout of my Unit 1 Page...

Why is it organized in the way it is?
I organized it in chronological order, using the projects that I found to be the most interesting to me. 

What piece are you most proud of?
The Turtle project stands out because it was my first experience with Python. I also really enjoyed creating the Rock, Paper, Scissors game, because the end product felt really rewarding. 

What's your best piece and how did you go about creating it?

My best was the Rock, Paper, Scissors piece and I had to map it out on paper first because there were so many different path routes in the game. So to ensure that all those options were noted but also in an organized manner, mapping it out on paper was key. 

Which one was the hardest?
The Encryption project was the hardest one for me as I had trouble figuring out the 

What piece would you most like to improve?


### Link to About Me Page
[https://bkebede.github.io/]
