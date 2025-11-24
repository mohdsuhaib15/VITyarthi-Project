# VITyarthi-Project
Project Title: Calorie Tracker

 Overview of the project: 
 Calorie​‍​‌‍​‍‌​‍​‌‍​‍‌ Tracker is an easy-to-use Python command-line tool that allows users to keep track and handle their calorie intake for each day. With the help of the Harris-Benedict formula and an activity multiplier, it first determines the user's daily calorie goal based on their input attributes (weight, height, age, and gender). If a food is not known, it can be added with its calorie content for the next time. The whole data is stored locally and users can work with the program even if they are ​‍​‌‍​‍‌​‍​‌‍​‍‌offline. 
 
 Features:
 • Personalized daily calorie goal calculation based on BMR.
 • Persistent local storage of user data and food calorie information.
 • Supports adding calorie intake via numeric values or food names.
 • Automatically resets daily calorie count at the start of a new day.
 • Command-line interface with clear progress display and user guidance.
 • User prompts for unknown foods to expand calorie database dynamically.

 Technologies/Tools Used:
  •	Python 3.x
	•	Standard libraries: os, datetime
	•	Local file handling for persistence ( calorie.txt )
  
  Steps to install & Run the program:
   .Download all the files in the same folder
   .Open terminal in that folder
   .Type “python main.py”
   .Now you can use it freely and all the data will be stored in the same folder

   Instruction for testing:
   •	Start the app and provide profile details when prompted.
	 •	Test calorie input by entering numeric values directly.
	 •	Test adding foods by name:
	 •	Add new food items and input their calorie values.
	 •	Select already saved foods for quick calorie addition.
	 •	Test quitting the app using ‘q’ and verify data saves correctly.
	 •	Run the app on a different day to confirm daily reset functionality.
	 •	Enter invalid or edge-case inputs to ensure input validation works properly.
   
