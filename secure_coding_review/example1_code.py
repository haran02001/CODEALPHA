from flask import Flask, request, render_template
from werkzeug.security import generate_password_hash
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Securely hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Store the username and hashed password in the database
        conn = get_db_connection()
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()

        return "Registration successful"

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Vulnerable to SQL Injection (for demonstration purposes)
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()

        if user:
            return "Login successful"
        else:
            return "Invalid credentials"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=False)
