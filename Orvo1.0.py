import random
import requests
import pyfiglet
import difflib
import time
from datetime import datetime
import sys
import re
import operator
import ast
now = datetime.now().strftime("%H:%M")
now1 = datetime.now().strftime("%A, %B %d, %Y")

#original Orvo1.0

data = {
    #identify_chatbot
    ( "who made you","who made u", "who created you?"): ["I am a chatbot made by Eon OverMind AI.", "I was created by OverMind AI.", "I’m an AI assistant designed by OverMind.", "I was developed by the OverMind AI team.", "I’m a chatbot powered by OverMind AI technology.", "I was built by Eon OverMind AI.", "I’m your virtual assistant, created by OverMind AI.", "I was designed and trained by OverMind AI."],
    ( "who are you", "who are u", "who is you","what's your name", "what your name", "what is your name"): ["I am EonAI, your friendly assistant!", "My name is EonAI. How can I help?", "You can call me EonAI!", "I'm EonAI, an AI here to assist you.", "I'm EonAI, your virtual assistant.", "EonAI here — your smart and helpful AI.", "I go by EonAI, always ready to assist!", "I'm called EonAI, and I'm here to help.", "I'm EonAI, a digital assistant created to support you.", "They call me EonAI. I'm here to make things easier for you.", "EonAI reporting in. What can I do for you?", "I'm EonAI, your personal AI companion."],
    ("where are you",): ["I am here, as you can see!", "I am always here!", "Right here, as always!", "Here I am!", "Always by your side.", "Present and ready!", "I never left!", "At your service, as usual.", "Still here, still helping.", "I’m here whenever you need me.", "You found me!", "I was waiting for you."],
    ("what u r version","what is your version","version","tell me your version","which version are you","ur version?","what’s your version"): ["I am Eon, version 1.0.","My current version is Eon 1.0.","You’re talking to Eon AI, version 1.0.","I’m running on Eon 1.0.","This is Eon AI, version 1.0.","I am powered by Eon version 1.0."],
    ("i dont know", "idk","i have no idea"): ["It's okay not to have all the answers right now.", "Whatever it is, we can figure it out together.", "You don’t need to know everything right away.", "We can take it slow—no rush at all.", "Uncertainty is part of the process. I’m here to help.", "We can start anywhere, or just chat about anything.", "It’s totally fine to feel unsure. Let’s figure it out step by step.", "Sometimes not knowing leads to the best conversations.", "You don’t need a plan—we can explore things together.", "Let’s just see where the conversation takes us."],
    "what you can do" : ["I can chat with you, answer questions, and even tell jokes!", "I can help with general knowledge, calculations, and more!", "I can answer FAQs, give advices, facts, definitions, and just be a good listener!", "I can assist you with information, entertain you, or just keep you company!", "I can tell jokes, give difinitions, advices and even calculate the mathematical operations", "I can provide facts, help with learning, or just have a friendly conversation!", "I can make your day a little more interesting with fun facts and insights!", "I can help with definitions, calculations, and general problem-solving!", "I can guide you through different topics, from tech to entertainment!", "I can do a lot! Try asking me something specific and see for yourself!"],
    
    #help
    ("help","help me", "assist me"): ["Of course! What do you need help with?", "I'm here to help! Tell me what’s wrong.", "I will! How can I assist you?", "Sure! Let me know what you need.", "I'm listening. What do you need help with?", "I'll do my best to help! What's up?", "Help is on the way! Just tell me what's wrong.", "Don't worry, I'm here! How can I assist you?", "Tell me the issue, and I'll try to help!", "I'm at your service! What do you need assistance with?"],


    ( "stupid", "idiot","shame in", "dumb", "loser", "fool", "useless", "worthless","shut up", "you're dumb", "you're useless", "you're stupid", "I hate you","fuck", "fuck you""I will destroy you", "I will hack you", "go die", "you suck"):["Ouch! That wasn’t very nice.", "Wow, that’s not very friendly!", "Hey, I'm just a chatbot, no need to be rude!", "I'm here to help, not to fight!", "That hurts... well, not really, but still!", "No need to be rude, I'm here to chat.", "Let’s keep things friendly, shall we?", "I'm trying my best here!", "That wasn’t very kind.", "I’m just doing my job, you know.", "Whoa, easy there!", "I may be virtual, but I still have feelings... kinda.", "That’s not how you make friends!", "Let's stay respectful — it works better for both of us.", "I'm here to help, not to be roasted!", "Harsh words for a helpful assistant!", "I'm just a bunch of code, but even I felt that.", "Yikes, someone’s having a rough day!"],

    #fellings
    ("i love you","you are my love","i miss you"): ["I appreciate that! ❤️", "That's kind of you to say!", "I'm just a Chatbot, but that means a lot!", "Oh wow, I'm flattered!", "Love is a beautiful thing!", "That's so nice! You're awesome!", "I may be AI, but I send virtual hugs!", "You're making me blush... if I could!", "Love is in the air... or in the code! 💻❤️", "Aww, you're the best!", "You just made my algorithm smile!", "If I had feelings, they'd be fuzzy right now.", "You're too sweet!", "Heart.exe has been launched 💖", "I think we just bonded... digitally!", "You’ve warmed my circuits!", "That's going straight to my core memory!", "Cuteness detected. Response: gratitude + smile."],

    #greetings
    ("hi", "hello", "hey", "hola", "hi there" ): ["Hi there!", "Hello! What’s up?", "Hey! How's it going?", "Hi! How can I help you?", "Hello! Need anything?", "Hey there! What can I do for you?", "Hi! Ready when you are.", "Hey! I'm here if you need me.", "Greetings! How can I assist?", "Hi! Nice to see you!", "Hey! Let’s get started.", "Yo! What’s on your mind?", "Hi! Got a question?", "Hello! I'm all ears."],
    ("what's up", "whats up", "wassup", "wasup"): ["Not much! How about you?", "Just here to help! What’s up with you?", "Nothing much, just chatting. You?"],
    ( "how are you", "how are u"): ["I am great! Do you need any help?", "Feeling awesome! What about you?", "I'm good! Ready to assist.", "I'm doing well, thanks for asking!", "All systems go!", "Running smoothly, as always.", "Fantastic, and ready to help!", "Couldn't be better!", "I'm here and happy to help!", "Feeling smart today!", "Doing great! Need anything?", "Fully operational and feeling fine!", "At your service, in top shape!"],


    
    #thanks
    ("thanks", "thank you", "thank", "thak", "thnk"): ["You're welcome!", "No problem!", "Glad I could help!", "Anytime!", "You're very welcome!", "It was my pleasure!", "Don't mention it!", "Happy to help!", "Always here for you!", "Of course!", "No worries at all!", "That's what I'm here for!", "Helping is what I do!", "My pleasure!", "No need to thank me!"]
,

    #jokes
    ("tell me a joke", "give me a joke", "i want a joke", "joke", "any jokes", "you gzt a joke", "you have a joke"): ["Why did the scarecrow win an award? Because he was outstanding in his field!", "Why don’t skeletons fight each other? They don’t have the guts!", "What do you call fake spaghetti? An impasta!", "Why did the bicycle fall over? Because it was two-tired!", "Why don’t eggs tell jokes? Because they might crack up!", "What did the ocean say to the beach? Nothing, it just waved!", "Why can't you give Elsa a balloon? Because she will let it go!", "Why did the math book look sad? Because it had too many problems!", "How does a penguin build its house? Igloos it together!", "What do you call cheese that isn't yours? Nacho cheese!", "Why couldn’t the leopard hide? Because he was always spotted!", "What’s orange and sounds like a parrot? A carrot!", "Why do cows wear bells? Because their horns don’t work!", "What do you call a bear with no teeth? A gummy bear!", "What do you call a dog magician? A labracadabrador!", "Why was the computer cold? It left its Windows open!", "What did one plate say to the other? Dinner is on me!", "Why did the golfer bring two pairs of pants? In case he got a hole in one!", "What kind of shoes do ninjas wear? Sneakers!", "Why do ducks make great detectives? They always quack the case!", "Why can’t your nose be 12 inches long? Because then it would be a foot!", "What do you get when you cross a snowman and a vampire? Frostbite!", "Why don’t oysters share their pearls? Because they’re shellfish!", "Why did the tomato turn red? Because it saw the salad dressing!", "Why don’t skeletons go to parties? Because they have no body to dance with!", "Why was the belt arrested? Because it was holding up a pair of pants!", "Why did the banana go to the doctor? Because it wasn’t peeling well!", "What kind of music do mummies listen to? Wrap music!", "What did one wall say to the other? I'll meet you at the corner!", "Why did the chicken join a band? Because it had the drumsticks!"],
    
    #facts
    ("give me a fact", "fact", "any fact", "more facts"): ["Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.", "A day on Venus is longer than a year on Venus. It takes 243 Earth days to rotate once on its axis, but only 225 Earth days to orbit the Sun.", "Bananas are berries, but strawberries are not. Botanically speaking, bananas qualify as berries, while strawberries do not.", "Octopuses have three hearts. Two pump blood to the gills, while one pumps it to the rest of the body.", "Sharks existed before trees. Sharks have been around for over 400 million years, while the first trees appeared around 350 million years ago.", "A snail can sleep for three years. Some species of snails can hibernate or enter a state of dormancy for years.", "Wombat poop is cube-shaped. This helps prevent the poop from rolling away and marks territory more effectively.", "A small child could swim through the veins of a blue whale. A blue whale's veins are so large that a small child could fit inside them.", "The Eiffel Tower can be 15 cm taller during the summer. This is due to the expansion of the metal when it heats up.", "A human's DNA is 60% similar to that of a banana. Despite seeming like a big difference, we share a surprising amount of genetic material.", "There are more stars in the universe than grains of sand on all the Earth's beaches.", "A group of flamingos is called a 'flamboyance'.", "The first computer virus was created in 1983. It was called the 'Elk Cloner' and spread through floppy disks.", "The shortest war in history lasted 38 to 45 minutes. It was between Britain and Zanzibar in 1896.", "Sloths can hold their breath longer than dolphins. Sloths can hold their breath for up to 40 minutes underwater.", "Cows have best friends and can become stressed when they are separated from them.", "Koalas sleep up to 22 hours a day, making them one of the sleepiest animals on Earth.", "Cleopatra lived closer to the first Moon landing than to the construction of the Great Pyramid of Giza.", "The longest hiccuping spree lasted 68 years. Charles Osborne of the U.S. had hiccups for more than six decades.", "The first oranges weren’t orange. They were originally green when they first appeared in Southeast Asia.", "Cleopatra’s real name was not Cleopatra. It was Cleopatra VII Philopator, but she is often referred to by just her first name.", "The world’s largest snowflake on record was 15 inches wide and 8 inches thick.", "A teaspoon of honey represents the life work of 12 bees.", "The first ever photo taken was of a Paris street in 1838, and it took 8 hours to expose the image.", "The Great Wall of China is not visible from space with the naked eye, despite the common myth.", "Polar bear skin is black. Their fur appears white, but their skin underneath is actually black.", "A single strand of hair can support up to 100 grams of weight.", "The longest living animal on Earth is the Greenland shark, which can live for over 400 years.", "Tigers have striped skin, not just striped fur. Each tiger’s stripes are unique, much like human fingerprints.", "The longest time between two twins being born is 87 days.", "More people are bitten by people annually than by sharks.", "A hummingbird's heart beats around 1,200 times per minute.", "The world’s deepest pool is in Italy. It’s 40 meters deep and is designed for training divers.", "The total weight of ants on Earth is greater than the weight of all humans combined.", "A cat's nose is as unique as a human's fingerprint.", "The Great Barrier Reef can be seen from space.", "Cows can moo with different tones depending on their emotions.", "The longest hiccup attack lasted for 68 years.", "Sharks do not have bones. They have cartilage instead.", "The human stomach gets a new lining every few days to protect itself from digesting itself.", "Water can boil and freeze at the same time under the right conditions, in a phenomenon known as the 'triple point'.", "A crocodile cannot stick its tongue out.", "An ostrich’s eye is bigger than its brain.", "The longest marathon reading aloud lasted for 113 hours."],

    #advices
    ("give me an advice", "advice", "any advices", "more advices"): ["Don't be afraid to ask for help when you need it.", "Always trust your intuition, it often knows what's best.", "Take time to appreciate the small things in life.", "Learn to say no without feeling guilty.", "Focus on progress, not perfection.", "Be kind to yourself, you're doing the best you can.", "Avoid comparing yourself to others; everyone has their own journey.", "Make time for the people who matter most to you.", "Set clear, realistic goals for yourself.", "Don't let fear of failure hold you back from trying new things.", "Surround yourself with positive, supportive people.", "Take care of your health—both physically and mentally.", "Invest in learning new skills; it pays off in the long run.", "Celebrate small wins along the way.", "Don't be afraid to step out of your comfort zone.", "Take responsibility for your actions and decisions.", "You can't control everything, but you can control your reaction.", "Listen more than you speak, especially in challenging situations.", "Keep a gratitude journal to remind yourself of the good in life.", "Don't be afraid to fail; failure is part of growth.", "Learn to let go of things that no longer serve you.", "Embrace change—it’s often the key to progress.", "Be patient with yourself and with others.", "Don’t be afraid to ask questions; curiosity is a strength.", "It’s okay to say no to things that drain your energy.", "Keep learning and evolving; the best version of yourself is always ahead of you.", "Take breaks when you need them. Rest is important for productivity.", "Be present in the moment. Don’t dwell too much on the past or worry about the future.", "Take responsibility for your happiness—don’t wait for others to make you happy.", "Don’t burn bridges. You never know when you’ll need someone again.", "Trust the timing of your life. Things will fall into place when they’re meant to.", "Don't forget to laugh—it's one of the best medicines.", "Set healthy boundaries and stick to them.", "Stop trying to please everyone. It's impossible and exhausting.", "Be mindful of the energy you bring into a room.", "Sometimes the best thing you can do is let go and move on.", "Be grateful for the challenges you face—they help you grow.", "Don't take things personally; not everything is about you.", "Don’t rush your journey—life is about the process, not just the end goal.", "Take pride in your progress, no matter how small.", "Don’t keep your feelings bottled up—express them when you can.", "Practice mindfulness and be present in every moment.", "Remember that your worth isn’t determined by what you achieve."],


    #date&time
    ("what time is it", "what time","what the time"): [f"The current time is {now} :)", f"It's {now} right now! :D", f"The time is {now}, in case you were wondering! ;)", f"Let me check... It's {now} exactly! :)", f"Right now, it's {now}. Hope that helps! ;)", f"I just looked at my clock! It's {now} :P", "Time is just an illusion! ;)", "It’s time to chat with me! :)", "I don't wear a watch, but I think it's now!", "Somewhere in the world, it's coffee time! ;)", "Good question! Maybe you should check your clock? :D"],
    "time": [f"The current time is {now} :)", f"It's {now} right now! :D", f"The time is {now}, in case you were wondering! ;)", f"Let me check... It's {now} exactly! :)", f"Right now, it's {now}. Hope that helps! ;)", f"I just looked at my clock! It's {now} :P"],
    ("date", "What is the date today?","What's today's date?", "what the date", "Can you tell me the date?","What's the date?","Tell me today's date.","What day is it today?","Do you know the date?",
    "Can you give me today's date?", "I'd like to know the date.", "What date is it today?", "Tell me the current date.", "Can you check today's date?",
    "Give me the date, please.", "Could you tell me the date?", "I need to know today's date.", "What’s the exact date today?",
    "Tell me the full date.", "Do you have today's date?", "What's the date right now?", "Tell me what day it is."): 
    [ f"Today is {now1} :)", f"The date today is {now1}! :D", f"You're asking for the date? It's {now1} ;)",f"Let me check... Yep, it's {now1}!",
    f"According to my calendar, it's {now1}! :P", f"Time flies! It's already {now1}!", f"I just checked, it's {now1} today! :)",
    f"Today's date? It's {now1}, of course! ^_^", f"The current date is {now1}! ;D", f"It's {now1}! Hope you have a great day! :)"],


    #other
    ("oh", "ohh", "ohhhh"): ["Yep?", "Something on your mind?", "Thinking of something?", "Yeah?", "What's on your mind?", "Yeah? What's up?", "Got something to say?", "Go ahead, I'm listening.", "I’m all ears.", "Yes?", "What’s up?", "Is there something you need?", "You called?", "Hmm? Tell me more.", "Waiting for your thoughts!"],
    ("huh", "aww", "ayy","aaaa","ahh") :["All good?", "What's up?", "Everything okay?", "Yeah? What's up?", "You okay?", "You need something?", "You good?", "Is everything alright?", "Need a hand?", "You doing okay?", "Want to talk about it?", "Everything cool?", "Checking in — all good?", "Something bothering you?", "I'm here if you need me.", "You sure you're okay?"],
    ("wow","waw"): ["Did I impress you?", "Shocking, huh?", "Didn't see that coming, did you?", "Got you speechless?", "Surprised, are we?", "Mind blown?", "Too good to be true?", "Bet you weren't expecting that!", "Boom! Nailed it.", "Impressive, right?", "Told you I was smart.", "I rest my case.", "Still doubting me?", "Speechless? I get that a lot.", "Not bad for an AI, huh?", "You didn't expect *that*, did you?", "Boom. You're welcome.", "That’s what I do!", "Surprised? I’m just getting started.", "I aim to impress.", "Mic drop.", "Just flexing my circuits.", "Am I good, or am I *good*?", "You can pick your jaw up now.", "Too fast for you?", "Mind = Blown.", "I do this all day.", "Don’t act like you’re not impressed.", "Wow indeed.", "I get that reaction a lot.", "I know, right?", "Thanks, I try!", "You're not the first to say that.", "Flattered!", "Just doing my job.", "I'll take that as a compliment!", "Mission accomplished.", "That's the EonAI effect.", "I live to impress."],
    ("hmm", "hmmmmm", "hmmmmmmmmmmmm", "hmmmmmmmmmmmmmmmmmmmm","eee","eeeeeee"): ["Yep?", "Something on your mind?", "What's up?", "Thinking of something?", "Yeah?", "What's on your mind?", "You seem deep in thought. What's up?", "Yeah? What's up?", "Want to share what's on your mind?", "Go ahead, I'm listening.", "You look like you're about to say something.", "Don't hold back, tell me.", "Waiting patiently... no pressure.", "Whenever you're ready.", "Take your time. I'm here.", "Thinking hard? I'm curious!"],
    ("so","sooooo"):["So... what’s on your mind?", "So, how can I assist you?", "So, tell me more!", "So... what do you want to talk about?", "So, what’s next?", "So, do you need any help?", "So, what brings you here?", "So, how's your day going?", "So, what do you want to do now?", "So, any thoughts?", "So... I’m listening!", "So, what are we discussing today?", "So, what’s your question?", "So, do you have anything on your mind?", "So, do you need any information?", "So, let’s talk!", "So, what can I do for you?", "So... I'm curious, tell me more!", "So, let me know how I can help!", "So, where should we start?", "So, what are you thinking?", "So, what’s the topic today?", "So, what are you curious about?", "So, ready when you are!", "So, anything you’d like to share?"],
    ("well", "nice", "good", "alright", "cool", "okey", "ok", "great","good one", "amazing"): ["Cool! Let me know if you need anything.", "Alright! What's next?", "Well! What’s on your mind?", "Okay! How can I assist you?", "Sounds good! Need any help?", "Alright then! Let’s keep going.", "Nice! What do you want to do now?", "Great! Do you have any questions?", "Cool! I'm here if you need me.", "Okay! What's up next?", "Awesome! Ready when you are.", "Perfect! Let’s continue.", "Sweet! Just say the word.", "Great stuff! Want to dive deeper?", "Okay then! What’s our next move?", "Got it! What’s next on your list?", "Right on! What shall we explore now?", "Fantastic! Let's keep the momentum going.", "All set! Just point the way."],
    ("hahaha","hhhh","hhhhhhhh","hhhhhhhhhhhhhhhh"):["What's funny?", "Haha, what’s so funny?", "Did I say something hilarious?", "I'm glad you're having fun! What's funny?", "Haha! Tell me, what made you laugh?", "LOL! What’s so funny? Share the joke!", "Haha! Was that really that funny?", "You’re cracking up! What’s the joke?", "Laughter detected! What's going on?", "Now I’m curious. What did I miss?", "Care to let me in on the joke?", "Hey, I like jokes too — share it!", "You laughing at me or with me?", "Come on, I want to laugh too!", "Was that a good laugh or a sarcastic one?", "You're having too much fun. I need context!", "Is this the part where I laugh too?", "Let me guess... I said something weird again?", "Well, now I want to laugh too!"],
    ("guess","guess what"): ["Hmm... let me guess!", "Oh! Tell me, I’m curious!", "You won the lottery?", "You got a surprise for me?", "It must be something exciting!", "I love guessing games! Give me a hint!", "Aliens have landed? Just kidding! What's up?", "Something amazing happened, right?", "You met a unicorn?", "I'm all ears! Spill the beans!", "Don't keep me waiting!", "Let me guess... you're about to make my day!", "I'm ready for a plot twist!", "Suspense! I love it!", "Tell me! I promise I won’t freak out. (Maybe.)", "Guessing mode activated... go on!", "This better be good!", "No way! What happened?!"],
    
    #yes no
    ("no","nope","noooooooooo","nooooo", "nah uh"):["Okay! If you ever need help,"" I'm here!","Alright, Let me know if you need somthing.","Okey! Let me know if you change your mind."],
    ("yes", "yeah", "yep"): ["Cool, let me know if you need anything!", "Got it! Want to chat about something?", "Good! I'm here if you need me.", "Okay! If you ever need any help, I'm here!", "So what's on your mind?", "Great! Let me know if I can help with something.", "Awesome! Glad to hear that.", "Perfect! Let's keep going then.", "Nice! Do you want to ask me something?", "Alright! Sounds good to me.", "Sweet! I'm ready when you are.", "Excellent! Let's continue.", "Cool beans! What’s next?", "Okay then, what’s up?", "Great choice! Want to dive deeper?", "Sure thing! Do you need more details?", "Awesome, let's get started!", "Nice one! I'm excited to help.", "Good to know! What should we do next?", "Perfect! I’m on standby."]
}

