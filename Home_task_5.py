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


def append_to_file(record):
    file_name = "news_feed.txt"
    with open(file_name, "a") as file:
        file.write(record)
    print(f"Record successfully added to {file_name}!")


while True:
    print("\nChoose an entry type:")
    print("1. News")
    print("2. Private Ad")
    print("3. Quote (Unique)")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        record = NewsEntry()
    elif choice == "2":
        record = PrivateAdEntry()
    elif choice == "3":
        record = UniqueEntry()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue


    record_text = record.entry()
    append_to_file(record_text)
