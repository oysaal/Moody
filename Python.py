# create a dictionary to store mood data
mood_data = {}

# define the list of moods
mood_list = ["Happy", "Sad", "Neutral", "Anxious", "Angry", "Tired", "Depressed", "Emotional", "Sickly"]

# loop through each day of the month
for day in range(1, 31):
    # get user input for mood
    valid_mood = False
    while not valid_mood:
        mood = input("Enter your mood for day " + str(day) + " (" + ", ".join(mood_list) + "): ")
        if mood in mood_list:
            valid_mood = True
        else:
            print("Invalid mood. Please enter a valid mood.")

    # add mood data to dictionary
    mood_data[day] = mood

# count the number of each type of mood
mood_counts = {}
for mood in mood_list:
    mood_counts[mood] = 0

for mood in mood_data.values():
    mood_counts[mood] += 1

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
