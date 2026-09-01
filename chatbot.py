import random 
import pyjokes
import requests 
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

greetings = [ "Hey! How can I help you today?",  "Hi there! What can I do for you?", "Nice to meet you! What's up!" , " Hello" ]
goodbye = [ "Goodbye" , "Nice meeting you, goodbye", "bye there" ] 
weather = [ "I'm not connected to a weather service yet, so I can't give you a real forecast." , "I can't check live weather yet, but you can look outside!" , "I don't have access to live weather data yet, but I hope it's nice outside!" ]
help = [ "Sure Buddy! I'm here to help. You can ask me about the weather, request a fun fact, or just say hello!" , "I am here to help, tell me what do you need ", "SOS " ] 
facts = [ " The dot over the lowercase letter i or j is called a tittle. " , " Bananas are botanically classified as berries, but strawberries are not." ,  "Wombat feces are cube-shaped, which keeps the droppings from rolling away." , "Honey never spoils, and edible 3,000-year-old honey has been found in Egyptian tombs." , "Sloths can hold their breath longer than dolphins, lasting up to 40 minutes underwater." ] 


name = input(" Bot: What's your name? \n You:" )
print(" Nice to meet you" , name ,"!!!")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return f"The weather in {city} is {temperature}°C with {description}."

    elif response.status_code == 404:
        return "I couldn't find that city. Please check the spelling."

    else:
        return "Sorry, I couldn't get the weather right now."
        
while True: 
    user_input = input( "You :" )
    user_input = user_input.lower().strip()

    if user_input == "":
        print("Bot: Please type something so I can respond!")
        continue

    elif "hello" in user_input or "hi" in user_input:
        print("Bot:", random.choice(greetings) , name )

    elif "weather" in user_input or "forecast" in user_input:
    city = input("Bot: What city are you in?\nYou: ")
        if city == "":
            print("Bot: Please enter a city.")
            continue

    print("Bot:", get_weather(city), name) 
   

    elif "help" in user_input or "sos" in user_input:
        print("Bot:", random.choice(help), name)

    elif "fact" in user_input: 
        print("Bot:", random.choice(facts), name )
    
    elif "bye" in user_input or "goodbye" in user_input:
        print("Bot:", random.choice(goodbye) , name )
        break 


    elif "joke" in user_input:
        print("Bot:", pyjokes.get_joke())
        
    else:
        print( "Bot: I don't understand. Try asking for HELP SOS " , name )



