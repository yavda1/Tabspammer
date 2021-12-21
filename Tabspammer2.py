#Imports
import random
import webbrowser

Run = 0 #Leave this
W1 = "https://docs.microsoft.com/en-us/dotnet/csharp/" #Change these to any website you want
W2 = "https://www.python.org"
W3 = "https://www.oracle.com/java/technologies/downloads/"
W4 = "https://www.javascript.com/"
while Run < 20: #Change the 20 to however many tabs you want to open
	Number = random.randint(1, 4) #Choosing a random number
	if Number == 1: #If the "Number" variable is 1 this happens
		Run += 1 #Leave this
		webbrowser.open(W1) #Opening the W1 variable
	elif Number == 2:
		Run += 1
		webbrowser.open(W2) #Opening the W2 variable
	elif Number == 3:
		Run += 1
		webbrowser.open(W3) #Opening the W3 variable
	elif Number == 4:
		webbrowser.open(W4) #Opening the W4 variable
		Run += 1
