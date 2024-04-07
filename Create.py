import sqlite3

conn = sqlite3.connect('newData.db')
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
    ("Adv Finance", "What does IPO stand for?", "Initial Product Offering", "Initial Public Offering", "Internal Public Offering", "Initial Private Offering", "B"),
    ("Adv Finance", "What is diversification?", "Investing in a variety of assets to reduce risk", "Investing all in one asset", "Reducing the number of investments", "Investing in international assets only", "A"),
    ("Adv Finance", "What is the primary goal of portfolio management?", "To maximize return for a given level of risk", "To minimize return for a given level of risk", "To invest in bonds only", "To invest in stocks only", "A"),
    ("Adv Finance", "What does CAPM stand for?", "Capital Asset Pricing Model", "Consumer Asset Pricing Model", "Capital Allocation Pricing Mechanism", "Corporate Asset Pricing Model", "A"),
    ("Adv Finance", "What is the formula for calculating net present value (NPV)?", "NPV = Net Cash Inflows - Initial Investment", "NPV = Initial Investment - Net Cash Inflows", "NPV = Net Cash Inflows / Initial Investment", "NPV = Initial Investment / Net Cash Inflows", "A"),
    ("Adv Finance", "What is meant by the time value of money?", "A dollar today is worth more than a dollar tomorrow", "A dollar today is worth less than a dollar tomorrow", "A dollar has the same value every day", "The concept is irrelevant in finance", "A"),
    ("Adv Finance", "What does WACC stand for?", "Weighted Average Cost of Capital", "Weighted Annual Cost of Capital", "Weighted Asset Cost of Capital", "Wide Area Cost of Capital", "A"),
    ("Adv Finance", "What is a bull market?", "A market showing consistent price increases", "A market showing consistent price decreases", "A market with fluctuating prices", "A market with stable prices", "A"),
    ("Adv Finance", "What does the Sarbanes-Oxley Act aim to improve?", "Corporate governance and accountability", "International trade regulations", "Environmental protection standards", "Employee benefits management", "A")
]


# Insert questions for 'Python'
python_questions = [
    ("Python", "What is the correct way to define a function in Python?", "def myFunction():", "function myFunction():", "create myFunction():", "func myFunction():", "A"),
    ("Python", "Which of the following data types is immutable?", "Tuple", "List", "Dictionary", "Set", "A"),
    ("Python", "How do you insert an item at a given position in a list in Python?", "list.insert(index, item)", "list.add(item, index)", "list.append(index, item)", "list.set(index, item)", "A"),
    ("Python", "What keyword is used to create a class in Python?", "class", "struct", "def", "object", "A"),
    ("Python", "Which module in Python is used for mathematical tasks?", "math", "string", "random", "datetime", "A"),
    ("Python", "How do you create a comment in Python?", "Using # at the beginning of the comment", "Using // at the beginning of the comment", "Using /* at the beginning of the comment", "Using <!-- at the beginning of the comment", "A"),
    ("Python", "What is the output of print(2 ** 3)?", "8", "6", "9", "5", "A"),
    ("Python", "What does the 'len()' function do in Python?", "Returns the length of an object", "Returns the size of an object", "Modifies the length of an object", "Deletes the object", "A"),
    ("Python", "Which of the following is the correct way to declare a dictionary?", "{'key': 'value'}", "['key': 'value']", "('key': 'value')", "<'key': 'value'>", "A"),
    ("Python", "What is a correct syntax to output 'Hello World' in Python?", "print('Hello World')", "echo 'Hello World'", "p('Hello World')", "printf('Hello World')", "A")
]

# Insert questions for 'Computer Forensics'
computer_forensics_questions = [
    ("Computer Forensics", "What is the primary goal of computer forensics?", "To recover and analyze data in a way that is legally admissible", "To delete data permanently", "To repair damaged software", "To enhance the speed of the computer", "A"),
    ("Computer Forensics", "Which of the following is a common tool used in computer forensics?", "EnCase", "Photoshop", "WinRAR", "Microsoft Word", "A"),
    ("Computer Forensics", "What is a write blocker?", "A device that prevents data from being modified on a storage device", "A software that blocks access to certain websites", "A tool that deletes data permanently", "A type of firewall", "A"),
    ("Computer Forensics", "What is the first rule of digital forensics?", "Do not alter the original data", "Always work on the system live", "Start by making a backup", "First, delete all unnecessary files", "A"),
    ("Computer Forensics", "Which of the following file systems is commonly used in Windows operating systems?", "NTFS", "HFS+", "ext4", "FAT32", "A"),
    ("Computer Forensics", "What is the process of making an exact copy of a drive called?", "Imaging", "Copying", "Cloning", "Mirroring", "A"),
    ("Computer Forensics", "Which of the following is a type of volatile memory?", "RAM", "HDD", "SSD", "ROM", "A"),
    ("Computer Forensics", "What is steganography?", "The practice of hiding data or messages within another file", "The study of viruses and malware", "The encryption of data", "The recovery of lost files", "A"),
    ("Computer Forensics", "In computer forensics, what is the term 'chain of custody' used for?", "Documenting the handling of evidence", "Linking a suspect to a piece of digital evidence", "Creating a backup of digital evidence", "The process of decrypting encrypted data", "A"),
    ("Computer Forensics", "What is the primary purpose of a forensic duplicate?", "To create an exact bit-for-bit copy of digital evidence", "To compress files for easy transport", "To enhance the quality of digital images", "To convert digital files into analog", "A")
]

