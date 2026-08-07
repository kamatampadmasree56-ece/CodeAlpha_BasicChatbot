import random
from datetime import datetime

print("=" * 60)
print("🤖 Welcome to THARA AI Assistant")
print("=" * 60)
print("Hello! I'm Thara.")
print("Type 'help' to see what I can do.")
print("Type 'bye' to exit.")
print("=" * 60)

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did Python go to school? To improve its class!",
    "Why do Java developers wear glasses? Because they don't C#."
]

quotes = [
    "Believe in yourself. Every expert was once a beginner.",
    "Success is the sum of small efforts repeated every day.",
    "Keep learning. Keep growing.",
    "Dream big and work hard."
]

responses = {
    "hi": "Hello! 👋",
    "hello": "Hi! Nice to meet you.",
    "hey": "Hey! How are you today?",
    "how are you": "I'm doing great! Thanks for asking. 😊",
    "what is your name": "My name is Thara AI Assistant.",
    "who are you": "I'm a Python chatbot created for the CodeAlpha Internship.",
    "good morning": "Good Morning! 🌞 Have a wonderful day.",
    "good afternoon": "Good Afternoon! 😊",
    "good evening": "Good Evening! 🌇",
    "good night": "Good Night! 🌙 Sweet dreams.",
    "thank you": "You're welcome! 😊",
    "thanks": "Happy to help!",
    "bye": "Goodbye! Have a wonderful day!"
}

while True:

    user = input("\nYou : ").lower().strip()

    if user == "bye":
        print("Thara :", responses["bye"])
        break

    elif user == "help":

        print("\n========== HELP ==========")
        print("hi")
        print("hello")
        print("how are you")
        print("what is your name")
        print("who are you")
        print("time")
        print("date")
        print("joke")
        print("quote")
        print("python")
        print("codealpha")
        print("bye")

    elif user == "time":
        print("Thara :", datetime.now().strftime("%I:%M %p"))

    elif user == "date":
        print("Thara :", datetime.now().strftime("%d-%m-%Y"))

    elif user == "joke":
        print("Thara :", random.choice(jokes))

    elif user == "quote":
        print("Thara :", random.choice(quotes))

    elif user == "python":
        print("Thara : Python is a simple, powerful and beginner-friendly programming language.")

    elif user == "codealpha":
        print("Thara : CodeAlpha provides internship opportunities and practical projects for students.")

    elif user in responses:
        print("Thara :", responses[user])

    else:
        print("Thara : Sorry, I don't understand that. Type 'help' to see available commands.")