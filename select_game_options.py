import csv
import random

# Pick a random word from database based on game settings
def get_word(level, topic):
    words = []

    with open ("word_database.csv", "r") as file:
        reader = csv.DictReader(file, delimiter="\t")
        for row in reader:
            row_level = row["level"].strip().upper()
            row_topic = row["topic"].strip().lower()

            if row_level == level and row_topic == topic:
                words.append(row["word"])
                #print(words)
    #if not words:
    #    print('no matching word found', level, topic)

        selected_word = random.choice(words)
        print(selected_word)
        return selected_word