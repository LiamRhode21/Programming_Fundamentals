import random

random_int = random.randint(0,2)
player_input = int(input("Scissor (0), Rock (1), Paper (2): "))
result = "You lose"

match random_int:
    case 0:
        computer = "scissor"
    case 1:
        computer = "rock"
    case 2:
        computer = "paper"

match player_input:
    case 0:
        player_string = "scissor"
    case 1:
        player_string = "rock"
    case 2:
        player_string = "paper"

if computer == player_string:
    result = "It was a draw"
elif computer == ("rock" and player_string == "paper") or ("scissor" and player_string == "rock") or ("paper" and player_string == "scissor"):
    result = "You win"

print(f"The computer chose: {computer} \nYou chose: {player_string} \n{result}!")