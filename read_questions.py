import sqlite3

def get_questions_for_category(category_name):
    """
    Fetches questions for a given category from the database.

    :param category_name: The name of the category to fetch questions for.
    :return: A list of question dictionaries.
    """
    conn = sqlite3.connect('newData.db')
    cursor = conn.cursor()

    # Prepare the SQL query to fetch questions for the specified category
    query = '''
    SELECT Question, AnswerOption1, AnswerOption2, AnswerOption3, AnswerOption4, CorrectAnswer 
    FROM Questions 
    WHERE CategoryName = ?;
    '''

    # Execute the query
    cursor.execute(query, (category_name,))
    
    # Fetch all results
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert fetched data into a list of dictionaries for easier handling
    questions = []
    for row in rows:
        questions.append({
            'question': row[0],
            'options': [row[1], row[2], row[3], row[4]],
            'correct_answer': row[5]
        })

    return questions

# Example usage (uncomment to test)
# questions = get_questions_for_category('Python')
# for question in questions:
#     print(question)