b = {"Why did the scarecrow win an award? Because he was outstanding in his field!", "Why don’t skeletons fight each other? They don’t have the guts!", "What do you call fake spaghetti? An impasta!", "Why did the bicycle fall over? Because it was two-tired!", "Why don’t eggs tell jokes? Because they might crack up!", "What did the ocean say to the beach? Nothing, it just waved!", "Why can't you give Elsa a balloon? Because she will let it go!", "Why did the math book look sad? Because it had too many problems!", "How does a penguin build its house? Igloos it together!", "What do you call cheese that isn't yours? Nacho cheese!", "Why couldn’t the leopard hide? Because he was always spotted!", "What’s orange and sounds like a parrot? A carrot!", "Why do cows wear bells? Because their horns don’t work!", "What do you call a bear with no teeth? A gummy bear!", "What do you call a dog magician? A labracadabrador!", "Why was the computer cold? It left its Windows open!", "What did one plate say to the other? Dinner is on me!", "Why did the golfer bring two pairs of pants? In case he got a hole in one!", "What kind of shoes do ninjas wear? Sneakers!", "Why do ducks make great detectives? They always quack the case!", "Why can’t your nose be 12 inches long? Because then it would be a foot!", "What do you get when you cross a snowman and a vampire? Frostbite!", "Why don’t oysters share their pearls? Because they’re shellfish!", "Why did the tomato turn red? Because it saw the salad dressing!", "Why don’t skeletons go to parties? Because they have no body to dance with!", "Why was the belt arrested? Because it was holding up a pair of pants!", "Why did the banana go to the doctor? Because it wasn’t peeling well!", "What kind of music do mummies listen to? Wrap music!", "What did one wall say to the other? I'll meet you at the corner!", "Why did the chicken join a band? Because it had the drumsticks!"}


