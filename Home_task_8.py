import os
import json
from datetime import datetime, timedelta
import csv
from collections import Counter
import string


class CurrentDate:
    def __init__(self):
        self.date = datetime.now().date()

    def show_res(self):
        print(f"Current date: {self.date}")


class DateCalculator:
    def __init__(self, expiration=0):
        self.expiration = expiration

    def calculate_days_left(self):
        today = datetime.now().date()
        target_date = today + timedelta(days=self.expiration)
        days_left = (target_date - today).days
        return days_left


class NewsEntry:
    def __init__(self):
        self.date_calculator = DateCalculator()

    def get_date(self):
        return datetime.now().strftime("%Y-%m-%d")

    def entry(self, data):
        text = data.get('text')
        city = data.get('city')
        date = self.get_date()
        return f"--- News ---\n{text}\n{city}, {date}\n\n"


class PrivateAdEntry:
    def __init__(self):
        self.date_calculator = DateCalculator()

    def entry(self, data):
        text = data.get('text')
        expiration_date = data.get('expiration_date')
        expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        days_left = (expiration_date_obj - datetime.now().date()).days
        return f"--- Private Ad ---\n{text}\nExpires on: {expiration_date}, {days_left} days left\n\n"


class UniqueEntry:
    def __init__(self):
        self.date_calculator = DateCalculator()

    def entry(self, data):
        quote = data.get('quote')
        author = data.get('author')
        date = datetime.now().strftime("%Y-%m-%d")
        return f"--- Interesting fact ---\n\"{quote}\" - {author}\nPublished on: {date}\n\n"


def get_file_path():
    default_folder = os.path.join(os.getcwd(), "data")
    os.makedirs(default_folder, exist_ok=True)
    print(f"Default folder: {default_folder}")
    file_name = input("Enter file name (or press Enter to use 'news_feed.json'): ").strip()
    return os.path.join(default_folder, file_name or "news_feed.json")


def append_to_file(file_path, record):
    with open(file_path, "a") as file:
        file.write(record)
    print(f"Record successfully added to {file_path}!")


def process_file(file_path):
    if os.path.exists(file_path):
        print(f"Processing file: {file_path}")
        with open(file_path, "r") as file:
            data = json.load(file)

        for record in data.get('records', []):
            entry_type = record.get('type')
            if entry_type == "news":
                record_obj = NewsEntry()
            elif entry_type == "private_ad":
                record_obj = PrivateAdEntry()
            elif entry_type == "unique":
                record_obj = UniqueEntry()
            else:
                print(f"Unknown entry type: {entry_type}")
                continue

            record_text = record_obj.entry(record)
            append_to_file(file_path, record_text)

        os.remove(file_path)
        print(f"File '{file_path}' has been successfully processed and removed.")
    else:
        print(f"File '{file_path}' does not exist.")


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
            writer.writerow([letter, count_all, count_upper])
    print("File 'letter_analysis.csv' has been updated!")


while True:
    print("\nChoose an action:")
    print("1. Process and Remove File (JSON format)")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        file_path = get_file_path()
        process_file(file_path)
        continue
    elif choice == "2":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")