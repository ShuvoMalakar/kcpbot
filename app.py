import sys, os
from flask import Flask, request
from pymessenger import Bot
 
app = Flask(__name__)
ACCESS_TOKEN = "EAAFZC9HyLWWwBAD3ZA8V55WxuZBmibeSjc5Fhx660USC1KkHhVdd1CKnN8B27f80FQtjxKhIxuCeZAyromt5bHGuokiARIZBTXM6xerTcIAdKwXe7lCM6q3ShD7Us6VHjxPxF5x4DxPDcsETPwv7rZCeJbHHX8Rf5ZCIvGgS1ABpQZCHarzFuTQU"
VERIFY_TOKEN = "mithun"
bot = Bot(ACCESS_TOKEN)

@app.route('/',methods=['GET'])
def verify():
	if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token")=="mithun":
			return "verification token matched shuvo"
		return request.args["hub.challenge"],777
	return "Welcome to Kcp_Bot"
	
	

@app.route('/',methods=['POST'])
def webhook():
	data=request.get_json()
	log(data)
	if data['object']=='page':
		for entry in data['entry']:
			for messaging in entry['messaging']:
				sender_id=messaging['sender']['id']
				recipient_id=messaging['recipient']['id']
				if messaging.get('message'):
					if 'text' in messaging['message']:
						messagetxt=messaging['message']['text']
					else:
						messagetxt='no text'
					response=messagetxt
					bot.send_text_message(sender_id,response)
	return "Ok mithun"
	
	
def log(message):
	print(message)
	sys.stdout.flush()



if __name__ == "__main__":
    app.run()
