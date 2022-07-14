import os
from flask import Flask, render_template, request, send_from_directory
from flask_mail import Mail, Message
from private import *

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.root_path, 'downloads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# configuration of mail
mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = USERNAME
app.config['MAIL_PASSWORD'] = PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendmail', methods=['POST'])
def sendmail():
    name = request.form.get('txtName')
    email = request.form.get('txtEmail')
    msg_body = f'Contact from: {name}, {email}\n\n'
    msg_body += request.form.get('areaMsg')
    msg = Message('Contact From my Porfolio', sender = USERNAME, recipients = [USERNAME])
    msg.body = msg_body
    mail.send(msg)
    return render_template('mail_sent.html', name=name)

@app.route('/downloads/<path:name>')
def download(name):
    key = request.args.get('key')
    print(key)
    if key == CV_KEY:
        return send_from_directory(app.config['UPLOAD_FOLDER'], name)
    else:
        return 'Invalid Key'

if __name__ == '__main__':
    app.run(debug=True, port=5550)