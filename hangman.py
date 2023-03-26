import random
import string
from words import words
def get_valid_word(words):
	word = random.choice(words)	#randomly choose something from the list of words in words.py file
	while '-' in word or ' ' in word:
		word = random.choice(words)
	return word

def hangman():
	word = get_valid_word(words).upper()
	word_letters = set(word)	# a set of letters in that word
	alphabet = set(string.ascii_uppercase)
	used_letters = set()
	lives = 6

	# getting user input
	while len(word_letters) > 0 and lives > 0:
		# used letters
		print('You have',lives,' left and You have used the letters: ', ' '.join(used_letters))

		# what current word is (wo_r_s )
		word_list = [letter if letter in used_letters else '-' for letter in word]
		print('current word: ', ' '.join(word_list))

		user_letter = input('Guess a letter: ').upper()
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)
			else:
				lives = lives - 1
				print('Entered letter is not in word.')
		elif user_letter in used_letters:
			print('You have used that character. Please try again.')
		else:
			print('Invalid character. Please try again.')
	if lives == 0:
		print('You died, sorry. The word was', word)
	else:
		print('You guessed the word', word)
if __name__ == '__main__':	
	hangman()