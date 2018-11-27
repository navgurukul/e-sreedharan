# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /    |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''', '''

	
''']

WORDS = [
	'lavadora',
	'secadora',
	'sofa',
	'gobierno',
	'diputado',
	'democracia',
	'computadora',
	'teclado'
]

def random_word():
	idx = random.randint(0, len(WORDS) - 1)
	return WORDS[idx]


def display_board(hidden_world, tries):
	print IMAGES[tries]
	print ""
	print hidden_world
	print " --- * --- * --- * --- * --- * --- "


def run():
	word = random_word()
	hidden_world = ['-'] * len(word)
	tries = 0

	while True:
		display_board(hidden_world, tries)
		current_letter = str(raw_input("Escoge una letra: "))

		letter_indexes = []
		for idx in range(len(word)):
			if word[idx] == current_letter:
				letter_indexes.append(idx)

		if len(letter_indexes) == 0:
			tries += 1

			if tries == 7:
				display_board(hidden_world, tries)
				print ""
				print "YOU LOSS! THE CORRECT WORD IT WAS " + word.upper()
				break
		else:
			for idx in letter_indexes:
				hidden_world[idx] = current_letter

			letter_indexes = []

		try:
			hidden_world.index('-')
		except ValueError:
			print ""
			print "CONGRATULATIONS! YOU WINN! THE WORD IS: " + word.upper()
			break
		


if __name__ == "__main__":
	print "B I E N V E N I D O S   A L   J U E G O   D E L   A H O R C A D O"
	run()