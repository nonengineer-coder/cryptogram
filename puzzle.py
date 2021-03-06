import random
from soup import Soup


class Puzzle:
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self):
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.guessed_puzzle = ""
        self.alpha_to_hash = dict()
        self.hash_to_alpha = dict()
        self.alpha_to_guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}
        self.soup = Soup()

    def reset_puzzle(self):
        """Reset the puzzles and dictionaries"""
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.guessed_puzzle = ""
        self.alpha_to_hash = dict()
        self.hash_to_alpha = dict()
        self.alpha_to_guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}

    def select_puzzle(self):
        self.puzzle = random.choice(self.soup.get_episodes())

    def hash_puzzle(self):
        """Hash the puzzle by randomly mixing up the alphabet,
        Keep track of alpha to hash and hash to alpha in dictionaries,
        Store hashed puzzle in a string for display purposes
        """
        alphabet = list.copy(Puzzle.ALPHABET)
        alphabet = random.sample(alphabet, len(alphabet))
        self.alpha_to_hash = {
            Puzzle.ALPHABET[i]: alphabet[i] for i in range(len(Puzzle.ALPHABET))}
        self.hash_to_alpha = {
            alphabet[i]: Puzzle.ALPHABET[i]
            for i in range(len(Puzzle.ALPHABET))}

        for letter in self.puzzle:
            if not letter.isalpha():
                self.hashed_puzzle += letter
            elif letter.upper() in Puzzle.ALPHABET:
                self.hashed_puzzle += self.alpha_to_hash[letter.upper()]

        self.hashed_puzzle = "  ".join(self.hashed_puzzle.split())

    def update_guesses(self, alpha, guess):
        """Update guesses dictionary"""
        self.alpha_to_guesses[alpha.upper()] = guess.upper()

    def guess_already_used(self, alpha, guess):
        if guess in self.alpha_to_guesses.values():
            return True
        else:
            return False

    def letter_in_hash(self, letter_to_replace, guess):
        if letter_to_replace in self.hashed_puzzle:
            return True
        else:
            return False 

    def update_guessed_puzzle(self):
        """Update the guessed puzzle for display purposes"""
        self.guessed_puzzle = ""
        for letter in self.hashed_puzzle:
            if not letter.isalpha():
                self.guessed_puzzle += letter
            elif letter.upper() in Puzzle.ALPHABET:
                self.guessed_puzzle += self.alpha_to_guesses[letter.upper()]
        self.guessed_puzzle = "  ".join(self.guessed_puzzle.split())

    def puzzle_matches_key(self):
        """Check if the puzzle matches key,
        Return True if it does, False otherwise
        """
        for letter in self.hashed_puzzle:
            if letter.isalpha():
                if self.alpha_to_guesses[letter] == self.hash_to_alpha[letter]:
                    continue
                else:
                    return False
        return True

    def display_guessed_puzzle(self):
        print(self.guessed_puzzle)

    def display_hashed_puzzle(self):
        print(self.hashed_puzzle)

    def display_puzzle(self):
        print("  ".join(self.puzzle.split()))
