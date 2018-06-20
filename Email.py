import requests
 
from flask import Flask
from flask_mail import Mail, Message
from flask_restplus import Resource, Api

app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.mailgun.org',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'postmaster@sandbox7bd32e3ca8214c9aa914141780905c8d.mailgun.org',
	MAIL_PASSWORD = 'e699b21e17aea111c3b1f0a1d60879b4'
	)
mail = Mail(app)

api=Api(app,title="EMail",description="Sending Mail",)

@api.route('/<string:mail_id>')
class methods(Resource):
    @api.doc('send msg')
    @api.response(204, 'msg sent')
    def post(self, mail_id):
        msg = Message("Hello!",
		sender="postmaster@sandbox7bd32e3ca8214c9aa914141780905c8d.mailgun.org",
		recipients=[mail_id])
	msg.body = "JusT a teStIng Mail"           
	mail.send(msg) 
	return '', 204


if __name__ =='__main__':
  app.run(debug=True)