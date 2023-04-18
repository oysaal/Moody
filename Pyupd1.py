import matplotlib.pyplot as plt


#___

import matplotlib.pyplot as plt

# create a dictionary to store mood and variable data
data = {}

# define the list of moods and variables
mood_list = ["Happy", "Sad", "Neutral", "Anxious", "Angry", "Tired", "Depressed", "Emotional", "Sickly"]
variable_list = ["Exercise", "Diet", "Stress"]

# loop through each day of the month
for day in range(1, 31):
    # get user input for mood and variables
    valid_mood = False
    valid_variables = False
    
    while not valid_mood:
        mood = input("Enter your mood for day " + str(day) + " (" + ", ".join(mood_list) + "): ")
        if mood in mood_list:
            valid_mood = True
        else:
            print("Invalid mood. Please enter a valid mood.")
    
    while not valid_variables:
        exercise = input("Enter the amount of exercise you did for day " + str(day) + ": ")
        diet = input("Enter your diet for day " + str(day) + ": ")
        stress = input("Enter your stress level for day " + str(day) + ": ")
        
        if exercise.isdigit() and diet.isalpha() and stress.isdigit():
            valid_variables = True
        else:
            print("Invalid input. Please enter valid values for exercise (as an integer), diet (as a string), and stress (as an integer).")

    # add mood and variable data to dictionary
    data[day] = {"mood": mood, "exercise": int(exercise), "diet": diet, "stress": int(stress)}

# count the number of each type of mood
mood_counts = {}
for mood in mood_list:
    mood_counts[mood] = 0

for mood in data.values():
    mood_counts[mood["mood"]] += 1

# calculate the percentage of each type of mood
total_count = sum(mood_counts.values())

mood_percentages = {}
for mood, count in mood_counts.items():
    mood_percentages[mood] = count / total_count * 100

# print out the results
print("Your mood for the month:")
for mood in mood_list:
    print(mood + ": " + str(mood_percentages[mood]) + "%")

# suggest ways to improve mood based on mood data
if mood_percentages["Depressed"] >= 50:
    print("You've been feeling depressed a lot this month. Here are some things you can try to improve your mood:")
    print("- Talk to a therapist or counselor")
    print("- Get regular exercise")
    print("- Practice self-care activities like taking a bath or reading a book")
elif mood_percentages["Happy"] >= 50:
    print("You've been feeling happy a lot this month. Keep up the good work!")
else:
    print("You've been feeling a mix of moods this month. Here are some things you can try to improve your mood:")
    print("- Identify triggers for negative moods and try to avoid them")
    print("- Incorporate relaxation techniques like deep breathing or meditation into your daily routine")
    print("- Get enough sleep and exercise regularly")

# plot bar chart of mood and variable data
fig, ax = plt.subplots(figsize=(10, 5))

mood_data = [mood_counts[mood] for mood in mood_list]
exercise_data = [data[day]["exercise"] for day in range(1, 31)]
diet


#_


import matplotlib.pyplot as plt

# create a dictionary to store mood and variable data
data = {}

# define the list of moods and variables
mood_list = ["Happy", "Sad", "Neutral", "Anxious", "Angry", "Tired", "Depressed", "Emotional", "Sickly"]
variable_list = ["Exercise", "Diet", "Stress"]

# loop through each day of the month
for day in range(1, 31):
    # get user input for mood and variables
    valid_mood = False
    valid_variables = False
    
    while not valid_mood:
        mood = input("Enter your mood for day " + str(day) + " (" + ", ".join(mood_list) + "): ")
        if mood in mood_list:
            valid_mood = True
        else:
            print("Invalid mood. Please enter a valid mood.")
    
    while not valid_variables:
        exercise = input("Enter the amount of exercise you did for day " + str(day) + ": ")
        diet = input("Enter your diet for day " + str(day) + ": ")
        stress = input("Enter your stress level for day " + str(day) + ": ")
        
        if exercise.isdigit() and diet.isalpha() and stress.isdigit():
            valid_variables = True
        else:
            print("Invalid input. Please enter valid values for exercise (as an integer), diet (as a string), and stress (as an integer).")
    
    # get user input for details about mood
    details = input("Enter any details about your mood for day " + str(day) + " (e.g., cause of mood, activities to improve mood): ")
    
    # add mood and variable data to dictionary
    data[day] = {"mood": mood, "exercise": int(exercise), "diet": diet, "stress": int(stress), "details": details}

