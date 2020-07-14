from puzzle import Puzzle


class Game:
    WON = """\
 __     __                               _
 \ \   / /                              | |
  \ \_/ ___  _   _  __      _____  _ __ | |
   \   / _ \| | | | \ \ /\ / / _ \| '_ \| |
    | | (_) | |_| |  \ V  V | (_) | | | |_|
    |_|\___/ \__,_|   \_/\_/ \___/|_| |_(_)

    """

    LOST = """\
 __     __           _           _   _
 \ \   / /          | |         | | | |
  \ \_/ ___  _   _  | | ___  ___| |_| |
   \   / _ \| | | | | |/ _ \/ __| __| |
    | | (_) | |_| | | | (_) \__ | |_|_|
    |_|\___/ \__,_| |_|\___/|___/\__(_)

    """

    SEEYOULATER = """\
   _____                                 _       _
  / ____|                               | |     | |
 | (___   ___  ___   _   _  ___  _   _  | | __ _| |_ ___ _ __
  \___ \ / _ \/ _ \ | | | |/ _ \| | | | | |/ _` | __/ _ | '__|
  ____) |  __|  __/ | |_| | (_) | |_| | | | (_| | ||  __| |
 |_____/ \___|\___|  \__, |\___/ \__,_| |_|\__,_|\__\___|_|
                      __/ |
                     |___/
    """
    DIVIDER = """\
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """

    def __init__(self):
        self.puzzle = Puzzle()
        self.turns = 0
        self.won = False

    def ask_user_to_play(self):
        response = input("Do you want to play? (y/n) ").lower()
        if response == "y":
            print("Let's play!")
            # create a reset the game function
            self.turns = 0
            self.won = False
            self.puzzle.reset_puzzle()
            self.puzzle.select_puzzle()
            print()
            self.puzzle.display_puzzle()
            print()
            self.puzzle.hash_puzzle()
            self.ask_user_to_set_difficulty()
        else:
            print(f'{game.SEEYOULATER}')
        return response

    def calculate_difficulty(self, difficulty):
        num_unique_characters = len(
            set("".join(ch.lower() for ch in self.puzzle.puzzle if ch.isalpha())))

        if difficulty == 'EASY' or difficulty == 'E':
            turns = num_unique_characters * 5
        elif difficulty == 'MEDIUM' or difficulty == 'M':
            turns = num_unique_characters * 3
        else:
            turns = num_unique_characters * 1
        return turns

    def ask_user_to_set_difficulty(self):
        difficulty = input(
            "What difficulty would you like to play? (easy (E)/medium (M)/hard (H)) ").upper()
        self.turns = self.calculate_difficulty(difficulty)
        print(f'Number of turns: {self.turns}')

    def play_round(self):

        def user_entered_blanks(letter_to_replace, guess):
            if letter_to_replace != "" and guess != "":
                blanks = False
            else:
                blanks = True
            return blanks

        def display_won_or_lost():
            if self.turns >= 0 and self.won:
                print(f'{game.WON}')
            else:
                print(f'{game.LOST}')
                self.puzzle.display_puzzle()
                self.puzzle.display_hashed_puzzle()
                print()

        def display_message(already_used, blanks):
            if not already_used and not blanks:
                self.puzzle.update_guesses(letter_to_replace, guess)
                self.turns -= 1
            elif blanks:
                print()
                print(game.DIVIDER)
                print(f'        >>>> Try again. <<<<')
            elif already_used:
                print()
                print(game.DIVIDER)
                print(f'>>>> Already used that letter in the puzzle, try again. <<<<')

            if self.turns > 0:
                print(game.DIVIDER)
                print(f'Turns left: {self.turns}\n')

        while not self.won and self.turns > 0:
            self.puzzle.update_guessed_puzzle()
            self.puzzle.display_guessed_puzzle()
            self.puzzle.display_hashed_puzzle()

            letter_to_replace = input(
                "What letter would you like to replace? ").upper()
            guess = input(
                "What letter would you like to replace it with? ").upper()

            already_used = self.puzzle.guess_already_used(
                letter_to_replace, guess)
            blanks = user_entered_blanks(letter_to_replace, guess)
            display_message(already_used, blanks)
            self.won = self.puzzle.puzzle_matches_key()

        display_won_or_lost()

    def play_game(self):
        play_again = self.ask_user_to_play()
        while play_again == 'y':
            self.play_round()
            play_again = self.ask_user_to_play()


if __name__ == '__main__':
    game = Game()
    game.play_game()
