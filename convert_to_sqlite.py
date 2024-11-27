import sqlite3
import pandas as pd
import os

print("Current working directory:", os.getcwd())

# Step 1: Define CSV file paths and SQLite database name
videos_csv = "C:/Users/chris.mills/OneDrive - Woods Rogers Vandeventer Black PLC/Documents/Programs/tarbell_test/Videos.csv"  # Replace with your actual file path
books_csv = "C:/Users/chris.mills/OneDrive - Woods Rogers Vandeventer Black PLC/Documents/Programs/tarbell_test/Books.csv"    # Replace with your actual file path
database_name = "TarbellIndex.db"

# Step 2: Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# Step 3: Create Videos table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Videos (
    ID INTEGER PRIMARY KEY,
    Lesson TEXT,
    Subject TEXT,
    Title TEXT,
    Timestamp TEXT,
    Volume INTEGER,
    Page INTEGER,
    Description TEXT
)
''')

# Step 4: Create Books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    ID INTEGER PRIMARY KEY,
    Subject TEXT,
    Title TEXT,
    Category1 TEXT,
    Category2 TEXT,
    Volume INTEGER,
    Lesson TEXT,
    Page INTEGER,
    Inventor TEXT,
    Description TEXT
)
''')

# Step 5: Load CSV files into Pandas DataFrames
videos_df = pd.read_csv(videos_csv)
books_df = pd.read_csv(books_csv)

# Step 6: Insert data into Videos table
videos_df.to_sql('Videos', conn, if_exists='replace', index=False)

# Step 7: Insert data into Books table
books_df.to_sql('Books', conn, if_exists='replace', index=False)

# Step 8: Commit changes and close the database connection
conn.commit()
conn.close()

print(f"Data successfully imported into {database_name}")
