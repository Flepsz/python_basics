import time

color = {
    'red': '\33[31m',

    'redz': '\33[7;91m',
    'yellowz': '\33[7;93m',
    'bluez': '\33[7;36m',
    'greenz': '\33[7;92m',
    'cyanz': '\33[7;96m',

    'r': '\33[m'
}


def get_level():
    import inquirer
    questions = [
        inquirer.List('modes',
                      message="Choose the difficulty level",
                      choices=['Nutella', 'Café com leite', 'Raiz'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['modes']


def play_game(word, time_set, num_lives, hint):
    start_time = time.time()
    current_word = list("_" * len(word))
    guessed_letters = set()

    while "_" in current_word and time.time() - start_time < time_set and num_lives > 0:
        print(" ".join(current_word))
        print("{}Lives{}: {}{}{}".format(color['redz'], color['r'], color['red'], num_lives, color['r']))
        user_input = input("Guess a letter: ").lower()
        while not user_input.isalpha() or len(user_input) != 1:
            user_input = input("Invalid input. Guess a letter: ").lower()

        if num_lives == 3:
            print("Hint: ", hint)

        if user_input in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(user_input)
        if user_input in word:
            print("{}Correct!{}\n".format(color['greenz'], color['r']))
            for i in range(len(word)):
                if word[i] == user_input:
                    current_word[i] = user_input
        else:
            print("{}Incorrect!{}\n".format(color['redz'], color['r']))
            num_lives -= 1

        print("<---------------------------------------->")
        print()

    if "_" not in current_word:
        print("Congratulations, you guessed the word!")
    else:
        print("Game over! The word was:", word)

    print("Time:", int(time.time() - start_time), "seconds")
