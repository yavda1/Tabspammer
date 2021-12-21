import random
import webbrowser

Run = 0
W1 = "https://www.youtube.com/channel/UCnV9orb2fg2TXYcHJsNVDQQ"
W2 = "https://www.python.org"
W3 = "https://www.oracle.com/java/technologies/downloads/"
W4 = "https://www.javascript.com/"
while Run < 20:
	Number = random.randint(1, 4)
	if Number == 1:
		Run += 1
		webbrowser.open(W1)
	elif Number == 2:
		Run += 1
		webbrowser.open(W2)
	elif Number == 3:
		Run += 1
		webbrowser.open(W3)
	elif Number == 4:
		webbrowser.open(W4)
		Run += 1