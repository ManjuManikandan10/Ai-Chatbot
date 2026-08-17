# AI Chatbot Web Application

A simple web-based chatbot application built with Python, Flask, MySQL, HTML, CSS, and JavaScript. Users can create an account, log in, chat with the bot, save their conversations, view chat history, and log out.

## Features

* User registration and login
* Session-based user authentication
* Protected chat page
* Rule-based chatbot responses
* MySQL database integration
* Automatic chat-history storage
* Chat-history retrieval
* Logout functionality

## Technologies Used

* **Python** — application programming language
* **Flask** — web framework
* **MySQL** — database
* **mysql-connector-python** — MySQL connection library
* **HTML, CSS, JavaScript** — web interface

## Project Structure

```text
project/
│
├── app.py
├── chatbot.py
├── database.py
├── test.py
├── templates/
│   ├── chat.html
│   ├── login.html
│   └── register.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── README.md
```

## How It Works

The application starts with the Flask server. Users can register or log in, and authenticated users are redirected to the chat page. When a user sends a message, Flask passes it to the chatbot, returns the answer, and stores the question and answer in MySQL.

```text
User
  │
  ▼
Login / Register
  │
  ▼
Flask Application
  │
  ├── User Authentication ──► MySQL
  │
  ▼
Chat Page
  │
  ▼
Send Question
  │
  ▼
/ask Route
  │
  ▼
Chatbot Response
  │
  └── Save Question + Answer ──► MySQL
```

### Chatbot

The main chatbot function is:

```python
get_ai_response(message)
```

The function converts the message to lowercase and checks for programmed keywords such as `hello`, `hi`, `python`, `flask`, and `bye`. If no matching keyword is found, it returns a default response.

### Example Responses

| User Input           | Chatbot Response                                                                             |
| -------------------- | -------------------------------------------------------------------------------------------- |
| `Hello`              | Hello! How can I help you today?                                                             |
| `What is your name?` | I am an AI Chatbot built using Python and Flask.                                             |
| `What is Python?`    | Python is a popular programming language used for web development, AI, automation, and more. |
| `What is Flask?`     | Flask is a lightweight Python web framework.                                                 |
| `Bye`                | Goodbye! Have a nice day.                                                                    |
| Unknown question     | Sorry, I don't understand that. Can you ask another question?                                |

## Installation

Make sure Python and MySQL are installed and that the MySQL server is running.

Check the Python version:

```bash
python --version
```

Install the required Python packages:

```bash
pip install flask mysql-connector-python
```

## Database Setup

Create the database in MySQL:

```sql
CREATE DATABASE chatbot_db;
USE chatbot_db;
```

Create the users table:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

Create the chat-history table:

```sql
CREATE TABLE chat_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## MySQL Configuration

Update the MySQL connection details in `database.py` for your own computer. The application expects the `chatbot_db` database to exist.

Do not upload your real database password to GitHub or another public repository. For a production application, store passwords and secret keys in environment variables.

## Running the Application

Start MySQL first, then run the Flask application:

```bash
python app.py
```

Open the local address shown in the terminal, normally:

```text
http://127.0.0.1:5000/
```

Register an account, log in, and then use the chatbot.

## Example Conversation

```text
You: Hello
Bot: Hello! How can I help you today?

You: What is Python?
Bot: Python is a popular programming language used for web development, AI, automation, and more.

You: What is Flask?
Bot: Flask is a lightweight Python web framework.

You: Bye
Bot: Goodbye! Have a nice day.
```

## Limitations

This project is a **rule-based chatbot**, not a generative AI system. Its responses are based on keywords programmed in `get_ai_response()`. It cannot understand arbitrary questions like a modern large language model.

The current application also uses direct password values and hard-coded configuration, so it should be treated as a learning project rather than a production system.

## Security Notes

Before deploying this application publicly, improve the following areas:

1. Hash user passwords instead of storing them directly.
2. Move the Flask secret key to an environment variable.
3. Move database credentials to environment variables.
4. Disable `debug=True` in production.
5. Add stronger input validation.
6. Add CSRF protection.
7. Add robust database error handling.

## Future Improvements

Possible improvements include:

* Password hashing
* Environment-based configuration
* CSRF protection
* Better input validation
* More chatbot responses
* Improved intent recognition
* Natural language processing
* AI API integration
* Better chat-history display
* Responsive web design
* Admin dashboard
* User profile management
* Production deployment

## Project Purpose

This project demonstrates how Python, Flask, MySQL, HTML, CSS, JavaScript, and a rule-based chatbot can be combined to build a basic full-stack web application.

