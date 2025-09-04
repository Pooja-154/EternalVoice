from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai
import pyttsx3

# Gemini API Config
os.environ["GOOGLE_API_KEY"] = "AIzaSyCE3PRBPyCQRbNqrJ0hqOjdnPoED3lL8Xs"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

# Flask setup
app = Flask(__name__)

# Text-to-Speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 180)

# Memory
history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    mode = request.json.get('mode', 'Default')

    # Mode-specific prompt prefix
    mode_prompts = {
        "Motivation": "Respond like a motivational coach who inspires with powerful and uplifting words.",
        "Fatherly Love": "Respond with gentle, caring, fatherly advice full of warmth.",
        "Sarcasm": "Respond sarcastically but humorously, as if playfully teasing.",
        "Default": "Respond normally."
    }

    style = mode_prompts.get(mode, "Respond normally.")

    # Combined prompt
    prompt = f"{style}\nUser: {user_input}\nBot:"

    response = model.generate_content(prompt)
    reply = response.text.strip()

    engine.say(reply)
    engine.runAndWait()

    return jsonify({'reply': reply})


if __name__ == '__main__':
    app.run(debug=True)
