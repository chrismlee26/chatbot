Name: Chinese Food Suggestion Chatbot

This chatbot functions by taking a user inputed number of people that want to eat
and randomly suggesting suitable foods based on this party size

----------------------

First we import the random module, this activates the random choice function which we 
will use a bit later.

The string responses are inside three lists.

Next we use an if else equation to select from these lists based on the user input.
As these are taken as strings, we convert them into integers so we can use 
greater than, less than, equal to operators to keep these responses within the correct
range. 

If the user types in a number greater than 10, the bot mentions this is too many for a table.

Following this function, is a list of print commands which clarifies what the program's job
is and what inputs it takes. 

Next we start a while loop to iterate over the function. This writes to the empty variable
user_response through an input which asks how many people are hungry today. This will 
go on indefinitely as long as numbers are typed.


Then we add an if statement which breaks the function when 'done' is typed.

Last we create a variable bot_response: which operates the above with the parameter 
user_response.

Then we print this new variable to the console.
