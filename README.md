# Live Cricket Data(event based)

### Project Description
The project consists of two main components: proxy_api.py and myapp.py.
#
### Getting Started
To run the project locally on your machine, follow these steps:
#
#### Prerequisites
You need to have a local web server set up, such as XAMPP, to host the project.
#
#### Installation and Setup
  1. Open the project in your preferred code editor, such as Visual Studio Code.
  2. Connect the database file to your local server. Ensure that your database configuration is correctly set up.
  3. Run proxy_api.py in your terminal to start the API proxy.
  4. Run myapp.py in your terminal to start the Flask application.
  5. Once the server is running, you will see a link or URL in the terminal where the Flask app is hosted.
  6. Open a web browser and paste the server URL into the address bar.
  7. You should now see the live cricket data displayed on the web page.
#
#### Customization
Make sure to replace the API URL as needed. You may need to configure the API endpoint in your code to fetch the cricket data from the source of your choice.
#
#### Project Structure
The project is structured as follows:
proxy_api.py: This file contains the code for the API proxy that fetches live cricket data.
myapp.py: This file contains the Flask application code that serves the web pages.
templates/: This directory holds the HTML templates used by the Flask app.
static/: This directory contains static files, such as CSS and images, used for styling and presentation.
# 
#### Dependencies
This project may require external libraries or dependencies. Make sure to install them using pip or another package manager.
1. For mysql connector: pip install mysql-connector-python
2. For Flask: pip install Flask
 
