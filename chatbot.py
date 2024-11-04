# Define questions and answers
qa_pairs = {
    "What is your name?": "I am a chatbot created to answer your questions.",
    "How are you?": "I'm just a program, so I don't have feelings, but thank you for asking!",
    "What can you do?": "I can answer your questions and provide information.",
    "Tell me a joke.": "Why did the computer go to the doctor? Because it had a virus!",
    "What is Python?": "Python is a programming language known for its readability and versatility.",
    "Who created you?": "I was created by a developer using Python.",
    "How do I learn Python?": "You can learn Python by practicing, reading tutorials, and following online courses.",
    "What is AI?": "AI, or Artificial Intelligence, is the simulation of human intelligence in machines.",
    "Tell me a fact.": "Did you know? The first computer was invented in the 1940s.",
    "What is Taiga?": "Taiga is a project management tool often used for agile and scrum teams.",
}

# Main chatbot function
def chatbot():
    print("Hello! You can ask me questions. Type 'exit' to stop.")
    while True:
        # Get input from the user
        user_input = input("You: ")
        
        # Check if the user wants to exit
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        # Respond to known questions
        response = qa_pairs.get(user_input, "I'm sorry, I don't know the answer to that.")
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()