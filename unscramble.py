# unscramble.py - scamble words and check against the dictionary
# Alex Mak

from itertools import permutations
import enchant
import sys

def usage():
	print('Usage: python unscramble.py word')

def words(letters):
	yield from map(''.join, permutations(letters, len(letters)))

def main():
	max_try = 500000
	d = enchant.Dict("en_US")
	count = 0
	match_count = 0

	if len(sys.argv) != 2:
		usage()
		return

	letters = sys.argv[1]
	
	for word in words(letters):
		count = count + 1
		if d.check(word) == True:
			match_count = match_count + 1
			print(word)
			if match_count > 2:
				break

		if count >= max_try and match_count == 0:
			print(f' after {max_try} tries, nope, sorry')
			break


	print(f'After {count} permutations, found {match_count} match', end = "")
	if match_count != 1:
		print('es.')
	else:
		print('.')

if __name__ =="__main__":
	main()