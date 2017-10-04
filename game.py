import getpass,os,random

#clears screen before executing game
os.system('clr')
os.system('clear')

#game commmences
print("*"*90)
print ("Rock Paper Scissors Game")
print ("="*90)

def gameLogic(userA,userB,inputs):
	if userA in inputs and userB in inputs:#checks if inputs are valid
		#game logic begins
		print("Results\n" + "="*90 + "\n{} Entered {}".format(pNameA,userA) + "\n{} Entered {}\n".format(pNameB,userB))
		if userA == "R":
			print("{} wins".format(pNameA) if userB=='S' else "{} Wins".format(pNameB))
		if userA == "P":
			print("{} Wins".format(pNameA) if userB=='R' else "{} Wins".format(pNameB))
		if userA == "S":
			print("{} Wins".format(pNameA) if userB=='P' else "{} Wins".format(pNameB))
	else:
		print ("Invalid inputs")
	return
def playSingle(pNameA,pNameB):
	userA = getpass.getpass('{} input: '.format(pNameA))
	num =	random.randint(1,9)
	if num <=3:
		userB = "R"
	elif num <=6:
		userB = "P"
	else:
		userB = "S"
	os.system('clr')
	os.system('clear')
	#convert lower case to upper if entered
	userA = userA.upper()
	userB = userB.upper()
	#list for checking invalid inputs
	inputs = ["R","P","S"]
	if userA==userB:#checks if game draw
		print("Match Draw")
	else:#if not same inputs, game commences
		gameLogic(userA,userB,inputs)
def playMulti(pNameA,pNameB):
	#takes input in hidden format
	userA = getpass.getpass('{} input: '.format(pNameA))
	userB = getpass.getpass('{} input: '.format(pNameB))
	os.system('clr')
	os.system('clear')
	#convert lower case to upper if entered
	userA = userA.upper()
	userB = userB.upper()
	#list for checking invalid inputs
	inputs = ["R","P","S"]
	if userA==userB:#checks if game draw
		print("Match Draw")
	else:#if not same inputs, game commences
		gameLogic(userA,userB,inputs)

playAgain = "Y"
yes = ["Y","y"]
comp = ["C","c"]
print("To play against computer, type: c and enter")
player2 = input()
if player2 in comp:
	print ("Enter player name followed by input as" + "\n R for rock,\n P for paper,\n S for scissor")
	pNameA = input("Enter Player Name: ")
	pNameB = "Computer"
	while(playAgain in yes):
		playSingle(pNameA,pNameB)
else:
	print ("Enter player names followed by inputs as" + "\n R for rock,\n P for paper,\n S for scissor")
	pNameA = input("Enter Player 1 Name: ")
	pNameB = input("Enter Player 2 Name: ")
	while(playAgain in yes):
		playMulti(pNameA,pNameB)
		playAgain = input("="*90+"\nWould you like to play again?\n Enter Y or N\n")
		os.system('clr')
		os.system('clear')