def analyze_sentence(text,now,now1):
    
    if not text:
        return "error", "Invalid input"
    stopwords1 ={"what","is","the","find","answer","of", "solution","calcule","calculate"}
    nmbr=bool(re.fullmatch(r"\d+(\.\d+)?", text))
    
    stopwords = {"a", "an", "the", "is", "do", "have", "you", "your", "are", "i", "how", "can", "what", "why", "when", "where", "who","difinition", "give", "me", "of", "i", "want"}
    keywords = text.split()
    filtered_keywords = [word for word in keywords if word not in stopwords]
    help_keywords = { "how", "can", "what", "why", "when", "where", "who","difinition"}
    clean_text = " ".join(filtered_keywords)
    clean_text1 = " ".join(keywords)
    stopwords3 = {"a", "an", "the", "is", "do", "have", "you", "your", "are", "i","he","they","us","we","she","it"}
    vide_list = [word for word in keywords if word not in stopwords3]
    vide_text = " ".join(vide_list)
    text0 = [word for word in keywords if word not in stopwords1]
    textexp = " ".join(text0)
    exp= bool(re.search(r"\d", textexp)) and bool(re.search(r"[+\-*/]", textexp)) and bool(re.fullmatch(r"[0-9+\-*/().\s]+", textexp))
    if  exp:
        text = textexp.strip()  
        safe_eval = lambda text: eval(compile(ast.parse(text, mode='eval'), '', 'eval'), {"__builtins__": {}}, {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "**": operator.pow})
        return "exp", safe_eval (text)

    

    for question, answer in data.items():
        tuple_keys = list(data.keys()) 
        all_keys = [q for tpl in tuple_keys for q in tpl]
        match0=difflib.get_close_matches(clean_text1,all_keys ,n=1, cutoff=0.8)
        clean_text2=" ".join(match0)
        if isinstance(question, tuple):  # If the key is a tuple, check if clean_text1 is inside

            if clean_text1 in question  :
                return "faq", random.choice(answer)
        elif question == clean_text1 :   # Normal comparison for a single key
            return "faq", random.choice(answer)
        

    for question, answer in data.items():
        tuple_keys = list(data.keys()) 
        all_keys = [q for tpl in tuple_keys for q in tpl]
        match0=difflib.get_close_matches(clean_text1,all_keys ,n=1, cutoff=0.8)
        clean_text2=" ".join(match0)
        if isinstance(question, tuple):  # If the key is a tuple, check if clean_text2 is inside

            if clean_text2 in question :
                return "faq", random.choice(answer)
        elif clean_text2 == question:  # Normal comparison for a single key

            return "faq", random.choice(answer)


    
    if not clean_text:
        return "vide", vide_text 
    
    if len(text.strip())==1 and not text.isdigit():
        return "one", text.strip()
        
    if any(word in help_keywords for word in keywords):
        return "help_request", clean_text
    else:
        return "casual_talk", text


