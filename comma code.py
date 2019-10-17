spam = ['cats', 'dogs', 'fish', 'pigs']

def list(spam):
    spam[-1] = 'and ' + spam[-1]
    mods = ''
    for i in spam:
        mods += i + ',' + ' '
    print("'" + mods[:-2] + "'.")

list(spam)
