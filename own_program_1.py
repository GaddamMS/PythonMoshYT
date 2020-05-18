'''Feature: Intimate user with precautions based on weather when going outside
 Problem Statement: We should identify the weather and tell the user of necessary precautions
 Solution:
 1. We will ask the user for temperature
 2. Based on the given temperature, we will intimate user with self - defined precautions
'''

temperature = int(input('What is the temperature (in centigrade) outside now?'))
# if type(temperature) is int or type(temperature) is float:
# else :
#     print('I am expecting the temperature and nothing else')

if temperature < 0:
    print('It is freezing outside. Prefer staying indoor unless it is an emergency.')
elif temperature in range (1,14):
    print('Use a thick, furry coat and shoes to go outside. Carry an umbrella if possible')
elif temperature in range (15,24):
    print('Use a furry coat and shoes to go outside. You should be loving the weather today.')
elif temperature in range (24,30):
    print('Damn! Your lucky day')
elif temperature in range (30,45):
    print('Cotton clothes are the best for this weather. Avoid black colour. '
          'Wear as lite as possible. Carry an umbrella')
elif temperature in range (45,60):
    print('You must stay indoors. Possibilities of heat stroke and going to an ER')
elif temperature in range (60,75):
    print('rush! Switch ON your air conditioner right away')
elif temperature > 75:
    print('You are Kentucky Fried Chicken!')
else:
    print('Nasty You! Enter the temperature correctly')