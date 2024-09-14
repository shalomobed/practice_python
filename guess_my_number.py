import random
def main():
    number = random.randint(1, 100)
    attempts = 10
    print("I have generated a random number between 1 and 100. "
          "You will have 10 attempts to guess that number.")
    for x in range(attempts):
        my_geuss = int(input(f"Guess {x + 1}: "))
        if my_geuss == number:
            print("You correctly guessed my number!")
            break
        elif my_geuss > number:
            print("Your guess is greater than my random number. Try Again.")
        else:
            print("Your guess is less than my random number. Try Again.")
    else:
        print("You have run out of attempts. The correct number was", number)


if __name__ == "__main__":
    main()
