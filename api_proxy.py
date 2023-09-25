import requests
import mysql.connector
from datetime import datetime, timedelta

# Define the URL for fetching data
url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/match/details?lang=en&seriesId=1398686&matchId=1399062&latest=true'

# Fetch the JSON response
response = requests.get(url)

# Check if the response was successful
if response.status_code != 200:
    print(f'Error fetching content: {response.status_code}')
    exit()

data = response.json()

# Extract the specific data you need
match = data['match']
matchId = match['objectId']
liveStatus = match['status']
series = match['series']
teamName = series['alternateName']
supportInfo = data['supportInfo']
liveSummary = supportInfo['liveSummary']
recentBalls = liveSummary['recentBalls']
firstRecentBall = recentBalls[0]  # Get the first recent ball
# Extract the desired data points
isFour = firstRecentBall['isFour']
isSix = firstRecentBall['isSix']
isWicket = firstRecentBall['isWicket']
oversActual = firstRecentBall['oversActual']

# Display the extracted data
print(f"Status: {liveStatus}")
print(f"Match Id: {matchId}")
print(f"Team Name: {teamName}")
print(f"Over: {oversActual}")
print(f"Four: {isFour}")
print(f"Six: {isSix}")
print(f"Wicket: {isWicket}")

# Database connection parameters
hostname = 'localhost'
username = 'root'
password = ''
database = 'match'

# Create a database connection
connection = mysql.connector.connect(
    host=hostname,
    user=username,
    password=password,
    database=database
)

# Check if a record with the same over exists in the database
check_existing_sql = "SELECT * FROM match_info WHERE oversActual = %s"
cursor = connection.cursor()
cursor.execute(check_existing_sql, (oversActual,))
existing_row = cursor.fetchone()

if existing_row:
    # A record with the same over exists
    last_updated = existing_row[7]  # Index 7 corresponds to lastUpdated field
    
    # Check if the record was updated more than 1 minute ago
    time_now = datetime.now()
    update_interval = timedelta(seconds=20)
    
    if time_now - last_updated > update_interval:
        # Update the existing record
        update_sql = """
            UPDATE match_info
            SET liveStatus = %s, matchId = %s, teamName = %s, isFour = %s, isSix = %s, isWicket = %s, lastUpdated = NOW()
            WHERE oversActual = %s
        """
        cursor.execute(update_sql, (liveStatus, matchId, teamName, isFour, isSix, isWicket, oversActual))
        connection.commit()
        print("Data updated in the database successfully.")
    else:
        # Skip the update, data was updated recently
        print("Data was updated recently. Skipping the update.")
else:
    # No record with the same over found, insert a new record
    insert_sql = """
        INSERT INTO match_info (liveStatus, matchId, teamName, oversActual, isFour, isSix, isWicket, lastUpdated)
        VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
    """
    cursor.execute(insert_sql, (liveStatus, matchId, teamName, oversActual, isFour, isSix, isWicket))
    connection.commit()
    print("Data saved to the database successfully.")

# Close the cursor and database connection
cursor.close()
connection.close()
