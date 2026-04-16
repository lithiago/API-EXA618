from flask import Flask, jsonify, request, make_response
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

mydb = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=os.getenv("DB_PORT"),
    cursorclass=pymysql.cursors.DictCursor # Returns data as dictionaries
)


app = Flask(__name__)

@app.route("/authors", methods=["GET"])
def getAuthors():
    
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM Message")
    
    query_return = my_cursor.fetchall()
    authors = []
    
    for row in query_return:
        authors.append(row[1])
    
    return make_response(
        jsonify(
            mensagem="Autores",
            dados=authors
        )
    )
@app.route("/message", methods=["PUT"])
def sendMessage():
    message = request.json
    my_cursor = my_cursor()
    
    my_cursor.execute(f"INSERT INTO message (mensagem, Nome_Autor) VALUES('{message['message']}', '{message['author']}')")

    mydb.commit()
    
    return jsonify({"status": "Message sent!"}), 201
@app.route("/allMessages")
def getMessage():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM Message")
    
    query_retunr = my_cursor.fetchall()
    
    
    return make_response(
        jsonify(
            query_retunr
        )
    )


if __name__ == "__main__":
    app.run(debug=True)