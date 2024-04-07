import sqlite3

conn = sqlite3.connect('QData34.db')
cursor = conn.cursor()

# Create Categories table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT NOT NULL
);
''')

# Create Questions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Questions (
    QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
    Question TEXT NOT NULL,
    CategoryName TEXT NOT NULL,
    AnswerOption1 TEXT NOT NULL,
    AnswerOption2 TEXT NOT NULL,
    AnswerOption3 TEXT NOT NULL,
    AnswerOption4 TEXT NOT NULL,
    CorrectAnswer CHAR(1) NOT NULL
);
''')

# Insert categories
categories = ['Adv Finance', 'Database', 'Python', 'Computer Forensics', 'FIN Modeling']
for category in categories:
    cursor.execute('INSERT INTO Categories (CategoryName) VALUES (?);', (category,))

conn.commit()

# Insert questions for 'Adv Finance'
adv_finance_data = [
    ("Adv Finance", "What is the formula for ROI?", "Gain from Investment / Cost of Investment", "Gain from Investment - Cost of Investment", "Cost of Investment / Gain from Investment", "Cost of Investment - Gain from Investment", "A"),
    # Add the rest of your 'Adv Finance' questions here
]

# Insert questions for 'Python'
python_questions = [
    ("Python", "What is the correct way to define a function in Python?", "def myFunction():", "function myFunction():", "create myFunction():", "func myFunction():", "A"),
    # Add the rest of your 'Python' questions here
]

# Insert questions for 'Computer Forensics'
computer_forensics_questions = [
    ("Computer Forensics", "What is the primary goal of computer forensics?", "To recover and analyze data in a way that is legally admissible", "To delete data permanently", "To repair damaged software", "To enhance the speed of the computer", "A"),
    # Add the rest of your 'Computer Forensics' questions here
]

database_questions = [
    ("Computer Forensics", "What is the primary goal of computer forensics?", "To recover and analyze data in a way that is legally admissible", "To delete data permanently", "To repair damaged software", "To enhance the speed of the computer", "A"),
    # Add the rest of your 'Computer Forensics' questions here
]

finmodeling_questions = [
    ("Computer Forensics", "What is the primary goal of computer forensics?", "To recover and analyze data in a way that is legally admissible", "To delete data permanently", "To repair damaged software", "To enhance the speed of the computer", "A"),
    # Add the rest of your 'Computer Forensics' questions here
]
# Function to insert questions
def insert_questions(data):
    for question in data:
        cursor.execute('''INSERT INTO Questions (CategoryName, Question, AnswerOption1, AnswerOption2, AnswerOption3, AnswerOption4, CorrectAnswer)
                        VALUES (?, ?, ?, ?, ?, ?, ?);''', question)

# Inserting questions into the database
insert_questions(adv_finance_data)
insert_questions(python_questions)
insert_questions(computer_forensics_questions)
insert_questions(computer_forensics_questions)
insert_questions(computer_forensics_questions)

# Commit and close
conn.commit()
conn.close()
