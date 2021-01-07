import random

quote = ["a stitch in time saves nine",
		 "Life is like a bicycle, to keep your balance you have to keep moving",
		 "Death is inevitable",
		 "Death is not the greatest lost in life",
		 "Life is sweet",
		 "The only way to learn code is by coding",
		 "Life is a biatch"
		]

random_quote = random.choice(quote)

print(f"Quote of the day: '{random_quote}' ")