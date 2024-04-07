import sqlite3

conn= sqlite3.connect('newData.db')
curse = conn.cursor()

curse.execute("SELECT * FROM sqlite_master WHERE type='table'")
#Reads all table
print(curse.fetchall())
print()

curse.execute("SELECT * FROM Adv Finance")
print(curse.fetchall())
print()

curse.execute("SELECT * FROM Database")
print(curse.fetchall())
print()

curse.execute("SELECT * FROM Python")
print(curse.fetchall())
print()

curse.execute("SELECT * FROM Computer Forensics")
print(curse.fetchall())
print()

curse.execute("SELECT * FROM FIN Modeling")
print(curse.fetchall())
print()