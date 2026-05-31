import random
import datetime

def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good Morning! ☀️ Rise and shine!"
    elif hour < 17:
        return "Good Afternoon! 🌤️ Hope your day is going well!"
    else:
        return "Good Evening! 🌙 Hope you had a productive day!"

def get_response(user_input, username):
    responses = {
        "hello": [
            f"Hey {username}! How can I help you today? 😊",
            f"Hello {username}! What's on your mind?",
            f"Hi {username}! Ready to help! 🤖"
        ],
        "study": [
            "📚 Study Tips:\n  1. Use Pomodoro technique (25 min study, 5 min break)\n  2. Summarize notes after class\n  3. Teach concepts to others\n  4. Practice past papers!",
            "Best study method: Active recall! Test yourself instead of just reading 💡"
        ],
        "exam": [
            "📝 Exam Tips:\n  1. Start revision early\n  2. Practice previous papers\n  3. Sleep well before exam\n  4. Stay hydrated!",
            "Don't panic during exams! Read questions carefully first 💪"
        ],
        "stress": [
            f"Hey {username}, take a deep breath! 🌿\n  • Take short breaks\n  • Go for a walk\n  • Talk to a friend\n  • You've got this! 💪",
            "Stress is normal! Break big tasks into smaller ones and tackle them one by one 🎯"
        ],
        "motivation": [
            f"You've got this {username}! 🌟 Every expert was once a beginner!",
            "Success is not final, failure is not fatal — it's the courage to continue that counts! 💫",
            f"Believe in yourself {username}! Hard work always pays off! 🚀",
            "Dream big, work hard, stay focused! 🎯"
        ],
        "programming": [
            "💻 Programming Tips:\n  1. Practice daily — even 30 minutes helps!\n  2. Build real projects\n  3. Read others' code\n  4. Debug patiently!",
            "Best way to learn programming: Build something you actually want to use! 🛠️"
        ],
        "python": [
            "🐍 Python is amazing for beginners!\n  • Easy to read\n  • Huge library support\n  • Used in AI, Web, Data Science\n  Start with python.org!",
        ],
        "career": [
            "💼 Career Tips:\n  1. Build a strong GitHub portfolio\n  2. Network on LinkedIn\n  3. Do internships\n  4. Learn in-demand skills!",
            "Focus on skills + projects + networking = Great career! 🎯"
        ],
        "time": [
            f"⏰ Current time: {datetime.datetime.now().strftime('%I:%M %p')}",
        ],
        "date": [
            f"📅 Today is: {datetime.datetime.now().strftime('%A, %B %d, %Y')}",
        ],
        "joke": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
            "Why did the student eat his homework? Because the teacher told him it was a piece of cake! 😄",
            "I asked my computer for a joke... it said 'Error 404: Humor not found'! 😂",
            "Why do Java developers wear glasses? Because they don't C#! 🤓"
        ],
        "food": [
            "🍕 Brain foods for studying:\n  • Dark chocolate 🍫\n  • Nuts and seeds 🥜\n  • Blueberries 🫐\n  • Green tea 🍵",
        ],
        "sleep": [
            "😴 Sleep Tips:\n  • 7-8 hours minimum\n  • No phone 30 min before bed\n  • Sleep same time daily\n  • Good sleep = Better memory!",
        ],
        "help": [
            "I can help with:\n  📚 study, exam, programming, python\n  💪 motivation, stress, career\n  😄 joke, food, sleep, time, date"
        ],
        "bye": [
            f"Goodbye {username}! Keep learning and growing! 🌟",
            f"See you later {username}! Stay awesome! 💫",
            f"Bye {username}! Go conquer the world! 🚀"
        ],
        "thanks": [
            "You're welcome! Always here to help! 😊",
            f"Anytime {username}! That's what I'm here for! 🤖",
            "Happy to help! Keep it up! 🌟"
        ],
        "weather": [
            "I wish I could check weather! But I hope it's sunny for you! ☀️"
        ],
        "name": [
            "I'm StudyBot 🤖 — your personal student assistant!",
        ],
    }

    user_lower = user_input.lower().strip()

    for key in responses:
        if key in user_lower:
            return random.choice(responses[key])

    fallback = [
        f"Hmm, not sure about that {username}! Type 'help' to see what I can do 😊",
        "Interesting! Try asking me about study, exams, motivation or jokes! 🤖",
        f"I'm still learning {username}! Type 'help' for available topics 💡"
    ]
    return random.choice(fallback)

def chatbot():
    print("=" * 55)
    print("     🎓 StudyBot — Your Personal Student Assistant")
    print("=" * 55)
    print(f"  {get_greeting()}")
    print("=" * 55)

    username = input("What's your name? ").strip()
    if not username:
        username = "Student"

    print(f"\nWelcome {username}! I'm StudyBot, here to help you! 🎉")
    print("Type 'help' to see topics or 'quit' to exit\n")

    count = 0

    while True:
        user_input = input(f"{username}: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print(f"\nStudyBot: Goodbye {username}! We had {count} conversations today! 👋")
            print("StudyBot: Keep studying and stay motivated! 🌟")
            break

        response = get_response(user_input, username)
        count += 1
        print(f"StudyBot: {response}\n")

chatbot()