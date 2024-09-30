# Secure Coding Recommendations

1. **SQL Injection Prevention**:
   Use parameterized queries to prevent SQL Injection.
   ```python
   user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