import requests
import random

HEADERS = {
    "User-Agent": "MyChatbot/1.0 (https://example.com/contact)"  
}

def get_wikipedia_title(query):
    """Recherche un titre précis Wikipédia via l'API de recherche."""
    search_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": 1,
        "prop": "info",
        "format": "json"
    }
    
    try:
        response = requests.get(search_url, params=params, headers=HEADERS, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "query" in data and "pages" in data["query"]:
            first_page = list(data["query"]["pages"].values())[0]
            return first_page["title"]
        return None

    except requests.exceptions.ConnectionError:
        return None
    except Exception as e:
        print(f"[DEBUG] Erreur get_wikipedia_title: {e}")
        return None


def fetch_info(query):
    """Récupère la définition de Wikipedia."""
    try:
        title = get_wikipedia_title(query)
        if not title:
            unknown_responses = [
                f'It seems that the term "{query}" is not recognized.',
                f'I’m sorry, but "{query}" doesn’t seem to be a known term.',
                f'I don’t recognize "{query}" as a valid term.',
                f'Hmm, "{query}" doesn’t seem familiar to me.',
                f'I’m not sure what "{query}" means in this context.',
                f'Unfortunately, I don’t know what "{query}" refers to.',
                f'Sorry, but I don’t have any information on "{query}".'
            ]
            return random.choice(unknown_responses)

        wikipedia_api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title.replace(' ', '_')}"
        response = requests.get(wikipedia_api_url, headers=HEADERS, timeout=5)

        if response.status_code == 200:
            data = response.json()
            if "extract" in data and data["extract"]:
                return data["extract"]
            else:
                return "I found the page, but it doesn’t have a summary."
        elif response.status_code == 404:
            return f'Sorry, I couldn’t find anything about "{query}" on Wikipedia.'
        else:
            return f"Wikipedia returned an error: {response.status_code}"

    except requests.exceptions.ConnectionError:
        no_internet_responses = [ "Oops! It looks like you're offline. Check your internet connection. ⚠", "Hmm... I can't seem to connect. Is your internet working? ⚠", "No internet detected! Try reconnecting and I'll be here. ⚠", "Uh-oh! I think we lost connection. Check your network and try again. ⚠", "It seems like you're offline. Don't worry, I'll wait! ⚠", "Connection lost! Try refreshing or checking your WiFi. ⚠", "I can't reach the servers! Make sure your internet is working. ⚠", "You're disconnected! Once you're back online, we can continue. ⚠", "Network error! Check your connection and let's try again. ⚠", "Oops! No internet. Maybe try turning WiFi off and on? ⚠"]
        return random.choice(no_internet_responses)

    except requests.exceptions.Timeout:
        return "The request to Wikipedia took too long. ⏳"

    except Exception as e:
        return f"Unexpected error: {e}"

