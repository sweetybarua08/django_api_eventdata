from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Define database connection parameters
hostname = 'localhost'
username = 'root'
password = ''
database = 'match'

@app.route('/')
def index():
    # Establish a database connection
    connection = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )
    cursor = connection.cursor()

 # Retrieve the last row of data from the database using the auto-incremented ID column
    cursor.execute("SELECT * FROM match_info ORDER BY id DESC LIMIT 1")

    # Fetch the last row
    data = cursor.fetchone()

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    return render_template('banner.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
