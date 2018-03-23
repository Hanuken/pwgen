#!/usr/bin/python3
import sys
import random

defLength = 12
num = 24
pwLengthRange = (2, 64)

alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

try:
	length = int(sys.argv[1])
except (ValueError, IndexError):
	length = defLength
	print('Warning! Password length must be int. Using default value - ' + str(defLength))
	length = defLength

if  length < pwLengthRange[0] or length > pwLengthRange[1]:
	print('Warning! Password length must be less than ' + str(pwLengthRange[0]) + ' and more than ' + 
str(pwLengthRange[1]) + '. Using default value - ' + str(defLength) + '.')
	length = defLength

for i in range(0, num):
		password = []
		for i in range(0, length):
			password.append(alphabet[random.randint(0, len(alphabet) - 1)])
		print(''.join(str(i) for i in password))
