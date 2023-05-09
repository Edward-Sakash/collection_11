"""Task - Highscore
You have a list of participants as strings. This list holds title-cased names. Alongside there is a dictionary with scores, using the same names as keys with a integer as their value.

Implement a method get_score that takes a name as an argument, verifies it is in the list of participants and then prints the name with the score.

If the participant can't be found print a message telling that.

Input:
participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}

get_score('Paul')
get_score('Britney')
Output:
Paul did not participate
Britney scored 80 points"""

# Solution 1
def get_score(name):
    # Convert the name to lowercase to match the keys in the scores dictionary
    name_lower = name.lower()

    # Check if the name is in the list of participants
    if name_lower in [p.lower() for p in participants]:
        # If the name is in the list, print the name and score
        print(f"{name} scored {scores[name_lower]} points")
    else:
        # If the name is not in the list, print a message
        print(f"{name} did not participate")

participants = ['Brian', 'Britney', 'Ben']
scores = {
    'brian': 25,
    'britney': 80,
    'ben': 50
}

get_score('Paul')    # Output: Paul did not participate
get_score('Britney') # Output: Britney scored 80 points

print("_______________________________________________")

# Solution 2
def get_score(name):
    # Convert name to lowercase for case-insensitive lookup
    name_lower = name.lower()
    
    # Check if name is in participants list
    if name_lower not in scores:
        print(f"{name} did not participate")
    else:
        # Retrieve score for name and print it
        score = scores[name_lower]
        print(f"{name} scored {score} points")
        

participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}

get_score('Paul')
get_score('Britney')

print("_______________________________________________")

# Solution 3

def get_score(name):
    # Check if name is in participants list
    if name.title() not in participants:
        print(f"{name} did not participate")
    else:
        # Retrieve score for name and print it
        score = scores[name.lower()]
        print(f"{name} scored {score} points")
        
# Example usage
participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}

get_score('Paul')
get_score('Britney')
