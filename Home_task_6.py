import os
from datetime import datetime, timedelta

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

    def entry(self):
        """News entry."""
        text = input("Enter the news text: ")
        city = input("Enter the city: ")
        date = self.get_date()
        return f"--- News ---\n{text}\n{city}, {date}\n\n"


class PrivateAdEntry:
    def __init__(self):
        self.date_calculator = DateCalculator()

    def entry(self):
        text = input("Enter the ad text: ")
        expiration_date = input("Enter the expiration date (YYYY-MM-DD): ")
        expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        days_left = (expiration_date_obj - datetime.now().date()).days
        return f"--- Private Ad ---\n{text}\nExpires on: {expiration_date}, {days_left} days left\n\n"


class UniqueEntry:
    def __init__(self):
        self.date_calculator = DateCalculator()

    def entry(self):
        """Interesting fact (quote)."""
        quote = input("Enter the quote: ")
        author = input("Enter the author's name: ")
        date = datetime.now().strftime("%Y-%m-%d")
        return f"--- Interesting fact ---\n\"{quote}\" - {author}\nPublished on: {date}\n\n"


def get_file_path():
    """Get the file path from the user or use the default."""
    default_folder = os.path.join(os.getcwd(), "data")
    os.makedirs(default_folder, exist_ok=True)
    print(f"Default folder: {default_folder}")
    file_name = input("Enter file name (or press Enter to use 'news_feed.txt'): ").strip()
    return os.path.join(default_folder, file_name or "news_feed.txt")


def append_to_file(file_path, record):"
    with open(file_path, "a") as file:
        file.write(record)
    print(f"Record successfully added to {file_path}!")


def process_file(file_path):
    if os.path.exists(file_path):
        print(f"Processing file: {file_path}")
        os.remove(file_path)
        print(f"File '{file_path}' has been successfully processed and removed.")
    else:
        print(f"File '{file_path}' does not exist.")


while True:
    print("\nChoose an entry type:")
    print("1. News")
    print("2. Private Ad")
    print("3. Quote (Unique)")
    print("4. Process and Remove File")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        record = NewsEntry()
    elif choice == "2":
        record = PrivateAdEntry()
    elif choice == "3":
        record = UniqueEntry()
    elif choice == "4":
        file_path = get_file_path()
        process_file(file_path)
        continue
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    file_path = get_file_path()

    record_text = record.entry()
    append_to_file(file_path, record_text)