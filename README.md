# Shakespearean MadLib

Southern Oregon University Hackathon 2023 project by Nole Stites

### Description of Project

My Hackathon project is a take on the classic game MadLibs. MadLibs, for those who do not know, is a game where an often humorous story is created by the player filling in certain blanks within the text. This project lets the user play a game of MadLibs themed after their choice of Shakespeare's plays. The webpage used to play the game uses the Flask library, which is a way for programmers to have a Python-based webpage with some minor HTML and CSS. Flask is a great tool to use so that the results of the forms you fill out for the game can be accessed and editted within Python.

### Setup Instructions
NOTE: The below instructions assume that you have a terminal that can run Linux commands successfully.

* If Python isn't installed, run this command:
* * $ sudo apt-get install python3.8
* Open a Linux terminal of your choice and clone the project using the following command:
* * $ git clone https://github.com/NoleStites/souhackathon2023.git
* Change your directory to be inside the project:
* * $ cd souhackathon2023
* Create a Python virtual environment:
* * $ python -m venv env
* * $ source env/bin/activate
* Once the environment is created, install Flask with the following command:
* * $ pip install -r requirements.txt
* Start the Flask application:
* * $ flask run
* When you run the previous command, you will see an output that says "Running on http://...". Go to the URL in a browser of your choice and have fun!



