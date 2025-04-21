import csv
import random

# Selects 3 word-definition pairs
class MatchWordsGame:
    # pass database as a parameter for cleaner code, change for other files later
    def __init__(self, level, topic, filename="word_database.csv"):
        self.word_pairs = self.select_words(level, topic, filename)  # Load pairs based on level and topic
        self.chances = 3  # chances - since it's always 3 pairs it can be hardcoded
        self.correct_matches = 0  # count of correct matches

    # Read words from the database
    def select_words(self, level, topic, filename):
        pairs = []
        with open(filename) as file:
            reader = csv.DictReader(file, delimiter="\t")
            for row in reader:
                if row["level"].strip().upper() == level and row["topic"].strip().lower() == topic:
                    pairs.append((row["word"], row["definition"]))  # Store word-definition pair
            random.shuffle(pairs)  # Scramble the word-definition order
        return pairs[:3]  # Return 3 random word-definition pairs
