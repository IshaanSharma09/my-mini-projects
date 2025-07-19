import random

words = (
    "aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo",
    "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly",
    "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken",
    "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab",
    "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin",
    "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle",
    "echidna", "eel", "eland", "elephant", "elk", "emu", "falcon", "ferret", "finch", "fish",
    "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat",
    "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull",
    "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse",
    "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo",
    "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion",
    "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill",
    "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse",
    "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter",
    "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin",
    "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea",
    "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer",
    "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion",
    "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider",
    "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan",
    "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture",
    "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat",
    "woodcock", "woodpecker", "worm", "wren", "yak", "zebra"
)

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

word = random.choice(words)
guessed_letters = set()
guess_count = 0

def display_word():
    for i in range(len(word)):
        if i == 3 or i == 6:
            print(word[i], end=' ')
        elif word[i] in guessed_letters:
            print(word[i], end=' ')
        else:
            print('_', end=' ')
    print()
if len(word) > 3:
    guessed_letters.add(word[3])
if len(word) > 6:
    guessed_letters.add(word[6])
print("Welcome to Hangman! Here's your word:")
display_word()

while guess_count < 6:
    answer = input("Guess a letter: ").lower()

    if not answer.isalpha() or len(answer) != 1:
        print("❌ Invalid input. Please enter a single alphabet letter.")
        continue

    if answer in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.add(answer)

    if answer in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        guess_count += 1

    display_word()
    print("\n".join(hangman_art[guess_count]))
    print("-" * 30)

    if all(c in guessed_letters or i == 3 or i == 6 for i, c in enumerate(word)):
        print("🎉 YOU WIN!")
        break
else:
    print("💀 GAME OVER!")
    print(f"The word was: {word}")
