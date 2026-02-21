from flask import Flask, render_template, request
import mysql.connector
import time

app = Flask(__name__)

# Wait for DB container
time.sleep(10)

db_config = {
    "host": "db",
    "user": "root",
    "password": "root",
    "database": "usersdb"
}

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)

    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()

    cursor.close()
    conn.close()

    return "User Registered Successfully 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
