import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12)/2))+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

print("⚔️ BATTLE TIME ⚔️")
print()
ch1Name= input("Name your Legend: \n")
ch1Type =input("Charater Type [(Human, Elf, Wizard, Orc)]:\n") 
print()
print(ch1Name)
ch1Health = health()
ch1Strength = strength()
print("Health: ", ch1Health)
print("Strength: ", ch1Strength)
print()
print("Who are the batteling?")
print()

ch2Name= input("Name your Legend: \n")
ch2Type =input("Charater Type [(Human, Elf, Wizard, Orc)]:\n") 
print()
print(ch2Name)
ch2Health = health()
ch2Strength = strength()
print("Health: ", ch2Health)
print("Strength: ", ch2Strength)
print()

round = 1
winner = None

while True:
  time.sleep(3)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle Begins!")

  c1Dice = rollDice(6)
  c2Dice = rollDice(6)

  difference = abs(ch1Strength - ch2Strength) + 1
  if c1Dice > c2Dice:
    ch2Health -= difference
    if  round==1:
      print(ch1Name, "wins the first blow")
    else:
      print(ch1Name, "wins round", round)
  elif c2Dice > c1Dice:
    ch1Health -= difference
    if  round==1:
      print(ch2Name, "wins the first blow")
    else:
      print(ch2Name, "wins round", round)
  else:
    print("Their swords clash and they draw the round", round)

  print()
  print(ch1Name)
  print("Health: ", ch1Health)
  print()
  print(ch2Name)
  print("Health: ", ch2Health)
  print()

  if ch1Health<=0:
    print(ch1Name, "has died!")
    winner = ch2Name
    break
  elif ch2Health <=0:
    print(ch2Name, "has died!")
    winner = ch1Name
    break
  else:
    print("And the they both standing for the next round")
    round += 1


time.sleep(3)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")