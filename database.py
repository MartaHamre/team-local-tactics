from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEADDR
from ssl import SOL_SOCKET
from core import Champion
import json

host = 'localhost'
port = 5555
target_address= (host, port)

sock = socket(AF_INET,SOCK_STREAM)
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sock.bind(target_address)

# use json to get the match results

def _parse_champ(champ_text: str) -> Champion:
    name, rock, paper, scissors = champ_text.split(sep=',')
    return Champion(name, float(rock), float(paper), float(scissors))


def from_csv(filename: str) -> json:
    champions = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            champ = _parse_champ(line)
            champions[champ.name] = champ

    return champions

#def new_csv(filename: str, champion, win):
   # with open(filename, "it") as file:
        

# Add inn so that match information from server gets written into resutls.txt


    


## ADD
 
def show_results():
    return from_csv('results.txt')

