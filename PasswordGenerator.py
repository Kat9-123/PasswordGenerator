from secrets import choice

def BoolOption(question):
	answer = input(question)
	if answer.lower() == "y":
		return True
	return False



passwordLength = input("Password length (default 50): ")
if passwordLength == "":
	passwordLength = "50"
try:
	passwordLength = int(pass_len)
except:
	passwordLength = 50

passwordLower = BoolOption("Lowercase characters (y/n): ")
passwordUpper = BoolOption("Uppercase characters (y/n): ")
passwordNumber = BoolOption("Numbers (y/n): ")
passwordSymbol = BoolOption("Symbols (y/n): ")
passwordSpecial = BoolOption("Special characters (y/n): ")

characterSet = ""

if passwordLower:
	characterSet += "abcdefghijklmnopqrstuvwxyz"
if passwordUpper:
	characterSet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if passwordNumber:
	characterSet += "0123456789"
if passwordSpecial:
	characterSet += "}{[]()/\\'`~,;:.\"<>_|"
if passwordSymbol:
	characterSet += "@#$%+-=?!*"

generatedPassword = ""
if characterSet == "":
	print("Character set is empty")
	input()
	exit()
for i in range(passwordLength):
	generatedPassword += choice(characterSet)
print()
print(generatedPassword)
print()
input()
