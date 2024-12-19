import os
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta


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
    file_name = input("Enter file name (or press Enter to use 'news_feed.xml'): ").strip()
    return os.path.join(default_folder, file_name or "news_feed.xml")


def append_to_txt_file(file_path, record):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(record + "\n")
    print(f"Record successfully added to {file_path}!")


def process_xml_file(file_path):
    if os.path.exists(file_path):
        print(f"Processing file: {file_path}")
        tree = ET.parse(file_path)
        root = tree.getroot()

        for record in root.findall('record'):
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


            record_data = {}
            if entry_type == "news":
                text = record.find('text')
                city = record.find('city')
                if text is not None and city is not None:
                    record_data = {
                        'text': text.text,
                        'city': city.text
                    }
                else:
                    print(f"Skipping record due to missing 'text' or 'city'.")
                    continue
            elif entry_type == "private_ad":
                text = record.find('text')
                expiration_date = record.find('expiration_date')
                if text is not None and expiration_date is not None:
                    record_data = {
                        'text': text.text,
                        'expiration_date': expiration_date.text
                    }
                else:
                    print(f"Skipping record due to missing 'text' or 'expiration_date'.")
                    continue
            elif entry_type == "unique":
                quote = record.find('quote')
                author = record.find('author')
                if quote is not None and author is not None:
                    record_data = {
                        'quote': quote.text,
                        'author': author.text
                    }
                else:
                    print(f"Skipping record due to missing 'quote' or 'author'.")
                    continue


            record_text = record_obj.entry(record_data)
            append_to_txt_file("news_feed.txt", record_text)

        os.remove(file_path)
        print(f"File '{file_path}' has been successfully processed and removed.")
    else:
        print(f"File '{file_path}' does not exist.")


while True:
    print("\nChoose an action:")
    print("1. Process and Remove File (XML format)")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        file_path = get_file_path()
        process_xml_file(file_path)
        continue
    elif choice == "2":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")