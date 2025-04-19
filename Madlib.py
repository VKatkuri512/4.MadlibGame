# Mad Libs Game 🎉

# Get user inputs
name = input("Enter a name: ")
action = input("Enter an action (verb): ")
cloth = input("Enter a piece of clothing: ")
food = input("Enter a type of food: ")
expression = input("Enter how they are looking (e.g., confused, happy): ")

# Create the story
story = """
One fine day, {name} decided to {action} in the middle of the street.
But here's the twist – {name} was wearing a {cloth}, munching on {food},
and looking extremely {expression} while doing it.
Everyone who saw it couldn’t stop laughing!
It was a moment to remember!
"""

# Print the story
print("\nHere is your Mad Libs story:\n")
print(story)
