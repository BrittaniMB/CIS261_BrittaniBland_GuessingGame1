import random

def display_title():
 print("Guess the Number!")
 print()

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I am thinking of a random number from 1 to {limit}\n.")
    count = 1
    guess = int(input("Your Guess?:  "))
    
    while(guess != number):
     if guess < number:
      print("Too Low")
      count += 1
     guess = int(input("your Guess?:  "))
    print(f"You guessed it in {count} tries.\n")
    
def main():
  display_title()
  again = "yes"
  while again.lower() == "yes":
    limit = int(input("Enter the limit:  "))
    play_game(limit)
    again = input("Would you like to play again? Enter yes or no:  ")
    print()
  print("Goodbye!")
  
if __name__ == "__main__":
   main()