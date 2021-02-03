from pyfiglet import Figlet

#Gets a list of fonts
figlet = Figlet()
Fonts = Figlet.getFonts(figlet)

#makes the list of fonts and the question to select one as a single string
fontQuestion = "Select a font: \n "
for i in range(len(Fonts)):
    fontQuestion += str(i) + "." + Fonts[i] + " \n "
fontQuestion += ">>>"

#Gets the font based on user input
selectedFont = Fonts[int(input(fontQuestion))]

#Creates a new Figlet that has the font requested
output = Figlet(font=selectedFont)

#Collects text the user wants submitted
Text = input("What would you like printed: \n >>>")

#Output
print(Figlet.renderText(output, Text))

