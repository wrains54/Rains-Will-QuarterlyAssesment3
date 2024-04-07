import sqlite3

# Establish a connection to the database, it will create one if it doesn't exist
conn = sqlite3.connect('QData.db')
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
    CategoryID INTEGER,
    Question TEXT NOT NULL,
    AnswerOption1 TEXT NOT NULL,
    AnswerOption2 TEXT NOT NULL,
    AnswerOption3 TEXT NOT NULL,
    AnswerOption4 TEXT NOT NULL,
    CorrectAnswer CHAR(1) NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);
''')

# Insert categories
categories = ['Adv Finance', 'Database', 'Python', 'Computer Forensics', 'FIN Modeling']
for category in categories:
    cursor.execute('INSERT INTO Categories (CategoryName) VALUES (?);', (category,))

# Commit the changes for categories
conn.commit()

# Since we need CategoryIDs for inserting questions, let's fetch these IDs after they are inserted
category_ids = {}
cursor.execute('SELECT CategoryID, CategoryName FROM Categories;')
for row in cursor.fetchall():
    category_ids[row[1]] = row[0]

# Prepare the data for each category (example for Adv Finance)
adv_finance_data = [
    (category_ids['Adv Finance'], "What is the formula for ROI?", "Gain from Investment / Cost of Investment", "Gain from Investment - Cost of Investment", "Cost of Investment / Gain from Investment", "Cost of Investment - Gain from Investment", "A"),
    (category_ids['Adv Finance'], "What does IPO stand for?", "Initial Product Offering", "Initial Public Offering", "Internal Public Offering", "Initial Private Offering", "B"),
    (category_ids['Adv Finance'], "What is diversification?", "Investing in a variety of assets to reduce risk", "Investing all in one asset", "Reducing the number of investments", "Investing in international assets only", "A"),
    (category_ids['Adv Finance'], "What is the primary goal of portfolio management?", "To maximize return for a given level of risk", "To minimize return for a given level of risk", "To invest in bonds only", "To invest in stocks only", "A"),
    (category_ids['Adv Finance'], "What does CAPM stand for?", "Capital Asset Pricing Model", "Consumer Asset Pricing Model", "Capital Allocation Pricing Mechanism", "Corporate Asset Pricing Model", "A"),
    (category_ids['Adv Finance'], "What is the formula for calculating net present value (NPV)?", "NPV = Net Cash Inflows - Initial Investment", "NPV = Initial Investment - Net Cash Inflows", "NPV = Net Cash Inflows / Initial Investment", "NPV = Initial Investment / Net Cash Inflows", "A"),
    (category_ids['Adv Finance'], "What is meant by the time value of money?", "A dollar today is worth more than a dollar tomorrow", "A dollar today is worth less than a dollar tomorrow", "A dollar has the same value every day", "The concept is irrelevant in finance", "A"),
    (category_ids['Adv Finance'], "What does WACC stand for?", "Weighted Average Cost of Capital", "Weighted Annual Cost of Capital", "Weighted Asset Cost of Capital", "Wide Area Cost of Capital", "A"),
    (category_ids['Adv Finance'], "What is a bull market?", "A market showing consistent price increases", "A market showing consistent price decreases", "A market with fluctuating prices", "A market with stable prices", "A"),
    (category_ids['Adv Finance'], "What does the Sarbanes-Oxley Act aim to improve?", "Corporate governance and accountability", "International trade regulations", "Environmental protection standards", "Employee benefits management", "A")
]

# Insert questions for Adv Finance
for data in adv_finance_data:
    cursor.execute('INSERT INTO Questions (CategoryID, Question, AnswerOption1, AnswerOption2, AnswerOption3, AnswerOption4, CorrectAnswer) VALUES (?, ?, ?, ?, ?, ?, ?);', data)

# Commit the changes for questions
conn.commit()

# Close the connection
conn.close()