# count the number of each type of mood
mood_counts = {}
for mood in mood_list:
    mood_counts[mood] = 0

for mood in data.values():
    mood_counts[mood["mood"]] += 1

# calculate the percentage of each type of mood
total_count = sum(mood_counts.values())

mood_percentages = {}
for mood, count in mood_counts.items():
    mood_percentages[mood] = count / total_count * 100

# print out the results
print("Your mood for the month:")
for mood in mood_list:
    print(mood + ": " + str(mood_percentages[mood]) + "%")

# suggest ways to improve mood based on mood data
if mood_percentages["Depressed"] >= 50:
    print("You've been feeling depressed a lot this month. Here are some things you can try to improve your mood:")
    print("- Talk to a therapist or counselor")
    print("- Get regular exercise")
    print("- Practice self-care activities like taking a bath or reading a book")
elif mood_percentages["Happy"] >= 50:
    print("You've been feeling happy a lot this month. Keep up the good work!")
else:
    print("You've been feeling a mix of moods this month. Here are some things you can try to improve your mood:")
    print("- Identify triggers for negative moods and try to avoid them")
    print("- Incorporate relaxation techniques like deep breathing or meditation into your daily routine")
    print("- Get enough sleep and exercise regularly")

# plot bar chart of mood and variable data
fig, ax =


#_

import sqlite3
import matplotlib.pyplot as plt

# create a connection to the database
conn = sqlite3.connect('mood_tracker.db')

# create a cursor object
c = conn.cursor()

# create a table to store mood data
c.execute('''CREATE TABLE IF NOT EXISTS mood_data
             (day INTEGER, mood TEXT, exercise INTEGER, diet TEXT, stress INTEGER, details TEXT)''')

# define the list of moods and variables
mood_list = ["Happy", "Sad", "Neutral", "Anxious", "Angry", "Tired", "Depressed", "Emotional", "Sickly"]
variable_list = ["Exercise", "Diet", "Stress"]

# loop through each day of the month
for day in range(1, 31):
    # get user input for mood and variables
    valid_mood = False
    valid_variables = False
    
    while not valid_mood:
        mood = input("Enter your mood for day " + str(day) + " (" + ", ".join(mood_list) + "): ")
        if mood in mood_list:
            valid_mood = True
        else:
            print("Invalid mood. Please enter a valid mood.")
    
    while not valid_variables:
        exercise = input("Enter the amount of exercise you did for day " + str(day) + ": ")
        diet = input("Enter your diet for day " + str(day) + ": ")
        stress = input("Enter your stress level for day " + str(day) + ": ")
        
        if exercise.isdigit() and diet.isalpha() and stress.isdigit():
            valid_variables = True
        else:
            print("Invalid input. Please enter valid values for exercise (as an integer), diet (as a string), and stress (as an integer).")
    
    # get user input for details about mood
    details = input("Enter any details about your mood for day " + str(day) + " (e.g., cause of mood, activities to improve mood): ")
    
    # insert mood and variable data into table
    c.execute("INSERT INTO mood_data (day, mood, exercise, diet, stress, details) VALUES (?, ?, ?, ?, ?, ?)", (day, mood, exercise, diet, stress, details))

# commit changes to database
conn.commit()

# close connection to database
conn.close()

# retrieve mood data from database
conn = sqlite3.connect('mood_tracker.db')
c = conn.cursor()
c.execute("SELECT * FROM mood_data")
rows = c.fetchall()

# create dictionary to store mood and variable data
data = {}

# loop through each row of data and add to dictionary
for row in rows:
    data[row[0]] = {"mood": row[1], "exercise": row[2], "diet": row[3], "stress": row[4], "details": row[5]}

# count the number of each type of mood
mood_counts = {}
for mood in mood_list:
    mood_counts[mood] = 0

for mood in data.values():
    mood_counts[mood["mood"]] += 1

# calculate the percentage of each type of mood
total_count = sum(mood_counts.values())

mood_percentages = {}
for mood, count in mood_counts.items():
    mood_percentages[mood] = count / total_count * 100

# print out the results
print("Your mood for the month:")
for mood in mood_list:
    print(mood + ": " + str(mood_percentages[mood]) +

#_

