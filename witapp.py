from wit import Wit
from pprint import pprint


access_token = "CHTZRFS2AYAOX4IYLWYVTVCNKWVXWBRN"
client = Wit(access_token = access_token)


def get_wit_response(message_text):
    wit_response = client.message(message_text)
    pprint(wit_response)
    entity = None
    try:
        entities = list(wit_response['entities'].keys())
        for key in entities:
            entity = key
    except:
        pass
    return (entity)


def generate_user_response(messaging_text):
     entity = get_wit_response(messaging_text)
     print(entity)
     if entity == "greetings:greetings":
          response = "Hello, This is K&H Brand, How i can help you?"
     elif entity == "working_hours:working_hours":
          response = "What are the working hours, From Sunday to Friday from 9 am to 11 pm, And Saturday from 12 pm to 6 pm ,The website is available all the time"
     elif entity == "brands:brands":
          response = "We have the following brands: Adidas, Nike, Puma, Rolex, and we also have our own brand."
     elif entity == "make_order:make_order":
          response = "please , send your name , email , address and phone number."
     elif entity == "pay_methods:pay_methods":
          response = "You can pay with visa, mastercard or cash"
     elif entity == "installment:installment":
          response = "Yes, by credit card without any fees"
     elif entity == "exchange:exchange":
          response = "Yes , within 30 days you can exchange piece but you can return it within only 20 days ."
     elif entity == "offers:offers":
          response = "At the end of each month we make discounts, on holidays and official occasions, and on Black Friday, all discounts are announced on the page"
     elif entity == "recive_order:recive_order":
          response = "within 4 or 5 days."
     elif entity == "end_messeges:end_messeges":
          response = "Thank you for contact with us, see you soon! :)"
     elif entity == "colors:colors":
          response = "if there is , will send all colors"
     elif entity == "adderss:adderss":
          response = "Our shop is at 15 Talaat Harb Street, Downtown, Cairo - Egypt"
     elif entity == "adderss:adderss":
          response = "Our shop is at 15 Talaat Harb Street, Downtown, Cairo - Egypt"
     else:
          response = "Sorry, i didn't understand you!"
     return response
