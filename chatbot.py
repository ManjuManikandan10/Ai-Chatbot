def get_ai_response(message):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"

    elif "your name" in message:
        return "I am an AI Chatbot built using Python and Flask."

    elif "python" in message:
        return "Python is a popular programming language used for web development, AI, automation, and more."

    elif "flask" in message:
        return "Flask is a lightweight Python web framework."

    elif "bye" in message:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that. Can you ask another question?"