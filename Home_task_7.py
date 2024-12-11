import csv
from collections import Counter
import string

def process_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def generate_word_count_csv(text):
    words = text.lower().split()
    ignored_words = {"---"}
    filtered_words = [word for word in words if word not in ignored_words]
    word_count = Counter(filtered_words)

    with open("word_count.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Word", "Count"])
        for word, count in word_count.items():
            writer.writerow([word, count])
    print("File 'word_count.csv' has been updated!")

def generate_letter_analysis_csv(text):
    text_clean = ''.join(filter(lambda c: c.isalpha(), text))
    text_lower = text_clean.lower()
    text_upper = ''.join(filter(lambda c: c.isupper(), text))

    letter_count_all = Counter(text_lower)
    letter_count_upper = Counter(text_upper)


    with open("letter_analysis.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Letter", "Count_All", "Count_Uppercase"])
        for letter in string.ascii_lowercase:
            count_all = letter_count_all.get(letter, 0)
            count_upper = letter_count_upper.get(letter.upper(), 0)
    print("File 'letter_analysis.csv' has been updated!")


input_file = "news_feed.txt"
text = process_file(input_file)
if text:
    generate_word_count_csv(text)
    generate_letter_analysis_csv(text)