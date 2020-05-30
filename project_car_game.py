options = ''
is_started = False
is_stopped = False
while True:
    options = input('>').lower()
    if options == 'start':
        if is_started is False:
            print('Car started ..')
            is_started = True
        elif is_started is True:
            print('Car already started')
    elif options == 'stop':
        if is_stopped is False:
            print('Car stopped ..')
            is_stopped = True
        elif is_stopped is True:
            print('Car already stopped')

    elif options == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif options == 'quit':
        break
    else:
        print("I don't understand that...")

#After the solution, reformatting the program by streamlining .lower func to input
#while statement changed