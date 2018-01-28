#!/usr/bin/python

# Reverse mad libs game for Udacity nanodegree section 2.  Functions like a fill in the blank quiz with mulitple stages and levels of difficulty.
# 
# Difficulty:
#
# Beginner - fill in the blank with helpful hints
# Intermediate - fill in the blank with hints disabled
# Expert - real life code examples to illustrate the fill in the blank concepts
# 
#

# Import sys for sys.exit() and random for random.shuffle()

import sys
import random

# Define our stages as a list of lists.  We'll iterate through each stage later in playStage()

stages = [
		
		(
			"Computers are __1__ machines that can be reprogrammed to do many different things. \n"
			"In this example, we'll use a programming language called Python to tell our computer what we want it to do. \n"
			"Python is an __2__, which means that the code we write is fed into the Python program to be translated into \n"
			"machine code before being run.  This design speeds up the code writing process by making code \n"
			"closer to human language.  That said, human languages are highly __3__, while machine language are highly __4__. \n" 
			"This means that we have to think about how we write programs differently than how we talk to people. \n"
			"These differences can lead to many __5__, which we have to carefully squash one by one :). \n"
			"\n"
			"\n"
		),

		(
			"In programming, we can assign common values to a __1__ to make code easier to understand. \n"
			"This also allows us to easily re-use common values in our programs to save time and prevent mistakes. \n"
			"When creating these values, its important for us to differentiate between __2__ and __3__. \n" 
			"The former is symbolized by = in Python and creates a __1__ with the desired value.  The latter is \n"
			"symbolized by == in Python and is actually an operation to test the value for __3__. Plain, text values \n"
			"assigned to __1__s are called __4__s.  When we combine two __4__s together into a single value, its called \n"
			"__5__.  In Python this is done with the + operator. \n"
			"\n"
			"We can also perform other operations on __4__s in Python.  See if you can identify the methods described below: \n"
			"\n"
			"__6__ prints the position of the beginning of the __4__ if found, -1 if not. \n"
			"__7__ looks for a specific sub-__4__ in a __4__ and substitutes a user-defined __4__ instead. \n"
			"\n"
			"\n"
		),


		(
			"To make our coding easier and more predictable, we can split our instructions into smaller, repeatable blocks called __1__s or __2__s. \n"
			"These blocks can be called in our code to perform operations and __3__ the desired values using a __3__ statement.  \n"
			"Remember - __1__s without a __3__ statement __3__ nothing. \n"
			"\n"
			"consider the following code.  What is missing in order to make it an effective __1__? \n"
			"\n"
			"def sum(a,b): \n"
			"	a = a + b\n"
			"	__4__ \n"
			"\n"
			"\n"
		),

		(
			"Most programming languages including Python include logic to assist with programming. In section 2.4 \n"
			"we covered two major types of logic - __1__ statements and __2__ loops. \n"
			"\n"
			"In programming, an __1__ statement is called a __3__, and allows us to set certain blocks of code to only execute \n"
			"if certain conditions are true (or false). At a high level this is called code __4__. \n"
			"In Python, the __1__ statement contains three __3__ statements - __5__, __6__, and __7__.  These can be combined to create \n"
			"complex __3__ statements that allow for many branches. \n"
			"\n"
			"__2__ loops function a little differently. They allow us to iterate over a block of code as long as (or until) \n"
			"certain conditions are met. Its important when using __2__ loops to remember to \n"
			"correctly set the break condition, else you may end up with an __8__ loop (which is a very serious bug). \n"
			"\n"
			"\n"
		),
	
		(
			"Python also supports more complex data structures than simply variables and strings. \n"
			"One such structure is a collection of values that can be accessed via an index. \n"
			" In many languages this is called an array, however in Python is it called a __1__. \n"
			"Individual values in an __1__ are called __2__s. __1__s support very advanced forms of data manipulation, \n"
			"and can be nested (this is called a __1__ in a __1__, or a multi-dimensional __1__). \n"
			"\n"  
			"See if you can identify the following operations that can be performed on __1__s: \n"
			"\n"
			"Allows us to change the value at a specific index via re-assignment: __3__- \n"
			"Allows us to have two names that point to the same data structure in memory: __4__ \n"
			"Now try to name the built-in functions that do the following: \n"
			"\n"
			"Adds an __2__ to the end of a __1__: __5__ \n"
			"Allows us to get the length of a __1__: __6__ \n"
			"\n"
			 "\n"
		),

]


# These problems will be added to each stage if the user chooses Advanced difficulty

