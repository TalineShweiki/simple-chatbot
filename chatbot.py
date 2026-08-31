import random 
greetings = [ "Hey! How can I help you today?",  "Hi there! What can I do for you?", "Nice to meet you! What's up!" , " Hello" ]

Goodbye = [ "Goodbye" , "Nice meeting you, goodbye", "bye there" ] 
Weather = [ "weather" , "forecast" ]
Help = [ "Help" , "Please suuport ", "SOS " ] 

Random Fact = [ "The dot over the lowercase letter "i" or "j" is called a tittle." , "Bananas are botanically classified as berries, but strawberries are not.", "Wombat feces are cube-shaped, which keeps the droppings from rolling away." , "Honey never spoils, and edible 3,000-year-old honey has been found in Egyptian tombs." , "Sloths can hold their breath longer than dolphins, lasting up to 40 minutes underwater." ] 

random.choice(greetings)
user_input = input( "You :" )
user_input = user_input.lower()

if "hello" in user_input or "hi" in user_input:
    print("Bot:", random.choice(greetings))



