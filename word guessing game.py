from random import choice

print("#" * 80)
print("#" * 29 + "  WORD GUESSING GAME  " + "#" * 29)
print("#" * 80)

while True:
    # Generate random words for both easy and hard levels
    word1 = choice(["turkey", "america", "italy", "spain", "portugal", "poland", "azerbaijan", "england", "russia", "syria", "denmark", "austria", "hungary", "bulgaria", "serbia", "thailand", "china", "japan"])
    word2 = choice(["chicken", "cow", "lion", "tiger", "turtle", "fish", "cat", "dog", "monkey", "gorilla", "whale", "hedgehog", "squirrel"])
    word3 = choice(["faucet", "hammer", "lighter", "hose", "bulb", "scarf", "antenna", "lampshade", "pillow", "bed", "sofa", "couch"])

    word1_hard = choice(["Abkhazia", "Andorra", "Angola", "Burundi", "Eritrea", "Gabon", "Kiribati", "Comoros", "Mauritius", "Rwanda", "Sealand", "Zimbabwe"])
    word2_hard = choice(["octopus", "hyena", "tarantula", "frog", "tertiary", "geoduck", "ukari", "axolotl", "mantis", "shrimp", "jellyfish", "squid"])
    word3_hard = choice(["pliers", "wrench", "frying pan", "strapless", "clamp","farbela", "saxophone", "rhombus"])

    # Convert words to uppercase
    word1 = word1.upper()
    word2 = word2.upper()
    word3 = word3.upper()
    word1_hard = word1_hard.upper()
    word2_hard = word2_hard.upper()
    word3_hard = word3_hard.upper()

    # Calculate word lengths
    len_word1 = len(word1)
    len_word2 = len(word2)
    len_word3 = len(word3)

    len_word1_hard = len(word1_hard)
    len_word2_hard = len(word2_hard)
    len_word3_hard = len(word3_hard)

    # Set the number of attempts
    attempts = 7
    guesses = []
    mistakes = []

    # Ask the player to choose the game difficulty
    choice_level = int(input("""
            Choose the Game Difficulty
            1. Easy Level
            2. Hard Level
            Enter the Level You Want to Play: """))

    if choice_level == 1:
        category = int(input("""
            1. Category: Countries
            2. Category: Animals
            3. Category: Objects
            Please Choose the Category You Want to Play:  """))

        if category == 1:
            print("You Chose the Countries Category")
            print(f"\n Your Word has {len_word1} Letters ...")

            while attempts > 0:
                display_word = " "
                for letter in word1:
                    if letter in guesses:
                        display_word = display_word + letter
                    else:
                        display_word = display_word + "-"
                    if display_word == word1:
                        print("You Guessed the Word Correctly, Congratulations ...")
                        break
                print("Guess the Word ", display_word)
                print(attempts, " Attempts Left")

                guess = input("Enter a Letter:\n >>>>>")
                guess = guess.upper()

                if guess == word1:
                    print("You Guessed Correctly.")
                    display_word = word1
                    break
                if guess in guesses or guess in mistakes:
                    print(f"{guess} Was Already Guessed, Please Try Another Letter")
                elif guess in word1:
                    count = word1.count(guess)
                    print(f"Correct! The Letter {guess} Appears {count} Times in the Word.")
                    guesses.append(guess)
                else:
                    print("Wrong Letter")
                    mistakes.append(guess)
                    attempts = attempts - 1
                    print(attempts, " Attempts Left")
                if attempts == 0:
                    print("You Have No More Attempts Left")
                    print(f"Your Word: {word1}")
        elif category == 2:
            print("You Chose the Animals Category")
            print(f"\n Your Word has {len_word2} Letters ...")

            while attempts > 0:
                display_word = " "
                for letter in word2:
                    if letter in guesses:
                        display_word = display_word + letter
                    else:
                        display_word = display_word + "-"
                    if display_word == word2:
                        print("You Guessed the Word Correctly, Congratulations ...")
                        break
                print("Guess the Word ", display_word)
                print(attempts, " Attempts Left")

                guess = input("Enter a Letter:\n >>>>>")
                guess = guess.upper()

                if guess == word2:
                    print("You Guessed Correctly.")
                    display_word = word2
                    break
                if guess in guesses or guess in mistakes:
                    print(f"{guess} Was Already Guessed, Please Try Another Letter")
                elif guess in word2:
                    count = word2.count(guess)
                    print(f"Correct! The Letter {guess} Appears {count} Times in the Word.")
                    guesses.append(guess)
                else:
                    print("Wrong Letter")
                    mistakes.append(guess)
                    attempts = attempts - 1
                    print(attempts, " Attempts Left")
                if attempts == 0:
                    print("You Have No More Attempts Left")
                    print(f"Your Word: {word2}")
        elif category == 3:
            print("You Chose the Objects Category")
            print(f"\n Your Word has {len_word3} Letters ...")

            while attempts > 0:
                display_word = " "
                for letter in word3:
                    if letter in guesses:
                        display_word = display_word + letter
                    else:
                        display_word = display_word + "-"
                    if display_word == word3:
                        print("You Guessed the Word Correctly, Congratulations ...")
                        break
                print("Guess the Word ", display_word)
                print(attempts, " Attempts Left")

                guess = input("Enter a Letter:\n >>>>>")
                guess = guess.upper()

                if guess == word3:
                    print("You Guessed Correctly.")
                    display_word = word3
                    break
                if guess in guesses or guess in mistakes:
                    print(f"{guess} Was Already Guessed, Please Try Another Letter")
                elif guess in word3:
                    count = word3.count(guess)
                    print(f"Correct! The Letter {guess} Appears {count} Times in the Word.")
                    guesses.append(guess)
                else:
                    print("Wrong Letter")
                    mistakes.append(guess)
                    attempts = attempts - 1
                    print(attempts, " Attempts Left")
                if attempts == 0:
                    print("You Have No More Attempts Left")
                    print(f"Your Word: {word3}")

    if choice_level == 2:
        category = int(input("""
                    1. Category: Countries
                    2. Category: Animals
                    3. Category: Objects
                    Please Choose the Category You Want to Play:  """))

        if category == 1:
            print("You Chose the Countries Category")
            print(f"\n Your Word has {len_word1_hard} Letters ...")

            while attempts > 0:
                display_word = " "
                for letter in word1_hard:
                    if letter in guesses:
                        display_word = display_word + letter
                    else:
                        display_word = display_word + "-"
                    if display_word == word1_hard:
                        print("You Guessed the Word Correctly, Congratulations ...")
                        break
                print("Guess the Word ", display_word)
                print(attempts, " Attempts Left")

                guess = input("Enter a Letter:\n >>>>>")
                guess = guess.upper()

                if guess == word1_hard:
                    print("You Guessed Correctly.")
                    display_word = word1_hard
                    break
                if guess in guesses or guess in mistakes:
                    print(f"{guess} Was Already Guessed, Please Try Another Letter")
                elif guess in word1_hard:
                    count = word1_hard.count(guess)
                    print(f"Correct! The Letter {guess} Appears {count} Times in the Word.")
                    guesses.append(guess)
                else:
                    print("Wrong Letter")
                    mistakes.append(guess)
                    attempts = attempts - 1
                    print(attempts, " Attempts Left")
                if attempts == 0:
                    print("You Have No More Attempts Left")
                    print(f"Your Word: {word1_hard}")

        if category == 2:
            print("You Chose the Animals Category")
            print(f"\n Your Word has {len_word2_hard} Letters ...")

            while attempts > 0:
                display_word = " "
                for letter in word2_hard:
                    if letter in guesses:
                        display_word = display_word + letter
                    else:
                        display_word = display_word + "-"
                    if display_word == word2_hard:
                        print("You Guessed the Word Correctly, Congratulations ...")
                        break
                print("Guess the Word ", display_word)
                print(attempts, " Attempts Left")

                guess = input("Enter a Letter:\n >>>>>")
                guess = guess.upper()

                if guess == word2_hard:
                    print("You Guessed Correctly.")
                    display_word = word2_hard
                    break
                if guess in guesses or guess in mistakes:
                    print(f"{guess} Was Already Guessed, Please Try Another Letter")
                elif guess in word2_hard:
                    count = word2_hard.count(guess)
                    print(f"Correct! The Letter {guess} Appears {count} Times in the Word.")
                    guesses.append(guess)
                else:
                    print("Wrong Letter")
                    mistakes.append(guess)
                    attempts = attempts - 1
                    print(attempts, " Attempts Left")
                if attempts == 0:
                    print("You Have No More Attempts Left")
                    print(f"Your Word: {word2_hard}")

        if category == 3:
            print("You Chose the Objects Category")
            print(f"\n Your Word has {len_word3_hard} Letters ...")

            while attempts > 0:
                display_word = " "
                for letter in word3_hard:
                    if letter in guesses:
                        display_word = display_word + letter
                    else:
                        display_word = display_word + "-"
                    if display_word == word3_hard:
                        print("You Guessed the Word Correctly, Congratulations ...")
                        break
                print("Guess the Word ", display_word)
                print(attempts, " Attempts Left")

                guess = input("Enter a Letter:\n >>>>>")
                guess = guess.upper()

                if guess == word3_hard:
                    print("You Guessed Correctly.")
                    display_word = word3_hard
                    break
                if guess in guesses or guess in mistakes:
                    print(f"{guess} Was Already Guessed, Please Try Another Letter")
                elif guess in word3_hard:
                    count = word3_hard.count(guess)
                    print(f"Correct! The Letter {guess} Appears {count} Times in the Word.")
                    guesses.append(guess)
                else:
                    print("Wrong Letter")
                    mistakes.append(guess)
                    attempts = attempts - 1
                    print(attempts, " Attempts Left")
                if attempts == 0:
                    print("You Have No More Attempts Left")
                    print(f"Your Word: {word3_hard}")
