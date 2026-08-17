import mysql.connector


def get_connection():

    connection = mysql.connector.connect(

        host="localhost",

        user="root",

        password="Manju107@",

        database="chatbot_db"

    )

    return connection