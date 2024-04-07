import tkinter as tk
from tkinter import ttk, messagebox
from read_questions import get_questions_for_category

class QuizBowlApp:
    def __init__(self, master):
        self.master = master
        master.title("Quiz Bowl App")

        # Category Selection Frame
        self.category_frame = ttk.LabelFrame(master, text="Select a Category")
        self.category_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.selected_category = tk.StringVar()
        self.category_combobox = ttk.Combobox(self.category_frame, textvariable=self.selected_category)
        self.category_combobox['values'] = ['Adv Finance', 'Database', 'Python', 'Computer Forensics', 'FIN Modeling']
        self.category_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.category_combobox.current(0)

        self.start_button = ttk.Button(self.category_frame, text="Start Quiz", command=self.start_quiz)
        self.start_button.grid(row=0, column=2, padx=10, pady=10)

    def start_quiz(self):
        category = self.selected_category.get()
        self.questions = get_questions_for_category(category)
        if not self.questions:
            messagebox.showinfo("No Questions", "No questions found for the selected category.")
            return

        # Close the category selection window
        self.master.withdraw()

        # Open the quiz window
        self.quiz_window = tk.Toplevel(self.master)
        self.quiz_window.title("Quiz")

        self.current_question_index = 0
        self.display_current_question()

    def display_current_question(self):
        question_data = self.questions[self.current_question_index]

        self.question_var = tk.StringVar(value=question_data['question'])
        ttk.Label(self.quiz_window, textvariable=self.question_var, wraplength=400).grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.selected_option = tk.StringVar(value="")
        for i, option in enumerate(question_data['options'], start=1):
            ttk.Radiobutton(self.quiz_window, text=option, variable=self.selected_option, value=option).grid(row=i, column=0, sticky="w")

        self.submit_button = ttk.Button(self.quiz_window, text="Submit Answer", command=self.submit_answer)
        self.submit_button.grid(row=6, column=3, padx=10, pady=10)

    def submit_answer(self):
        selected_option = self.selected_option.get()
        correct_option = self.questions[self.current_question_index]['correct_answer']

        if selected_option == correct_option:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", "Incorrect! The correct answer was: " + correct_option)

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_current_question()
        else:
            messagebox.showinfo("Quiz Completed", "You've completed the quiz!")
            self.quiz_window.destroy()
            self.master.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizBowlApp(root)
    root.mainloop()
