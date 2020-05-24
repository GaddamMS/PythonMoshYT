name = input('Hello user! Please enter your name : ')

if len(name) < 3:
    print(''' Such a short name! 
          We do not accept names less than 3 letters.
          You can try entering a longer name''')
elif len(name) > 50:
    print('''Whoa! such a loooooong name!! 
              Use some initials if possible.
              We can't fit such a long name in our system''')
else:
    print('Perfect name my friend!')