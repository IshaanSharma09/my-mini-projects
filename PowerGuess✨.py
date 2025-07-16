import random

marvel = {
    "scarlet witch": 1,
    "thor": 2,
    "doctor strange": 3,
    "thanos": 4,
    "captain marvel": 5,
    "hulk": 6,
    "iron man": 7,
    "vision": 8,
    "loki": 9,
    "black panther": 10,
    "shang-chi": 11,
    "ant-man": 12,
    "wasp": 13,
    "spider-man": 14,
    "star-lord": 15,
    "gamora": 16,
    "drax": 17,
    "war machine": 18,
    "rocket raccoon": 19,
    "groot": 20,
}

pick = random.choice(list(marvel.keys()))

print("🎮 Guess the Marvel character based on power!")
print("🧠 1 = strongest, 20 = weakest")
print("🕹️ You have 10 guesses. Start guessing!")

guess = 1
while guess <= 10:
    answer = input(f"Guess #{guess}: ").lower()

    if answer not in marvel:
        print("⚠️⚠️⚠️ Invalid character name! Please enter a valid Marvel character.")
        continue

    if answer == pick:
        print(f"🎉🎉 Correct!! It was '{pick.title()}'. You guessed it in {guess} tries!")
        break
    elif marvel[pick] < marvel[answer]:
        print("❌ Too low in power! Try someone stronger.")
    elif marvel[pick] > marvel[answer]:
        print("❌ Too high in power! Try someone weaker.")

    guess += 1

if guess > 10:
    print(f"😔 Sorry! You're out of guesses. The correct answer was: '{pick.title()}'.")
