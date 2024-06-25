import random as rd
import art
import game_data as gd
from replit import clear


go = True
score = 0
#create a function for comparison
def compare(A,B):
  global score
  global go
  global choice
  global greater
  
  if A["follower_count"] > B["follower_count"] and choice == "a":
    score +=1
    clear()
  elif A["follower_count"] < B["follower_count"] and choice == "b":
    score +=1
    clear()
  elif A == B:
    score += 1
    clear()
  else:
    go = False
    clear()


#while go is true -> keep asking A or B
A = rd.choice(gd.data)
while go:
  print(art.logo) #print logo
  
#randomly pick 2 people from the list in gd and make sure it does not repeat
  B = rd.choice(gd.data)
  print(f"A: {A['name']}, a {A['description']}, from {A['country']}")
  print(art.vs)
  print(f"B: {B['name']}, a {B['description']}, from {B['country']}")
  choice = input("Who has more followers? Type A or B: ").lower()
  compare(A, B)
  if go:
    print(f"You're Right! Current Scrore: {score}")
  A = B

if not go:
  print(f"Sorry, that's wrong. Final score: {score}")
# assign the 2 people to A and B
# use compare function to compare (in compare set 'go' to false if chosen value greater A or B)