from flask import Flask, request, render_template
from werkzeug.security import check_password_hash
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Secure Query using Parameterized Query
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

        if user and check_password_hash(user['password'], password):
            return "Login successful"
        else:
            return "Invalid credentials"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=False)
