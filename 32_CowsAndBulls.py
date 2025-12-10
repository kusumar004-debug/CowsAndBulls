import random

def generate_secret():
    """Generate a 4-digit number with no repeating digits."""
    digits = "0123456789"
    return "".join(random.sample(digits, 4))

def get_guess():
    """Ask the user for a valid 4-digit guess."""
    while True:
        guess = input("Enter a 4-digit number with no repeating digits: ")

        if len(guess) != 4:
            print("❌ Must be 4 digits.")
        elif not guess.isdigit():
            print("❌ Only digits allowed.")
        elif len(set(guess)) != 4:
            print("❌ Digits must not repeat.")
        else:
            return guess

def count_cows_bulls(secret, guess):
    """Return number of cows and bulls."""
    bulls = 0
    cows = 0
    for i in range(4) :
        if guess[i] == secret[i] :
            bulls += 1
        elif guess[i] in secret :
            cows += 1
    return cows, bulls

def play_game():
    secret = generate_secret()
    attempts = 0

    print("\n🎮 Welcome to the Cows and Bulls Game!")
    print("I have generated a secret 4-digit number. Try to guess it!")

    while True:
        guess = get_guess()
        attempts += 1

        cows, bulls = count_cows_bulls(secret, guess)

        print(f"👉 Bulls: {bulls} | Cows: {cows}")

        if bulls == 4:
            print(f"\n🎉 Correct! You guessed the number {secret} in {attempts} attempts!")
            break

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("👋 Thanks for playing! Goodbye!")
            break

main()

