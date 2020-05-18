price = 1000000
good_credit = False

if good_credit:
    print('Down payment is ' + str(price * .1)  + ' and it is 10% of price as you have good credit score')
elif not good_credit:
    print('Down payment is ' + str(price * .2) + 'and it is 20% of the price')