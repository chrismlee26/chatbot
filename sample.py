# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

#combine functions and conditionals to get a response from the bot
def get_mood_bot_response(user_response):

  #add some bot responses to this list
  bot_response_happy = ["omg! great!", "Keep smiling!", "I love to see you happy!"]
  bot_response_sad = ["im here for you", "sending good vibes", "Ok is fine"]

  if user_response == "happy":
    return choice(bot_response_happy)
  elif user_response == "sad":
    return choice(bot_response_sad)
  elif user_response == "ok":
    return choice(bot_response_sad)  
  else:
    return "I hope your day gets better"




print("Welcome to Mood Bot")
print("Please enter how you are feeling")

user_response = ""
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
  user_response = input("How are you feeling today?: ")
  
  # Quits program when user responds with 'done'
  if user_response == 'done':
    break

  
  bot_response = get_mood_bot_response(user_response)
  print(bot_response)










# Create a function called get_bot_response(). This function must:

# It should have 1 parameter called user_response, which is a string with the users input.

# It should return a string with the chat bot’s response.

# It should use at least 2 lists to store at least 3 unique responses to different user inputs. For example, if you were building a mood bot and the user entered “happy” for how they were feeling your happy response list could store something like “I’m glad to hear that!”, “Yay!”, “That is awesome!”.

# Use conditionals to decide which of the response lists to select from. For example: if a user entered “sad”, my program would choose a reponse from the of sad response list. If a user entered “happy”, my program would choose a reponse from the of happy response list.

# Use choice() to randomly select one of the three responses. (See example from class.)

# Greet the user using print() statements and explain what the chat bot topic is and what kind of responses it expects.

# Get user input using the input() function and pass that user input to the get_bot_response() function you will write

# Print out the chat bot’s response that is returned from the get_bot_response() function

# Use a while() loop to keep running your chat bot until the user enters "done".

