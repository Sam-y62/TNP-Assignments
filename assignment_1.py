import random
quiz_data = [
    {
        "question": "What does AI stand for?",
        "options": ["A. Artificial Interaction", "B. Artificial Intelligence", "C. Automatic Integration", "D. Algorithmic Interpretation"],
        "answer": "B"
    },
    {
        "question": "Who invented the World Wide Web?",
        "options": ["A. Alan Turing", "B. Tim Berners-Lee", "C. Bill Gates", "D. Steve Jobs"],
        "answer": "B"
    },
    {
        "question": "Which is not a primary color in the RGB color model?",
        "options": ["A. Red", "B. Green", "C. Blue", "D. Yellow"],
        "answer": "D"
    },
    {
        "question": "Which of the following is a frontend framework?",
        "options": ["A. React", "B. Django", "C. Flask", "D. Spring"],
        "answer": "A"
    },
    {
        "question": "What is the smallest unit of data in computing?",
        "options": ["A. Byte", "B. Bit", "C. Nibble", "D. Pixel"],
        "answer": "B"
    },
    {
        "question": "Which of the following is not a relational database management system?",
        "options": ["A. MySQL", "B. PostgreSQL", "C. MongoDB", "D. Oracle"],
        "answer": "C"
    },
    {
        "question": "What does IoT stand for?",
        "options": ["A. Internet of Technology", "B. Internet of Things", "C. Integration of Tools", "D. Interface of Technology"],
        "answer": "B"
    },
    {
        "question": "Which programming paradigm focuses on 'objects' that contain data and methods?",
        "options": ["A. Functional Programming", "B. Object-Oriented Programming", "C. Procedural Programming", "D. Event-Driven Programming"],
        "answer": "B"
    },
    {
        "question": "What is the name of the device that converts digital signals to analog and vice versa?",
        "options": ["A. Router", "B. Modem", "C. Switch", "D. Gateway"],
        "answer": "B"
    },
    {
        "question": "Which protocol is used to send email?",
        "options": ["A. HTTP", "B. FTP", "C. SMTP", "D. POP3"],
        "answer": "C"
    },
    {
        "question": "What does GPU stand for?",
        "options": ["A. General Processing Unit", "B. Graphics Processing Unit", "C. Game Processing Unit", "D. Geometric Processing Unit"],
        "answer": "B"
    },
    {
        "question": "Which cloud platform is developed by Microsoft?",
        "options": ["A. AWS", "B. Google Cloud", "C. Azure", "D. IBM Cloud"],
        "answer": "C"
    },
    {
        "question": "What is the primary role of a firewall in a network?",
        "options": ["A. To increase network speed", "B. To block unauthorized access", "C. To store data", "D. To enhance server capacity"],
        "answer": "B"
    },
    {
        "question": "Which of the following is not a search engine?",
        "options": ["A. Google", "B. Bing", "C. Yahoo", "D. WhatsApp"],
        "answer": "D"
    },
    {
        "question": "What is the file extension for Python scripts?",
        "options": ["A. .java", "B. .py", "C. .cpp", "D. .js"],
        "answer": "B"
    },
    {
        "question": "What is the main purpose of a DNS server?",
        "options": ["A. To store files", "B. To map domain names to IP addresses", "C. To provide security", "D. To host websites"],
        "answer": "B"
    },
    {
        "question": "What is the purpose of an operating system?",
        "options": ["A. To perform computations", "B. To serve as a database", "C. To manage hardware and software resources", "D. To compile code"],
        "answer": "C"
    },
    {
        "question": "Which company developed the Linux operating system?",
        "options": ["A. Microsoft", "B. IBM", "C. Linus Torvalds", "D. Red Hat"],
        "answer": "C"
    },
    {
        "question": "Which programming language is known as the language of the web?",
        "options": ["A. Java", "B. Python", "C. JavaScript", "D. Ruby"],
        "answer": "C"
    },
]

credentials = {
    "username": "admin",
    "password": "password123"
}

def login():
    print("Welcome to the MCQ game")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == credentials["username"] and password == credentials["password"]:
        print("Login successful! Welcome!")
        return True
    else:
        print("Login failed! Incorrect username or password.")
        return False


def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter your answer (A,B,C,D): ").upper()
    if user_answer == question_data["answer"]:
        return True
    else:
        return False


while True:
    if login()==True:
        break

score=0
random.shuffle(quiz_data)
for i in range(1,6):
    print(f'Question {i} of 5')
    if ask_question(quiz_data[i]):
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {quiz_data[i]['answer']}.\n")

print(f"You scored {score}/5.")