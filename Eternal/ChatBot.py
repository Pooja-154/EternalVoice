# chatbot_voice.py

import pyttsx3  # For voice output
import time

# Initialize TTS engine (replace with your own model if needed)
engine = pyttsx3.init()

# Optional: Configure voice properties
engine.setProperty('rate', 150)  # speed
engine.setProperty('volume', 1.0)

# Simulated Chatbot Logic (replace with your model later)
def chatbot_reply(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a program, but I'm running smoothly!",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.")

# Function to speak response using TTS model
def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

# Main Chat Loop
print("🤖 Chatbot is ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        speak("Exiting now. Bye!")
        break
    response = chatbot_reply(user_input)
    speak(response)
    time.sleep(0.5)
