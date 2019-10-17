tree = input("How many trees did you spot in 300 square feet? ") #Prompt user to write how many trees spotted over 300 square feet
tree = int(tree) #Assign integer value to trees
nol = 2788000000 / 90000 #Calculate the number of 300 square foot lots by dividing the total square feet of Sacramento by 300 square feet
total = (nol * tree) #30977.77 is the number of 300 square foot lots in Sacramento, multiply by trees found to calculate total trees in Sacramento
actual = 1301066 #Counted 42 trees in 300 square feet, multiply by number of 30 square foot lots in Sacramento to estimate total trees
print("The total you calculated =" ,total, "compared to my calculation =", actual) #Print our calculation and user's calculation and compare it
