# jokes.py
import random

jokes = [
    ("Why did the chicken cross the road?", "To get to the other side!"),
    ("What do you call a bear with no teeth?", "A gummy bear!"),
    ("Why did the math book look sad?", "Because it had too many problems."),
    ("What do you call fake spaghetti?", "An impasta!"),
    ("How does a penguin build its house?", "Igloos it together!")
]

joke = random.choice(jokes)
print(f"Joke: {joke[0]}\nPunchline: {joke[1]}")