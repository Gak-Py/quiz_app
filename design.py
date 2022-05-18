from tkinter import *
from quiz_machine import QuizMachine

THEME_COLOR = "#efefef"


class QuizUI:

    def __init__(self, quiz_brain: QuizMachine):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="#333", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill="#333",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/maru.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/batsu.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill="#333")
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz is End!\nYour Score is {self.quiz.score}", fill="#333")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="blue")
            self.canvas.itemconfig(self.question_text, fill="#fff")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="#fff")
        self.window.after(1000, self.get_next_question)








