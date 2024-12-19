import sqlite3
from datetime import datetime

conn = sqlite3.connect('records.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    city TEXT NOT NULL,
                    date TEXT NOT NULL,
                    UNIQUE(text, city, date)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS private_ad (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    expiration_date TEXT NOT NULL,
                    days_left INTEGER NOT NULL,
                    UNIQUE(text, expiration_date)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS unique_facts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    quote TEXT NOT NULL,
                    author TEXT NOT NULL,
                    date TEXT NOT NULL,
                    UNIQUE(quote, author, date)
                )''')

conn.commit()


class DatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect('records.db')
        self.cursor = self.conn.cursor()

    def insert_news(self, text, city):
        date = datetime.now().strftime("%Y-%m-%d")
        try:
            self.cursor.execute("INSERT INTO news (text, city, date) VALUES (?, ?, ?)", (text, city, date))
            self.conn.commit()
            print("News record added successfully.")
        except sqlite3.IntegrityError:
            print("Duplicate news record. Skipping insertion.")

    def insert_private_ad(self, text, expiration_date, days_left):
        try:
            self.cursor.execute("INSERT INTO private_ad (text, expiration_date, days_left) VALUES (?, ?, ?)", (text, expiration_date, days_left))
            self.conn.commit()
            print("Private ad record added successfully.")
        except sqlite3.IntegrityError:
            print("Duplicate private ad record. Skipping insertion.")

    def insert_unique_fact(self, quote, author):
        date = datetime.now().strftime("%Y-%m-%d")
        try:
            self.cursor.execute("INSERT INTO unique_facts (quote, author, date) VALUES (?, ?, ?)", (quote, author, date))
            self.conn.commit()
            print("Unique fact record added successfully.")
        except sqlite3.IntegrityError:
            print("Duplicate unique fact record. Skipping insertion.")


class NewsEntry:
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.db_handler = DatabaseHandler()

    def entry(self):
        self.db_handler.insert_news(self.text, self.city)

class PrivateAdEntry:
    def __init__(self, text, expiration_date, days_left):
        self.text = text
        self.expiration_date = expiration_date
        self.days_left = days_left
        self.db_handler = DatabaseHandler()

    def entry(self):
        self.db_handler.insert_private_ad(self.text, self.expiration_date, self.days_left)

class UniqueEntry:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author
        self.db_handler = DatabaseHandler()

    def entry(self):
        self.db_handler.insert_unique_fact(self.quote, self.author)

# Example usage
news = NewsEntry("A new species of bird has been discovered in the Amazon rainforest.", "Manaus")
news.entry()

ad = PrivateAdEntry("Selling a new laptop in perfect condition.", "2024-12-25", 9)
ad.entry()

fact = UniqueEntry("To be or not to be, that is the question.", "William Shakespeare")
fact.entry()

# Close the connection when done
conn.close()
