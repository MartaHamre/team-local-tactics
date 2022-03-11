from socket import socket, AF_INET, SOCK_STREAM
from champlistloader import load_some_champs
from core import Champion, Match, Team
from rich.prompt import Prompt

host = 'localhost'
port = 5555
address= (host, port)

def input_champion(prompt: str,
                   color: str,
                   champions: dict[Champion],
                   player1: list[str],
                   player2: list[str]) -> None:

    # Prompt the player to choose a champion and provide the reason why
    # certain champion cannot be selected
    while True:
        match Prompt.ask(f'[{color}]{prompt}'):
            case name if name not in champions:
                print(f'The champion {name} is not available. Try again.')
            case name if name in player1:
                print(f'{name} is already in your team. Try again.')
            case name if name in player2:
                print(f'{name} is in the enemy team. Try again.')
            case _:
                player1.append(name)
                break

def startServer():
  
  # Server start and awaiting connections
  sock = socket(AF_INET, SOCK_STREAM)
  
  
  sock.bind(("localhost", 5555))
  
  print("Connection pending...")

  # Connecting players (Player 1 & Player 2)

    # Player 1
  sock.listen()
  player1, address1 = sock.accept()
  print("First player connected to server.\n")

  print("Waiting on second player.\n")

    # Player 2
  sock.listen()
  player2, address2 = sock.accept()
  print("Second player connected to server.")

  main()
    


def main():
  champions = load_some_champs()

  # Champion selection needs to be added in here
  player1 = []
  player2 = []

  for _ in range(2):
    input_champion('Player 1', 'red', champions, player1, player2)
    input_champion('Player 2', 'blue', champions, player2, player1)

  
    # Match
  match = Match(
        Team([champions[name] for name in player1]),
        Team([champions[name] for name in player2])
    )
  match.play()


    # Add in the transfer of match results to DB and to client



  sock.close()

print("Inizializing server.")
startServer()
