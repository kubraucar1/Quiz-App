class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("invalid choice")
        return self.answer == answer


# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('answer: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        point = 100/ len(self.questions)
        totalPoint = round(self.score*point)
        print(f"Total {len(self.questions)} Question and you know {self.score} question")
        print("Total Point : ",totalPoint)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        print(f'Question {questionNumber} of {totalQuestion}'.center(50, '*'))


q1 = Question('What is the best programming language?', ['dart', 'python', 'javascript', 'java'], 'python')
q2 = Question('What is the most popular programming language?', ['dart', 'python', 'javascript', 'java'], 'java')
q3 = Question('What is the easiest programming language in the world?', ['dart', 'python', 'javascript', 'java'], 'dart')


questions = [q1, q2, q3]

quiz = Quiz(questions)

quiz.loadQuestion()