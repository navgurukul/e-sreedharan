import json

# camelCase for function names
# snake_case for variable names
# CAPS_CASE for CONSTANTS

LIFELINES = {
	
}

def get_data(filename):
	with open(filename) as questions:
		data = json.load(questions,)

	return data

def display_line():
	print
	print "*" * 50
	print

def display_question(question, level):
	# Print question and dekho ki wo ek dict hai
	# ab question and uske 4 options ko alag alag lines mai print karo with

	print "Aapka naya question aapki screen pe ye raha"
	display_line()
	print question['question']
	for no, option in enumerate(question['options']):
		print (str(no + 1) + ". "+ option)
	display_line()
	pass

def ask_answer(level):
	# TODO ye niche diye huye print statements ko modify kare and har baar ek diff message aaye
	print ("Ye question aapke liye bahut important hai")
	print("Is question ka answer aap options 1, 2, 3, 4 ke form mai dijeyega")
	answer = int(raw_input())
	return answer

def match_answer(user_answer, actual_answer):
	if user_answer == actual_answer:
		print "Ye jawab bilkul sahi hai"
		return True
	else:
		print "Ye jawab galat hai, aapka game yahin kahatm hota hai"
		return False

	
def lost_game(prize_earned):
	print "you have earned rupees " + str(prize_earned)
	print "thank you for playing with us"

def get_level(question_no):
	return 1

def start_game():
	prize_earned = 1

	questions = get_data('questions.json')

	for question_no, question in enumerate(questions):

		level = get_level(question_no)
		display_question(question, level)
		answer = ask_answer(level)
		solved = match_answer(answer, question['answer'])

		if solved == False:
			lost_game(prize_earned)
			break


start_game()