from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection settings
db_config = {
    "host": "muradb-db-1.c3qesewy2b8j.eu-north-1.rds.amazonaws.com",  # Change to your MySQL server host
    "user": "admin",  # Change to your MySQL username
    "password": "1234567Python?",  # Change to your MySQL password
    "database": "List"  # Change to your database name
}

def get_items():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT id, description FROM items")
    items = cursor.fetchall()
    cursor.close()
    connection.close()
    return items

@app.route("/")
def index():
    items = get_items()
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)
