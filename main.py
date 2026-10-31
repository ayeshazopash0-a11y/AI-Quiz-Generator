
import json
import random
from dataclasses import dataclass, asdict

# Structured output schema
@dataclass
class Question:
    question: str
    options: list[str]
    correct_answer: str
    explanation: str

@dataclass
class Quiz:
    topic: str
    questions: list[Question]

# Local question bank
QUESTION_BANK = {
    "python": [
        Question(
            "Which keyword defines a function?",
            ["def", "func", "function", "define"],
            "def",
            "Python uses def to define functions."
        ),
        Question(
            "Which data type stores True or False?",
            ["str", "bool", "int", "list"],
            "bool",
            "Boolean values are True or False."
        ),
        Question(
            "Which symbol starts a comment?",
            ["//", "#", "/*", "--"],
            "#",
            "Python uses # for single-line comments."
        )
    ],
    "ai": [
        Question(
            "What does AI stand for?",
            ["Artificial Intelligence", "Auto Internet",
             "Advanced Input", "Artificial Interface"],
            "Artificial Intelligence",
            "AI means Artificial Intelligence."
        ),
        Question(
            "What is machine learning?",
            ["Learning from data", "Writing HTML",
             "Building hardware", "Manual typing"],
            "Learning from data",
            "Machine learning finds patterns in data."
        ),
        Question(
            "What is an LLM?",
            ["Large Language Model", "Local Logic Machine",
             "Linked Learning Mode", "Long List Method"],
            "Large Language Model",
            "LLMs process and generate language."
        )
    ]
}

# Tool function
def generate_quiz(topic):
    topic = topic.lower().strip()

    if topic not in QUESTION_BANK:
        raise ValueError("Choose Python or AI.")

    questions = random.sample(
        QUESTION_BANK[topic], 3
    )

    return Quiz(topic=topic, questions=questions)

# Validate structured output
def validate_quiz(quiz):
    assert isinstance(quiz.topic, str)
    assert len(quiz.questions) == 3

    for question in quiz.questions:
        assert len(question.options) == 4
        assert question.correct_answer in question.options

    return True

# Main assistant
def main():
    print("================================")
    print("    AI QUIZ ASSISTANT")
    print("    Tool Calling + JSON Output")
    print("================================")

    topic = input("Enter topic (Python/AI): ")

    try:
        print("\nCalling generate_quiz tool...")

        quiz = generate_quiz(topic)
        validate_quiz(quiz)

        output = asdict(quiz)

        with open("output.json", "w", encoding="utf-8") as file:
            json.dump(output, file, indent=4)

        print("\nTool executed successfully!")
        print("Structured JSON validated!")
        print("Saved to output.json\n")

        print(json.dumps(output, indent=4))

    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
