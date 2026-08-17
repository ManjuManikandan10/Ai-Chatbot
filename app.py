from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from database import get_connection
from chatbot import get_ai_response

app = Flask(__name__)
app.secret_key = "my_secret_key"


# Home Page
@app.route("/")
def home():
    return redirect(url_for("login"))


# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO users(username,email,password)
        VALUES(%s,%s,%s)
        """

        cursor.execute(sql, (username, email, password))

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
        SELECT * FROM users
        WHERE email=%s AND password=%s
        """

        cursor.execute(sql, (email, password))

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect("/chat")

        return "Invalid Email or Password"

    return render_template("login.html")


# Chat Page
@app.route("/chat")
def chat():

    if "user_id" not in session:
        return redirect("/login")

    return render_template(
        "chat.html",
        username=session["username"]
    )


# Ask AI
@app.route("/ask", methods=["POST"])
def ask():

    if "user_id" not in session:
        return jsonify({"answer": "Please Login"})

    data = request.get_json()

    question = data["message"]

    answer = get_ai_response(question)

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO chat_history
    (user_id,question,answer)
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        sql,
        (
            session["user_id"],
            question,
            answer
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"answer": answer})


# Chat History
@app.route("/history")
def history():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT question,answer
    FROM chat_history
    WHERE user_id=%s
    ORDER BY id DESC
    """

    cursor.execute(sql, (session["user_id"],))

    chats = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(chats)


# Logout
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)