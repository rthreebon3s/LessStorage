while 1 != 2:
    ask1 = input('Insert quantity: ')
    ask2 = input('Insert size type: ')
    if ask2.lower() in ['b']:
        a = open("file.txt", "a")
        a.write("B" * int(ask1))
        a.close()
    elif ask2.lower() in ['k','kb']:
        a = open("file.txt", "a")
        a.write("K" * int(ask1) * 1024)
        a.close()
    elif ask2.lower() in ['m','mb']:
        a = open("file.txt", "a")
        a.write("M" * int(ask1) * 1024 * 1024)
        a.close()
    elif ask2.lower() in ['g','gb']:
        a = open("file.txt", "a")
        a.write("G" * int(ask1) * 1024 * 1024 * 1024)
        a.close()
    else:
        print('Invalid!')
    ask3 = input('Do you want to reset the file? (y,n) ')
    if ask3.lower == 'y':
        a = open("file.txt", "w")
        a.write("")
        a.close()
        print('Reset successful!')
    elif ask3.lower == 'n':
        print('Reset cancelled!')
    else:
        while ask3 not in ['y','n']:
            ask3 = input('The action is invalid. Proceed? (y,n) ')
            if ask3.lower == 'y':
                a = open("file.txt", "w")
                a.write("")
                a.close()
                print('Reset successful!')
            elif ask3.lower == 'n':
                print('Reset cancelled!')
    print('\n')