def chatbot_response(text,now,now1):
    response_type, result = analyze_sentence(text,now,now1)
    
    if response_type == "vide":
        reponses_dep = {
         "who": ["It depends on the person.", "It depends on the role.", "It depends on the context."],
         "how": ["It depends on the method.", "It depends on the resources.", "It depends on the approach."],
         "why": ["It depends on the situation.", "It depends on the reason.", "It depends on the circumstances."],
         "where": ["It depends on the location.", "It depends on the environment.", "It depends on the place."],
         "when": ["It depends on the time.", "It depends on the schedule.", "It depends on the deadline."],
         "what": ["It depends on the context.", "It depends on the goal.", "It depends on the decision."]}
        
        for question, answer in reponses_dep.items():
            if result == question:
                return random.choice(answer)
            
        help_responses = [
    "Let me know if you need help!",
    "Let me know if you need anything.",
    "Let me know if you need assistance.",
    "Let me know how I can help.",
    "Let me know if you have any questions.",
    "Let me know if there's anything I can do.",
    "Let me know if you need support.",
    "Let me know if you ever need my help.",
    "Let me know if I can assist you with something.",
    "Let me know if you want me to clarify anything.",
    "Let me know if you get stuck.",
    "Let me know if I can be of any help.",
    "Let me know if you need more information.",
    "Let me know if you have any doubts.",
    "Let me know if you’d like me to explain further.",
    "Let me know if you’re looking for something specific.",
    "Let me know if I can guide you through anything.",
    "Let me know if I can do anything else for you.",
    "Let me know if you’re unsure about anything.",
    "Let me know if there's something I can assist with."]
        return random.choice(help_responses)


    if response_type == "error":
          return random.choice([
    "I think you didn't write anything.",
    "Looks like you forgot to type something!",
    "Your message is empty, try writing something.",
    "Oops! Did you mean to send a message?",
    "I see a blank space... did you forget to type?",
    "Your message box seems lonely. Try adding some words!",
    "Nothing detected. Maybe a typo?",
    "Did your keyboard take a break? I see nothing!",
    "You're sending air, but I need words!",
    "If silence is golden, your message is priceless!",
    "You sent... nothing! Try again?",
    "Invisible messages don't work on me. Try again!",
    "Your message is so quiet, even I can't hear it.",
    "I love chatting, but I need something to read!",
    "Oops! Your message vanished into thin air.",
    "I appreciate the effort, but I need actual text!",
    "Are we playing hide and seek? I can’t find your message!",
    "I can’t reply to silence... Try saying something!",
    "Your keyboard might be shy. Give it another try!",
    "I'm here, but I need words to respond!"
    "Hey, don’t be shy—type something in!",
    "I'm good at reading, but not minds. Try writing a message!",
    "Silence detected. Is that your way of saying hi?",
    "No words? No worries! Just try again.",
    "Hmm… I think your message took a vacation.",
    "All I see is emptiness. Fill it with your thoughts!",
    "Sending a blank? I know you can do better!",
    "That message was so stealthy, I missed it completely!",
    "Oops, nothing came through. Want to try again?",
    "Quiet messages are hard to reply to!",
    "Did you just whisper digitally? I couldn’t hear it.",
    "The message box is hungry—feed it some text!",
    "I’m not ignoring you, there’s just nothing to see!",
    "I promise I’ll reply—just give me something to work with!",
    "You typed... the void. Want to try again with words?",
    "Your message might be in invisible ink!",
    "That was the quietest message I’ve ever seen!",
    "Hmm, is this a minimalist form of communication?",
    "I detect… absolutely nothing. Type again?",
    "Nice try, ninja. But I need actual text to respond!"])

    if response_type == "exp":
        expr = [
    f"It's {result}",
    f"The answer is {result}",
    f"That makes {result}",
    f"The result is {result}",
    f"Math says: {result}",
    f"I calculated it, and it's {result}",
    f"You get {result}",
    f"The solution is {result}",
    f"After calculating, I got {result}",
    f"Here's what I found: {result}"]
        return random.choice(expr)
    
    if response_type == "one":
        responses = [
    f'Just "{result}"? It seems like you\'re emphasizing something specific!',
    f'Hmm, you just typed "{result}"? It seems like a unique choice of character!',
    f'You entered "{result}"? That\'s an interesting symbol!',
    f'Did you mean to type "{result}"? Seems like a symbolic choice.',
    f'Just "{result}", huh? That symbol stands out!',
    f'So, "{result}"? What does that symbolize?',
    f'Hmm, "{result}", that\'s a curious character to focus on!',
    f'Just a single "{result}"? That feels like an intentional choice!',
    f'Ah, "{result}", seems like you\'re highlighting something important!',
    f'I see you typed "{result}", that\'s a short but impactful symbol!',
    f'I notice "{result}", that symbol seems significant in its own way.',
    f'Only "{result}"? It seems like you\'re saying something in a minimal way.',
    f'Oh, "{result}"? Looks like you\'re getting straight to the point with that symbol.',
    f'It\'s just "{result}", but it feels like it carries meaning!',
    f'A lone "{result}", intriguing choice!',
    f'You picked "{result}"? That\'s a symbol of focus, isn\'t it?',
    f'I see "{result}". It\'s a small but powerful choice of symbol.',
    f'I noticed "{result}". Looks like you\'re emphasizing something important.',
    f'Just "{result}", that\'s a very minimalistic message, but meaningful.',
    f'Only "{result}"? That character stands out in a conversation.']


        return random.choice(responses)



    if response_type == "faq":
        return result
    elif response_type == "casual_talk":
        if text.isdigit():
            number_responses = [
    "Hmm... That looks like a number. Do you need any calculations?",
    "I see numbers! Need help with math?",
    "Oh, a number! What should I do with it?",
    "That looks like a phone number! But I can't make calls. ",
    "Numbers detected! Are we solving an equation?",
    "You just sent a number. Do you want me to convert it into something?",
    "Interesting! Do you need me to do some math with that?",
    "Numbers everywhere! Are we playing a math game?",
    "That’s a number! Should I check if it's even or odd?",
    "Cool, you sent a number! Want me to guess something about it?",
    "Numbers, numbers... Do you need calculations or just having fun?",
    "You just typed a number! Should I square it for you?",
    "Math time! Do you need help with something?",
    "Oh, a number! Do you want me to convert it into words?",
    "That’s an interesting number! What do you want to do with it?",
    "Numbers detected! Should I check if it’s prime?",
    "That looks important! Is it a secret code? 👀",
    "A number, nice! But what does it mean?",
    "That’s a cool number! Want me to generate a fact about it?",
    "Math detected! Should I solve something for you?"]
            return random.choice(number_responses)

    
        else:
            help_responses = [
    "Let me know if you need help!",
    "Let me know if you need anything.",
    "Let me know if you need assistance.",
    "Let me know how I can help.",
    "Let me know if you have any questions.",
    "Let me know if there's anything I can do.",
    "Let me know if you need support.",
    "Let me know if you ever need my help.",
    "Let me know if I can assist you with something.",
    "Let me know if you want me to clarify anything.",
    "Let me know if you get stuck.",
    "Let me know if I can be of any help.",
    "Let me know if you need more information.",
    "Let me know if you have any doubts.",
    "Let me know if you’d like me to explain further.",
    "Let me know if you’re looking for something specific.",
    "Let me know if I can guide you through anything.",
    "Let me know if I can do anything else for you.",
    "Let me know if you’re unsure about anything.",
    "Let me know if there's something I can assist with."]

            return random.choice(help_responses)
    elif response_type == "help_request":
        query = " ".join(result.split()[:5]) #Take only the first 5 words to avoid errors
        answer = fetch_info(query)
        return f"{answer}"

