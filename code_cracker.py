import random

def get_guess():
	return list(input('What is your 3 digit number guess? : '))

def generate_code():
	digits = [str(num) for num in range(10)]
	random.shuffle(digits)
	return digits[:3]

def generate_clues(code,user_guess):
	if user_guess == code:
		return "CODE CRACKED!"

	clues = []

	for index,num in enumerate(user_guess):
		if num == code[index]:
			clues.append("Digit Matched")
		elif num in code:
			clues.append("Close")

	if clues == []:
		return ["Nope!"]
	else:
		return clues


print("Welcome to Code Cracker!")

code = generate_code()
print(code)
clueReport = []

while clueReport !="CODE CRACKED!":
	guess = get_guess()

	clueReport = generate_clues(code,guess)

	print("Result of your Guess : ")

	for clue in clueReport:
		print(clue)
