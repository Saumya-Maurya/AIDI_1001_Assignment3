from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200553573"})

# Route to handle Dialogflow webhook requests
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    # Extract intent name from the request
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')

    # Example of handling different intents and generating responses
    if intent == 'Gadget Info':
        response_text = "Here is the information about the Gadgets."
    elif intent == 'Store Hours':
        response_text = "Here you can see the timings of the store."
    elif intent == 'Tech Categories':
        response_text = "You can find the categories available in the store."
    elif intent == 'Promotions and Discounts':
        response_text = "Here is the information about the discounts on the products."
    else:
        response_text = "I'm not sure how to respond to that."

    # Return the response in the required format
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
