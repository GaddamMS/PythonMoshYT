options = ''

while True:
    options = input('>').lower()
    if options == 'start':
        print('Car started ..')
    elif options == 'stop':
        print('Car stopped ..')
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