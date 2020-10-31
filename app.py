from flask import Flask, render_template, request

from lib.chatbot import response, greeting

app = Flask(__name__)

def format_response(recipe):
    return recipe.replace("\n", "<br>")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    user_response = str(userText).lower()
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            return "You are welcome.."
        else:
            if greeting(user_response) is not None:
                return greeting(user_response)
            else:
                return format_response(response(user_response))
    else:
        return "Bye! take care.."

if __name__ == "__main__":
    app.run()