database_questions = [
    ("Database", "What is SQL?", "Structured Query Language", "Simple Query Language", "Standard Question Language", "Sequential Query Language", "A"),
    ("Database", "What does 'PRIMARY KEY' in SQL indicate?", "A unique identifier for each row", "A primary function key", "A non-unique identifier for each row", "A special keyword for indexing", "A"),
    ("Database", "Which SQL statement is used to extract data from a database?", "SELECT", "EXTRACT", "GET", "PULL", "A"),
    ("Database", "What is a foreign key?", "A key used to link two tables together", "A key that is not important", "A key that is unique in each table", "A key used to encrypt data", "A"),
    ("Database", "What is normalization in database design?", "The process of minimizing redundancy", "The process of maximizing redundancy", "The process of deleting data", "The process of encrypting data", "A"),
    ("Database", "Which of the following is a NoSQL database?", "MongoDB", "MySQL", "Oracle", "SQL Server", "A"),
    ("Database", "Which command is used to remove rows from a table?", "DELETE", "REMOVE", "ERASE", "DROP", "A"),
    ("Database", "What is the default sort order of the 'ORDER BY' clause in SQL?", "Ascending", "Descending", "Random", "Alphabetical", "A"),
    ("Database", "What does DDL stand for in SQL?", "Data Definition Language", "Data Duplication Language", "Data Development Language", "Data Description Language", "A"),
    ("Database", "What is a transaction in a database?", "A unit of work that is either completed in its entirety or not done at all", "A type of database model", "A request to retrieve data", "A method to increase database speed", "A")
]

fin_modeling_questions = [
    ("FIN Modeling", "What is financial modeling used for?", "To make informed business and financial decisions", "To track inventory", "To manage employee records", "To monitor social media trends", "A"),
    ("FIN Modeling", "Which software is most commonly used for financial modeling?", "Microsoft Excel", "Google Sheets", "Notepad", "Microsoft Word", "A"),
    ("FIN Modeling", "What is a 'Discounted Cash Flow' model used to estimate?", "The current value of projected future cash flows", "A company's promotional expenses", "The amount of cash in the bank", "The company's debt levels", "A"),
    ("FIN Modeling", "In financial modeling, what does NPV stand for?", "Net Present Value", "New Product Value", "Net Private Value", "National Present Value", "A"),
    ("FIN Modeling", "What is a 'sensitivity analysis' in financial modeling?", "A technique to predict how different values of an independent variable affect a particular dependent variable", "An analysis of a company's sensitivity to market trends", "A review of a model's font sensitivity", "An analysis of the sensitivity of the company's stock", "A"),
    ("FIN Modeling", "What is typically the first step in building a financial model?", "Defining the model's purpose", "Selecting the model's color scheme", "Choosing the font size", "Deciding the number of sheets to use", "A"),
    ("FIN Modeling", "What does 'WACC' stand for in financial modeling?", "Weighted Average Cost of Capital", "Wide Area Communication Channel", "Weekly Average Company Cost", "Weighted Average Credit Card", "A"),
    ("FIN Modeling", "In a financial model, what is a 'scenario analysis' used for?", "To predict financial outcomes based on various financial scenarios", "To determine the best scenario for watching a movie", "To analyze the best-case scenario for employee vacations", "To create scenarios for company parties", "A"),
    ("FIN Modeling", "Why is it important to use 'assumptions' in financial models?", "To provide a basis for the model's calculations and projections", "To guess the CEO's preferences", "To assume the company's success", "To make the model look complex", "A"),
    ("FIN Modeling", "What is the primary purpose of creating financial models?", "To simulate the financial performance of a business under various conditions", "To create visual presentations for stakeholders", "To track the company's stock price", "To calculate employee bonuses", "A")
]

def insert_questions(data):
    for question in data:
        cursor.execute('''INSERT INTO Questions (CategoryName, Question, AnswerOption1, AnswerOption2, AnswerOption3, AnswerOption4, CorrectAnswer)
                        VALUES (?, ?, ?, ?, ?, ?, ?);''', question)


insert_questions(adv_finance_data)
insert_questions(python_questions)
insert_questions(computer_forensics_questions)
insert_questions(database_questions)
insert_questions(fin_modeling_questions)

# Commit and close
conn.commit()
conn.close()
