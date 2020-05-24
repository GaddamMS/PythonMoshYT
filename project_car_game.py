options = ''

while options.lower() != 'quit':
    options = input('>')
    if options.lower() == 'start':
        print('Car started ..')
    elif options.lower() == 'stop':
        print('Car stopped ..')
    elif options.lower() == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif options.lower() == 'quit':
        break
    else:
        print("I don't understand that...")