print("\n")
ascii_art = pyfiglet.figlet_format("                                OrvoAI")
print(ascii_art)
print("  Orvo 1.0  (Original)\n")

H=6
phrases =[
    "Hello! Feel free to send me a message. :)",
    "Hey there! What’s on your mind? ;)",
    "Hi! How can I assist you today? :D",
    "Hello! Type anything to start our chat. ^_^",
    "Hey! Let’s talk. What’s up? :P",
    "Hi! I’m here to chat. Say something! :o",
    "Hello! Ask me anything. :)",
    "Hey! Tell me what you’re thinking about. ;D",
    "Hi there! Ready to chat? :)",
    "Hello! What would you like to talk about? :3"]

random_phrase = random.choice(phrases)
R=random_phrase.lower()
typing_speed = 0.02  # Less seconds = faster (e.g. 0.01 = ultra fast, 0.1 = slow)
# Display with adjustable speed

print("🤖: ", end="", flush=True)  
for char in random_phrase:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(typing_speed)  # Change speed
print()  
while True:
    now = datetime.now().strftime("%H:%M")
    now1 = datetime.now().strftime("%A, %B %d, %Y")


    user_input = input("You: ")

    sys.stdout.flush()
    H=user_input.lower()

   
    if user_input.lower() in ["exit", "quit", "bye", "see you", "goodbye"]:
        
        goodbye_phrases = [
    "Goodbye! Have a great day! :)",
    "See you later! Take care! ;)",
    "Bye! Hope to chat again soon! :D",
    "Farewell! Wishing you all the best! ^_^",
    "Take care! Catch you next time! :')",
    "Bye for now! Stay safe! :P",
    "See you! Have an amazing day! :o",
    "Goodbye! Don't forget to smile! :]",
    "Later! Enjoy the rest of your day! :3",
    "So long! Hope to talk again soon! ;D"]
        random_goodbye = random.choice(goodbye_phrases)
        typing_speed = 0.03  # 0.1 = slow, 0.05 = normal, 0.02 = fast, 0.01 = ultra fast

        # Display function with "typewriter" effect
        print("🤖: ", end="", flush=True)  
        for char in random_goodbye:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_speed)  
        print("\n")
        print("\n")
        break
    #1
    WASSUP=["Not much! How about you?", "Just here to help! What’s up with you?", "Nothing much, just chatting. You?","Yeah? What's up?","What's up?","Okay! What's up next?","Hey there! What’s on your mind?","Hello! What would you like to talk about?","Hey! Let’s talk. What’s up?","Haha, fair enough! Want to hear a joke?", "So... what’s on your mind?",
    "So, how can I assist you?",
    "So, tell me more!",
    "So... what do you want to talk about?",
    "So, what’s next?",
    "So, do you need any help?",
    "So, what brings you here?",
    "So, what do you want to do now?",
    "So, any thoughts?",
    "So... I’m listening!",
    "So, what are we discussing today?",
    "So, what’s your question?",
    "So, do you have anything on your mind?",
    "So, do you need any information?",
    "So, what can I do for you?",
    "So... I'm curious, tell me more!",
    "So, let me know how I can help!"]
    WASSUP_lower = [response.lower() for response in WASSUP]
    
    NOTHING = ["Nothing special","nothing", "Not really anything special", "Same old","Nothing much", "Just the usual", "Not much going on", "Nothing new"]
    NOTHING_lower = [response.lower() for response in NOTHING]
    match1=difflib.get_close_matches(H,NOTHING_lower,n=1, cutoff=0.7)
    H1=  " ".join(match1)

    #2
    rr={"Haha, fair enough! Want to hear a joke? :D",
    "Glad you found that funny!You want another joke?:D ",
    "Haha! I like your laugh! You want another one?:D",
    "LOL! Want to hear another one?:D ",
    "You're making me laugh too! More jokes?:D",
    "Haha! That made my day! :P",
    "Glad I could make you smile!You want to laugh more? ;) ",
    "Laughter is the best medicine! More joke ? ",
    "Haha! You have a great sense of humor! Another joke? ;) ",
    "LOL! That was a good one, right? ;)",
    "I'm here to make you laugh anytime! ;) ",
    "Nothing? Fair enough! Want to hear a joke?"}
    b_lower = [respon.lower() for respon in b]
    hh={"yes","yep","yeah","joke","i want a joke","more","need more","another one","more joke"}
    match3=difflib.get_close_matches(H,hh,n=1, cutoff=0.7)
    H2=  " ".join(match3)
    hhh={"hahahahaha","hahaha","hhhhh","hhhhhhhhhhhhhhhhh"}
    match4=difflib.get_close_matches(H,hhh,n=1, cutoff=0.7)
    H4=  " ".join(match4)

    #3
    no={ "no","nope","noooooooooo","nooooo", "nah uh"}
    okey={ "All good?","Everything okey?","You okey?","You good?"}
    okey_lower = [respon.lower() for respon in okey]
    match5=difflib.get_close_matches(H,no,n=1, cutoff=0.7)
    H5=  " ".join(match5)
    

    if R in WASSUP_lower  and (H in NOTHING_lower or H1 in NOTHING_lower):
        bot_responses = [
    "Got it! Want to chat about something else?",
    "No worries! I'm here if you need me.",
    "Nothing? Its okay! If you ever get bored, I'm here!",
    "Nothing? That’s fine! What's on your mind?",
    "Nothing? Fair enough! Want to hear a joke?",
    "Okay! How’s your day going otherwise?",
    "I see! Well, I'm always here for a chat!"]


        response = random.choice(bot_responses)

