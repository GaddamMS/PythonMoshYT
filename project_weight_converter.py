# Problem : To ask the user to input weight in Kilograms or Pounds and convert it accordingly

import math

weight = int(input('Enter your weight: '))
weight_type = input(' Weight in (L)bs or (K)ilos : ')
weight_type = weight_type.upper()

if weight_type != 'L' and weight_type != 'K':
    print('Please enter L for Pounds and K for Kilos')
elif weight_type == 'L':
    weight *= .453
    weight = math.floor(weight)
    print(f"You are {weight} kilos")
elif weight_type == 'K':
    weight *= 2.204
    weight = math.floor(weight)
    print(f"You are {weight} lbs")