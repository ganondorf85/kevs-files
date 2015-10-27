print("Welcome to guess the number")
number = 10
guess = int(raw_input("Enter a guess:"));

if guess <number:
	print "Too low"
if guess >number:
	print "Too high"
if guess ==number:
	print "Correct!!"