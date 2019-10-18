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
