from datetime import datetime


class User:
    def __init__(self, user_id: int, user_name: str):
        self.user_id = user_id
        self.user_name = user_name

    def __str__(self):
        return f"Name: {self.user_name}, ID: {self.user_id}"


class Product:
    def __init__(self, prod_id: int, prod_name: str):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.questions = []

    def add_question(self, question: 'Question'):
        self.questions.append(question)


class Question:
    def __init__(self, ques_id: int, ques: str, product: Product):
        self.ques_id = ques_id
        self.ques = ques
        self.answers = []
        product.add_question(self)

    def add_answer(self, answer: 'Answer'):
        self.answers.append(answer)


class Answer:
    def __init__(self, ans_id: int, ans: str, question: Question, user: User):
        self.ans_id = ans_id
        self.ans = ans
        self.user = user
        self.votes = 0
        self.time = datetime.now()
        question.add_answer(self)

    def upvote(self):
        self.votes += 1

    def downvote(self):
        self.votes -= 1

    def __le__(self, other: 'Answer') -> bool:
        return self.votes <= other.votes

    def __str__(self):
        return f"Answer: {self.ans}, Votes: {self.votes}, By: {self.user.user_name}"


# Demo Code
if __name__ == "__main__":
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    product = Product(101, "Laptop")

    question1 = Question(1, "What is the battery life?", product)

    answer1 = Answer(1, "Around 10 hours", question1, user1)
    answer2 = Answer(2, "It depends on usage", question1, user2)

    answer1.upvote()
    answer1.upvote()
    answer2.upvote()

    print(f"Product: {product.prod_name}")
    for q in product.questions:
        print(f"Question: {q.ques}")
        for a in q.answers:
            print(a)
