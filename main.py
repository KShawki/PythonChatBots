import os, sys
from flask import Flask, request
import json
from pymessenger import Bot
from pprint import pprint
from witapp import generate_user_response
app = Flask(__name__)

VERIFICATION_TOKEN = "hello"
PAGE_ACCESS_TOKEN = "EAAHZBoyl1fw8BAHUHz8N1ysZBvVb1FP0vXREYK88nXaQZB15eVpHn6YWY6AdAB0u38Svp9LQMZA17UphE3gJ24PTzLqOSXhwvpMB7SnlFb8PrPsYaAtWHukWKN5pXNj2Hc3E3uUjloQJMGGqOiQJHBTrfQMqgYPe4lZA0W8bQYd53EVOwegEH"
bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello-world", 200

@app.route('/', methods=['POST'])
def webhook():
    printmsg("Starting Webhook")
    data = request.get_json()
    pprint(data)
    process_data(data)
    return "ok",200

def process_data(data): 
    if data["object"]=="page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                sender_id = messaging_event["sender"]["id"]
                recipient_id = messaging_event["recipient"]["id"]
                if messaging_event.get("message"):
                    if "text" in messaging_event["message"]:
                        messaging_text = messaging_event["message"]["text"]
                    else:
                        messaging_text = "no text"
                    if(sender_id == '103898431625143'):
                        bot.send_text_message(sender_id,messaging_text)
                        return
                    response = generate_user_response(messaging_text)
                    bot.send_text_message(sender_id,response)

def send_response(sender_id, response) :
    bot.send_text_message(sender_id, response)

def printmsg(msg):
    print(msg)
    sys.stdout.flush()

if __name__=="__main__":
    app.run(debug=True, port=80)
    
