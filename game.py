import sys


def play():
    hits = 0
    errors = 0
    word = input(str("Type a word: ")).upper()
    print("The word have: ", len(word), " letters!")
    while True:
        letter = input("Type a letter: ").upper()
        if len(letter) > 1:
            print("Unknown letter, try again!")
        elif len(letter) == 0:
            print("Empty answer, try again!")
        else:
            if errors <= 6:
                if letter in word:
                    print('Right answer!')
                    hits += 1
                    print("The word have: ", len(word), " letters!")
                    print("Only remain", len(word) - hits, " letters!")
                    print("SCOREBOARD: HITS: ", hits,
                          " X ERRORS: ", errors, "!")
                    if hits == len(word):
                        print('Congratulations! You win the game!')
                        print('The word was ', word, '!')
                        choice = input(
                            "Do you want to try again? (y/n): ").lower().strip()
                        if choice == 'n':
                            sys.exit()
                        else:
                            print("OK!")
                else:
                    print('Incorrect answer, try again!')
                    errors += 1
                    print("SCOREBOARD: HITS: ", hits,
                          " X ERRORS: ", errors, "!")
                    print("Only remain", len(word) - hits, " letters!")
                    print("WORD: ", ["_"]*len(word))
            else:
                print('You lose!')
                choice = input(
                    "Do you want to try again? (y/n): ").lower().strip()
                if choice == 'n':
                    sys.exit()
                else:
                    print("OK!")
