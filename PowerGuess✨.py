import random
marvel = {"scarlet witch" : 1,
          "thor" : 2,
          "doctor strange" : 3,
          "thanos" : 4,
          "captain marvel" : 5,
          "hulk" : 6,
          "iron man" : 7,
          "vision" : 8,
          "loki" : 9,
          "black panther" : 10,
          "shang-chi" : 11,
          "ant-man" : 12,
          "wasp" : 13,
          "spider-man" : 14,
          "star-lord" : 15,
          "gamora" : 16,
          "drax" : 17,
          "war machine" : 18,
          "rocket raccoon" : 19,
          "groot" : 20,}
pick = random.choice(list(marvel.keys()))
print("Guess the Marvel character based on power (1 = strongest, 20 = weakest)")
print("You have 10 guesses. Start guessing!")
answer = input(": ").lower()
guess = 1
while True:
    if guess > 10:
        print("Sorry!😔 your guess are finished")
        break
    elif pick == answer and guess <= 10:
        print(f"Correct!!🎉🎉 and you take {guess} guess to complete it")
        break
    elif marvel[pick] < marvel[answer]:
        print("NO!❌ that too low in power")
        guess += 1
        answer = input("Choose a Marvel characters which is high in power: ").lower()
    elif marvel[pick] > marvel[answer]:
        print("NO!❌ that too high in power")
        guess += 1
        answer = input("Choose a Marvel characters which is low in power: ").lower()
