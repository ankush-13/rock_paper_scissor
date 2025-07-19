import random 

def play_rock_paper_scissors():
  choices = ('r','p','s')
  user_choice = input("Rock,paper,scissors?(r/p/s): ").lower()
  if user_choice not in choices:
    print("Invalid choice!")

  computer_choice = random.choice(choices)
  print(f'you chose: {user_choice}')
  print(f'Computer chose: {computer_choice}')

  if user_choice == computer_choice:
    print("Its a tie!")

  elif(user_choice == 'r' and computer_choice == 's') or\
    (user_choice == 's' and computer_choice == 'p') or\
    (user_choice == 'p' and computer_choice == 'r'):
    print("You won!")
  else:
    print("You lose!")

  play_again = input("Play again?(y/n): ").lower()
  if play_again == 'y':
    play_rock_paper_scissors()
  else:
    print("Thanks for playing!")

play_rock_paper_scissors()

