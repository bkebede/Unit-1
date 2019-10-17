def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    return number

try:
    my_number = int(input('Please Enter A Number: '))
except ValueError:
    print('Error: Invalid value, enter an integer')
    exit()
print(my_number)

while my_number > 1:
    my_number = collatz(my_number)
    print(my_number)

