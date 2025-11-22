import random;
def get_choices():
      player_choice = input("Enter a choice(rock, paper, scissor): ") ;
      options = ["rock","paper","scissor"]
      computer_choice = random.choice(options);
      choices = {"player" : player_choice , "computer" : computer_choice};
      return choices;


# print(choices);
# Dictionaries

# food = ["pizzas", "carrots","eggs"]
# dinner = random.choice(food)

def check_win(player, computer):
      print (f"You choose {player} Computer Choose {computer}");
      if player == computer:
            return "It is a tie!";

 
      elif player == "rock":
            if computer == "scissor":
                  return "Rock smashes scissor ! You Win"
            else :
                  return "paper covers the rock ! You Lose"
      elif player == "scissor":
            if computer == "rock":
                  return "Rock smashes scissor ! You lose"
            else :
                  return " scissor cuts the paper ! You win"
      elif player == "paper":
            if computer == "scissor":
                  return "scissor cuts the paper ! You lose"
            else :
                  return "paper covers the rock ! You Win"     
      return [player, computer]

choices = get_choices( )
result = check_win(choices["player"], choices["computer"]);
print(result);




 

