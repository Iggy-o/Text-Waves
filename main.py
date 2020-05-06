#Ighoise Odigie
#April, 20 2020
#Youtube: https://www.youtube.com/channel/UCud4cJjtCjEwKpynPz-nNaQ?
#Github: https://github.com/Iggy-o
#Preview: https://repl.it/@IghoiseO/Text-Waves

'''
Warning: Large input values may cause substantial device lag
Start of with smaller values and work your way up

HAVE FUN!!!
'''

#<!--First Part: User Input-->
#This prints out the program Header
header = "--Text Wave Simulator--"
print(header)

#The following is placeholder text and their respective user input prompts
symbol_text = "\nChoose any Symbol -> "
symbol = str(input(symbol_text))
numWaves_text = "\nChoose any number of waves -> "
numWaves = int(input(numWaves_text))
heightWaves_text = "\nChoose a wave height -> "
heightWaves = int(input(heightWaves_text))



#<!--Second Part: Creating Waves-->
#Based on user input, the output variable is filled with a wave pattern
output = ''

#Loops through and executes based on the user inputted number of waves
for f in range(numWaves):

  #Creates the first half of a wave
  for g in range(1, heightWaves+1):
    output += symbol * g
    output += "\n"

  #Creates the second half of a wave
  for h in range(heightWaves, 0, -1):
    output += symbol * h
    output += "\n"



#<!--Third Part: Printing Results-->
#The output is printed out for the user to view
print(output)



#<!--Program Complete-->
