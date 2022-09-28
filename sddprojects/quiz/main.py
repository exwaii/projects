# “Who Wants to Be a University Student? version 8 – finished on 4/06/21 © 2022 by Xuanyu Liu 442731403”
# question files taken from Isaac, Markus and Chris
from random import shuffle, choices
from urllib.parse import unquote
import pandas as pd
from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable


# define a question class
class Question:
    def __init__(self, question: str, choices: list[str], answer: str) -> None:
        self.order = list(range(len(choices)))
        self.choices = choices
        shuffle(self.order)  # shuffles the order of the choices
        # converts answer to corresponding number with A being 0
        self.answer = ord(answer) - 65
        self.question = question  # stores question
        # think of order as a list of [A, B, C, D] and answer as one of the letters.
        # the order is then shuffled and when asking it follows the new arrangement of alphabets
        # eg if shuffled order is [D, B, C, A] then the original d option will be printed, then b etc
        # to check the answer we convert the user's answer to the corresponding index in the order list
        # and check if the variable of that index is equal to the answer (below)
        # e.g. if shuffled order is [D, B, C, A] and user answers D we check if order[3] = A is equal to the answer
        # this way the order can be shuffled without affecting the answer

    def ask_question(self) -> bool:
        while True:  # loops until valid answer is entered
            print(self.question)  # prints question
            # iterates through the shuffled order of the choices
            for i in range(len(self.order)):
                # prints the choice in the shuffled order
                print(f"{chr(i+65)}. {self.choices[self.order[i]]}")
            user_answer = input("Answer: ").upper()  # stores user answer
            # if answer is valid
            if len(user_answer) == 1 and user_answer in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:len(self.choices)]:
                if self.order[ord(user_answer) - 65] == self.answer:
                    return True
                return False
            # if answer is invalid
            print(
                f"\nI am sorry, I did not understand you - you must answer one of {', '.join(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(self.choices)]))} (case insensitive)")


# loads question csv file from file path and returns a list of question objects
def load_csv(path) -> list[Question]:
    df = pd.read_csv(path)  # loads csv file as dataframe
    return [Question(row.question, [row.a, row.b, row.c, row.d], row.answer) for row in df.itertuples(index=False)]
    # iterates through dataframe row by row and adds a question object with the question, choices, answer from row to list


# loads question from trivia url
def load_trivia(category_id) -> list[Question]:
    response = requests.get(
        f"https://opentdb.com/api.php?amount=20&category={category_id}&encode=url3986")
    response = response.json()["results"]
    return [
        Question(
            unquote(question['question']),
            [unquote(question['correct_answer'])] + [unquote(inc_answer)
                                                     for inc_answer in question['incorrect_answers']],
            "A",
        )
        for question in response
    ]
    # iterates through each item and inputs choices as [correct ans, incorrect x3] and answer A, unquoting the strings
    # choices will be shuffled on initialisation regardless so setting answer as A is fine


