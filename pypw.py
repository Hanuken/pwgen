#!/usr/bin/python3
import sys
import random
import argparse

config = {
	'strLen'	:	50,
	'rows'		:	8,
}

def main():
	parser = argparse.ArgumentParser(description='pypw. A simple password generator. https://github.com/hanuken/pypw')

	parser.add_argument('length', type=int, default=12, nargs='?', help='length of password')

	parser.add_argument('-l', '--letters', help='use letters', action="store_true")
	parser.add_argument('-n', '--numbers', help='use numbers', action="store_true")
	parser.add_argument('-c', '--chars', help='use chars', action="store_true")

	parser.add_argument('-d', '--dictionary', help='show dictionary, that used for password generation', action="store_true")

	parser.add_argument('-s', '--string', help='return 128 random symbols instead a group of passwords (you can choose and copy a random range from it)', action="store_true")

	args = parser.parse_args()

	random_sec = random.SystemRandom()

	unicodeDecLetters = [n for n in range(65, 91)] + [n for n in range(97, 123)]

	letters = [chr(n) for n in unicodeDecLetters]
	numbers = [num for num in range(10)]
	special_chars = [char for char in "~!@#$%^&*()_+`-={}[]:;<>./'"]

	dictionary = []
	if args.letters: dictionary = dictionary + letters
	if args.numbers: dictionary = dictionary + numbers
	if args.chars: dictionary = dictionary + special_chars
	if not len(dictionary): dictionary = letters + numbers + special_chars

	if args.dictionary: print('Dictionary: ', str(dictionary))

	if args.length <= 0: args.length = 12

	passInRow = round(config['strLen'] / args.length) + 1

	if args.string:
		print(''.join([str(random_sec.choice(dictionary)) for x in range(129)]))

	else:
		for row in range(config['rows']):
			print(' '.join([''.join([str(random_sec.choice(dictionary)) for x in range(args.length)]) for y in range(passInRow)]))

if __name__ == '__main__':
	main()
