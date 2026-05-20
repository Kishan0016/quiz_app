# Quiz Questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. define", "B. func", "C. def", "D. function"],
        "answer": "C"
    }
]

# Quiz App Logic
score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.")

print(f"\n🎉 Your Final Score is: {score}/{len(questions)}")
