def logic_word(time, color, num_lives, time_set, word):
    start_time = time.time()
    current_word = list("_" * len(word))
    guessed_letters = set()

    while "_" in current_word and time.time() - start_time < time_set and num_lives > 0:
        print(" ".join(current_word))
        print("{}Lives{}: {}{}{}".format(color['red_bg'], color['r'], color['red'], num_lives, color['r']))
        user_input = input("Guess a letter: ").lower()
        while not user_input.isalpha() or len(user_input) != 1:
            user_input = input("Invalid input. Guess a letter: ").lower()

        if user_input in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(user_input)
        if user_input in word:
            print("{}Correct!{}\n".format(color['green'], color['r']))
            for i in range(len(word)):
                if word[i] == user_input:
                    current_word[i] = user_input
        else:
            print("{}Incorrect!{}\n".format(color['red'], color['r']))
            num_lives -= 1

    if "_" not in current_word:
        print("Congratulations, you guessed the word!")
    else:
        print("Game over! The word was:", word)

    print("Time:", int(time.time() - start_time), "seconds")
