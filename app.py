from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

responses = [
    [r"hey", ["Hello %1, How are you today ?"]],
    [r"hi|hey|hello", ["Hello", "Hey there"]],
    [r"what is your name?", ["My name is Chatbot"]],
    [r"how are you?", ["I'm doing good. How about You ?"]],
    [r"sorry (.*)", ["Its alright","Its OK, never mind"]],
    [r"I am fine", ["Great to hear that, How can I help you?"]],
    [r"quit", ["Bye-bye, take care"]],
    [r"container", ["Sure, please type the container details in the chat."]],
    [r"vulnerability", ["Sure, please type the vulnerability details in the chat."]],
    [r"risk", ["Sure, please type the cve details"]],
    [r"cve", ["Sure, please type the cve details in the chat."]],
    [r"bye", ["Thanks, take care,bye."]],
]

chatbot = Chat(responses, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_message = request.args.get('msg')
    return str(chatbot.respond(user_message))

if __name__ == "__main__":
    app.run(debug=True)
