import json

# camelCase for function names
# snake_case for variable names
# CAPS_CASE for CONSTANTS

class Kbc:

	def __init__(self):
		pass

	def get_data(self, filename):
		with open(filename) as questions:
			data = json.load(questions,)

		return data

	def display_line(self, ):
		print
		print "*" * 50
		print

	def display_question(self, question):
		# Print question and dekho ki wo ek dict hai
		# ab question and uske 4 options ko alag alag lines mai print karo with

		print "Aapka naya question aapki screen pe ye raha"
		self.display_line()
		print question['question']
		for no, option in enumerate(question['options']):
			print (str(no + 1) + ". "+ option)
		self.display_line()
		pass

	def ask_answer(self):
		# TODO ye niche diye huye print statements ko modify kare and har baar ek diff message aaye
		print ("Ye question aapke liye bahut important hai")
		print("Is question ka answer aap options 1, 2, 3, 4 ke form mai dijeyega")
		answer = int(raw_input())
		return answer

	def match_answer(self, user_answer, actual_answer):
		if user_answer == actual_answer:
			print "Ye jawab bilkul sahi hai"
			return True
		else:
			print "Ye jawab galat hai, aapka game yahin kahatm hota hai"
			return False

		
	def lost_game(self, prize_earned):
		print "you have earned rupees " + str(prize_earned)
		print "thank you for playing with us"

	def get_level(self, question_no):
		# complete this function
		# TODO step 2complete this function
		return 1

	def calculate_prize(self, question_no, solved):
		# level = get_level(question_no)
		# TODO Step 1 complete this function without the use of level
		# TODO Step 2 complete this function with the use of level
		# For that first you have to calculate level function
		return 1

	def start_game(self):
		questions = self.get_data('questions.json')

		for question_no, question in enumerate(questions):
			self.display_question(question)
			answer = self.ask_answer()
			solved = self.match_answer(answer, question['answer'])
			prize = self.calculate_prize(question_no, solved)

			if solved == False:
				self.lost_game(prize_earned)
				break

if __name__ == "__main__":
    kbc = Kbc()
    kbc.start_game()