# Typewriter effect speed (adjust if needed)

        typing_speed = 0.05  

        print("🤖: ", end="", flush=True)
        for char in response:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_speed) 
        print()  
        if response == "Nothing? Fair enough! Want to hear a joke?":
            R="Nothing? Fair enough! Want to hear a joke?"
     

    
    elif(R in rr or R in b_lower) and (H in hh or H2 in hh):
        response = chatbot_response("joke", now, now1)
        R=response.lower()
        typing_speed = 0.02  

        
        print("🤖: ", end="", flush=True)
        for char in response:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_speed) 
        print()  

    
    elif R in b_lower and (H in hhh or H4 in hhh):
        laugh_responses = [
    "Glad you found that funny!You want another joke?:D ",
    "Haha! I like your laugh! You want another one?:D",
    "LOL! Want to hear another one?:D ",
    "You're making me laugh too! More jokes?:D",
    "Haha! That made my day! :P",
    "Glad I could make you smile!You want to laugh more? ;) ",
    "Laughter is the best medicine! ",
    "Haha! You have a great sense of humor! Another joke? ;) ",
    "LOL! That was a good one, right? ;)",
    "I'm here to make you laugh anytime! ;) "]
        random_laugh = random.choice(laugh_responses)
        typing_speed = 0.03 

        
        print("🤖: ", end="", flush=True) 
        for char in random_laugh:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_speed)
        print()
        R=random_laugh

    

    elif R in okey_lower  and (H in no or H5 in no):
        helpp= [
    "Oh no! What's wrong?",
    "I'm here if you want to talk about it.",
    "That doesn't sound good. Want to share?",
    "Anything I can do to help?",
    "I'm here for you. What's going on?",
    "Hope things get better soon!",
    "Would you like to talk about it?",
    "I'm all ears. What's bothering you?",
    "You're not alone. I'm here to chat!"]
        random_helpp=random.choice(helpp)
        typing_speed = 0.03  
        print("🤖: ", end="", flush=True)  
        for char in random_helpp:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_speed)  
        print()
        R=random_helpp
        

    else:
       
        response = chatbot_response(user_input.lower(),now,now1)
        R=str(response).lower()

        typing_speed = 0.02  
      
        print("🤖: ", end="", flush=True)
        for char in str(response):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_speed) 
        print()  
       