# loads question from quizlet url
def load_quizlet(id) -> list[Question]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        "referer": "https://google.com/",
    }
    # to dodge captcha
    response = requests.get(
        f"https://quizlet.com/au/{id}", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')  # stores html as soup
    qanswers = soup.find_all("span", attrs={"class": "TermText"})
    qanswers = {
        qanswers[i].text: qanswers[i + 1].text for i in range(0, len(qanswers), 2)
    }
    # both quizlet terms and definitions are stored in span tags with class TermText
    # findall finds them from left to right down the page, so the list altenates between terms and their definitions
    keys = list(qanswers.keys())
    shuffle(keys)
    return [
        Question(
            f"What is the definition of {word}?",
            [qanswers[word]] + choices(tuple(qanswers.values()), k=3),
            "A",
        )
        for word in keys[:20]]
    # however, there are around 100-200 questions in the quizlet, so we only take the first 20 and shuffle them for the quiz
    # again, choices will be shuffled on initialisation regardless so setting answer as A is fine


def greet_user() -> str:
    print("""
 / @ @ \\
( > º < )
  >>x<<
 /  O  \\""")
    print("Let's play Who Wants to Be a University Student!")
    name = input("Please enter your name: ")  # stores user's name
    print(f"Welcome {name}! You have 1 point(s).")
    return name  # returns user name


# returns True if user wants to play and False otherwise
def quiz_end(name, points, topic, correct, total) -> bool:
    print(f"Game over, {name}!")
    print(f"You answered {correct} out of {total} question(s) correctly.")
    scores = pd.read_csv("./scores.csv")
    highscore = False  # flag for congratulatory message
    for i, score in enumerate(scores[topic]):
        if points >= score:  # if user score in the top 5 is equal to or less
            scores[topic] = pd.concat(
                [scores.loc[:i-1, topic] if i != 0 else pd.Series([], dtype=str),
                 pd.Series([points]),
                 scores.loc[i:, topic]],
                ignore_index=True
            )
            # replace score list with updated list of scores
            scores[topic+" names"] = pd.concat(
                [scores.loc[:i-1, topic+" names"] if i != 0 else pd.Series([], dtype=int),
                 pd.Series([name]),
                 scores.loc[i:, topic+" names"]],
                ignore_index=True
            )
            # replace name list with updated list of names
            scores.to_csv("./scores.csv", mode='w')
            # update scores.csv
            highscore = True
            # set flag for congratulatory message to be True
            break
    print(f"Displaying highscores for {topic}")
    x = PrettyTable()
    x.add_column("Username", scores[topic+" names"])
    x.add_column("Highscore", scores[topic])
    # display highscores with prettytable
    print(x)
    print(
        f"Your high score is {points} points.")
    if highscore:
        print("Congratulations! You are in the top 5 scores for this topic!")
        # congratulates if set a top 5 score
    return True if input("Do you want to continue playing this game? (y/n) ").lower() == "y" else False


# QUESTION FILE PATH DICTIONARY
PATHS = {
    "Data Structures": "./DataStructures.csv",
    "Social Contexts of Software Design": "./SocialContext.csv",
    "Input and Output": "./InputOutput.csv",
    "System Modelling Tools": "./SystemModellingTools.csv",
}

# TRIVIA API CATEGORY ID DICTIONARY
TRIVIA_TOPICS = {
    "Any": "0",
    "General Knowledge": "9",
    "Books": "10",
    "Movies": "11",
    "Music": "12",
    "Musicals and theatres": "13",
    "Television": "14",
    "Video games": "15",
    "Board games": "16",
    "Science: Nature": "17",
    "Science: Computers": "18",
    "Science: Mathematics": "19",
    "Mythology": "20",
    "Sports": "21",
    "Geography": "22",
    "History": "23",
    "Politics": "24",
    "Art": "25",
    "Celebrities": "26",
    "Animals": "27",
    "Vehicles": "28",
    "Comics": "29",
    "Science: Gadgets": "30",
    "Anime and manga": "31",
    "Cartoons": "32",
}

# QUIZLET SITE ID DICTIONARY
QUIZLET_IDS = {
    "Terminology": "218063564/hsc-software-design-and-development-flash-cards/",
}

def main():
    name = greet_user()  # stores username received from greeting function
    while True:
        if input("Would you like to (enter a or b)\na) Study SDD\nb) Play trivia\n").lower() == "a":
            # if user wants to study SDD
            if input("Would you like to (enter a or b)\na) Study general terminology\nb) A specific topic\n") == "a":
                # if user wants to study quizlet flashcards
                topic = "Terminology"
                questions = load_quizlet(QUIZLET_IDS[topic])
            else:
                # if user wants to study questions on specific topics
                for file_topic in PATHS:
                    print(file_topic)
                while True:
                    topic = input("Please enter a topic: ")
                    if topic in PATHS:  # repeat until valid topic
                        break
                    print(
                        "I am sorry, I did not understand you - please enter a valid topic")
                questions = load_csv(PATHS[topic])
            shuffle(questions)
            # only questions from files need to be shuffled -
            # quizlet questions are already shuffled in quizlet function,
            # trivia questions are already shuffled as api gives a new set of questions each time
        else:
            # if user wants to play trivia
            for trivia_topic in TRIVIA_TOPICS:
                print(trivia_topic)  # displays the topics
            while True:
                topic = input(
                    "Please enter a topic (case insensitive) from above: ").lower().capitalize()  # stores topic
                if topic in TRIVIA_TOPICS.keys():
                    questions = load_trivia(TRIVIA_TOPICS[topic])
                    break  # repeat until valid topic
                print(
                    "I am sorry, I did not understand you - please enter a valid topic")

        points = 1  # initialises points value of 1
        correct = 0  # initialises number of questions correctly answered
        for i in range(len(questions)):  # loops through questions
            print(f"\nQuestion {i + 1}.")  # prints question number
            # calls question object's ask_question method and stores result
            if questions[i].ask_question():
                points *= 2  # double points
                print(f"Correct! You have {points} point(s).")  # prints points
                correct += 1  # adds 1 to number of correctly answered
            else:
                points = 1  # if incorrect, reset points to 1
                # prints points and correct answer
                print(
                    f"Incorrect! You have {points} point(s).\nThe correct answer is {chr(65 + questions[i].order.index(questions[i].answer))}")
        # displays and stores highscores, congratulating if user got a top 5 highscore
        # is user playing again?
        if not quiz_end(name, points, topic, correct, len(questions)):
            break


    print("Thank you for playing Who Wants to Be a Uni Student!")


if __name__ == "__main__":
    main()

