from random import choice

def food_suggestion_bot_response(user_response):

  bot_response_chinese_1 = ["Taiwanese Solo Hotpot", "Fried Rice", "Noodle Soup", "Dumplings", "Hong Kong Cafe"]
  bot_response_chinese_2 = ["Juicy Shanghainese Dumplings", "Spicy Hotpot", "BBQ Skewers", "Sichuan Spicy Food", "Spicy Pickle Fish"]
  bot_response_chinese_3 = ["Seafood Hotpot", "Cantonese Banquet", "Peking Duck", "Cream Lobster with Noodles", "Chaozhou Late Night"]

  if int(user_response) >= 1 and int(user_response) <= 2:
    return "How about " + choice(bot_response_chinese_1) 
  elif int(user_response) >= 3 and int(user_response) <= 5:
    return "Delicious " + choice(bot_response_chinese_2)
  elif int(user_response) >= 6 and int(user_response) <= 10:
    return choice(bot_response_chinese_3) + " is always a party!"
  else:
    return "Might be too many people for one table"

print("Hello, I am the Chinese Food Suggeston Bot")
print("I randomly suggest Chinese food based on your party size.")
print("Please enter a numerical response.")
print("Type \"done\" to quit.")

user_response = ()

while True:
  user_response = input("How many people are hungry today? ")

  if user_response == 'done':
    break

  bot_response = food_suggestion_bot_response(user_response)
  print(bot_response)
