import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samule L. Jackson"]

people2 = ["Adebayo", "Rilwan", "Ajibola", "Americana"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_person2 = random.choice(people2)

# print(f"How about you go to {random_bar} with {random_person}")
print(f"How about you go to {random_bar} with {random_person2}")