advanced_problems = [
		
		(
			"Answer the questions below with the correct code: \n"
			"\n"
			"Assume you want to write a python program udacity_exam.  The name of the program (including extensions) should be __6__. \n"
			"\n"
			"Assume that the path to your python interpreter is /usr/bin/python.  The first line of your script should include __7__ \n"
			"\n"
			"Write a line of python code to print hello world (use double quotes).  this should be one line. \n"
			"__8__ \n"
			"\n"
			"\n"
		),

		(
			"Answer the questions below with the correct code: \n"
			"\n"
			"Assign the string \"Hello World!\" to a variable named \"hello\" using one line of python code: \n"
			"__8__ \n"
			"\n"
			"Print the sub-string \"Hello\" from the variable defined above using one line of python code: \n"
			"__9__ \n"
			"\n"
			"Print the string \"Hello Udacity\" using the sub-string from the previous question in one line of python code: \n"
			"__10__ \n"
			"\n"
			"\n"
		),

		(
			"Answer the questions below with the correct code: \n"
			"\n"
			"Write the first line of a procedure named \"test_function\" that accepts two arguments named \"easy\" and \"hard\": \n"
			"__5__"
			"Complete the following procedure such that it returns 7: \n"
			"def addition(a, b): \n"
			"	__6__ \n"
			"	return a \n"
			"\n"
			"Complete the following procedure such that it returns the values of a and b: \n"		
			"def division(a, b): \n"
			"	a = a / b \n"
			"	__7__ \n"
			"\n"
		),

		(
			"Answer the questions below with the correct code: \n"
			"\n"
			"Write the first line of an if statement that tests the variable \"test\" for equality to the string \"arduous\": \n"
			"__9__ \n"
			"\n"
			"Complete the while loop below to prevent an infinite loop: \n"
			"index = 0 \n"
			"while index < 10: \n"
			"print index \n"
			"__10__ \n"
			"\n"
			"Complete the while loop below such that it continues to the next iteration if the value of \"index\" is greater than 5: \n"
			"index = 0 \n"
			"while index < 10: \n"
			"	if index > 5: \n"
			"		__11__ \n"
		),

		(
			"Answer the questions below with the correct code: \n"
			"\n"
			"Given the following list, write one line of python code to print \"China\": \n"
			"countries = [['China', 'Beijing'], ['India', 'Dehli'], ['Romania', 'Bucharest']] \n"
			"__7__ \n"
			"\n"
			"Given the list above, add ['United States', 'Washington']: \n"
			"__8__ \n"
			"Given the list above, write the first line of a loop that will iterate through each item in the list assigning the variable \"country\" to the current index: \n"
			"__9__ \n"
			"\n"
			"\n"
		),

]

# Define the answers to each stage in a list of lists.  Important here that the answer key be in the same order as stages[].  
# This also has the byproduct of making the answer key feature in beginner mode too easy... without random.shuffle() anyway.

answer_key = [
		["general purpose", "interpreted language", "ambiguous", "precise", "bugs"],
		["variable", "assignment", "equality", "string", "concatenation", "find", "replace"],
		["function", "procedure", "return", "return a"],
		["if", "while", "conditional", "branching", "if", "elif", "else", "infinite"],
		["list", "element", "mutation", "aliasing", "append", "len"],
	] 


# Answers to the Advanced difficulty questions.  Added to answer_key if Advanced difficulty is chosen.

advanced_problems_key = [
		['udacity_exam.py', '#!/usr/bin/python', 'print "hello world"'],
		['hello = "Hello World!', 'print hello[:5]', 'print hello[:5] + "Udacity"'],
		['def test_function(easy,hard):', 'a = 7', 'return a,b'],
		['if test == "arduous"', 'index = index + 1', 'continue'],
		['print countries[1][1]', 'countries.append(["United States", "Washington" ])', 'for country in countries:'],
]
		
# Procedure to output difficulty options and return the user's selection.
# Only inputs from game_difficulty[] will be accepted, any other input
# will simply trigger another iteration of the while loop.

def chooseDifficulty():
	game_difficulty = [ "Beginner", "Intermediate", "Advanced", ]
	difficulty = ""
	print (
		"Welcome to the Udacity Intro to Programming Nano-Degree Section 2 Quiz! \n"
		"Please choose a difficulty level: \n"
		"\n"
		"1.) Beginner \n"
		"2.) Intermediate \n"
		"3.) Advanced \n"
		"\n"
		)
	while difficulty not in game_difficulty:
		difficulty = raw_input("Choose Difficulty [Beginner|Advanced|Intermediate]: ")
	return difficulty

# Procedure to transform the stages[] data based on the difficulty selected.  
# Beginner requires that the answer_key[] for each stage be moved to a second list
# and shuffled (we didn't want to make it so easy that the right answers are always in order...)
# Intermediate effectively does nothing.  No action needed.
# Advanced adds a whole new set of problems to each section based on real code examples.

def transformDifficulty(difficulty):
	if difficulty == "Beginner":
		index = 0
		while index < len(stages):
			answers = list(answer_key[index])
			random.shuffle(answers)
			key = (
				"Answer Key: \n" 
				"\n" + '\n'.join(answers) + "\n"
				)
			stages[index] = stages[index] + key 
			index = index + 1
	elif difficulty == "Intermediate":
		return None
	elif difficulty == "Advanced":
		index = 0
		while index < len(stages):
			stages[index] = stages[index] + advanced_problems[index]
			answer_key[index] = answer_key[index] + advanced_problems_key[index]
			index = index + 1

# Bread and butter procedure.  Runs through each stage asking for and verifying user's answers.
# Replaces blanks with correct answers, and restarts the iteration on wrong answers.  4 Wrong answers in a 
# stage means you lose (program bails out using sys.exit() ). 

def playStage(stage, key):
	index = 0	
	num_guesses = 4
	print stage.replace(str(index + 1), "__?__")
	while index < len(key):
		user_input = raw_input("What term should the ? (question mark) be?")
		if user_input == key[index]:
			stage = stage.replace("__" + str(index + 1) + "__", key[index])	
			index = index + 1
			print stage.replace(str(index + 1), "__?__")
		else:
			num_guesses = num_guesses - 1
			print "Incorrect! Number of guesses remaining: " + str(num_guesses)
			if num_guesses == 0:
				print "Sorry, try again next time!"
				sys.exit()
	print "Good Job! Stage Complete!"

# Equivalent of a main() function.  Runs the game, calls other functions, iterates through each of the stages in the game.

def playGame():
	difficulty = chooseDifficulty()
	transformDifficulty(difficulty)
	index = 0
	print "\n"
	print "Alright! Lets Play!"
	while index < len(stages):
		print (
			"\n"
			"Stage " + str(index + 1)  + "\n"
			"--------------------------\n"
			"\n"
			)
		playStage(stages[index], answer_key[index])
		index = index + 1

# Start the fun!

playGame()
