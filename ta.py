import random
import sys1

counter = 0
bot_response_chinese = ["Taiwanese Hotpot", "Hong Kong Cafe", "Noodle Soup", "Sichuan Spicy Food", "BBQ Skewers", "Dumplings"]
bot_response_chinese_1= ["Shanghainese Dumplings", "sending good vibes", "Ok is fine"]

def conversation(counter, user_input, list1, list2):

    if counter == 0:
        print(random.choice(list1))
        counter += 1
    
    if counter == 1:
        print(random.choice(list2))

conversation(counter, sys.argv[1], bot_response_chinese, bot_response_chinese_1)