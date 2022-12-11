from flask import Flask, jsonify, request
app = Flask(__name__)
app.config['SECRET_KEY']='XXXXXXX'

from mailjet_rest import Client


api_key = '5b0e93b218a848afdaeab1685c1c792c'
api_secret = '721c122338c12d79106f1ba8196ea5ae'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')


@app.route('/sendEmail',methods=["POST"])
def sendEmail():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json
        name = body["name"]
        email = body["email"]
        data = {
  'Messages': [
    {
      "From": {
        "Email": "ana.customer1000@gmail.com",
        "Name": "Cipher2022"
      },
      "To": [
        {
          "Email":email,
          "Name": name
        }
      ],
      "Subject": "Greetings from Cipher2022.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear {{name}} , Your registration for Cipher2022 is confirmed.<\br>Thank you.",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print (result.json())
        return jsonify({"Accepted":202}),202
    else:
        return jsonify({"Bad Request":400}),400
        
    
if __name__ == '__main__':
	app.run(debug=True)

