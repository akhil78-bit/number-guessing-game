import random

def play_game():
    print("\n🎯 Welcome to Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 7

    while attempts > 0:
        try:
            guess = int(input(f"\nEnter your guess ({attempts} attempts left): "))

            if guess == number:
                print("🎉 Congratulations! You guessed the correct number!")
                return
            elif guess < number:
                print("📉 Too low! Try again.")
            else:
                print("📈 Too high! Try again.")

            attempts -= 1

        except ValueError:
            print("⚠️ Please enter a valid number!")

    print(f"\n😢 Game Over! The correct number was {number}.")


# Main loop
while True:
    play_game()
    
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("👋 Thanks for playing!")
        break