import praw
from flask import Flask, request, render_template, jsonify
import joblib
import nltk
import re

app = Flask(__name__,template_folder='template')


model = joblib.load('model/production_model.pkl')

client_id = ""
client_secret = ""
user_agent = ""
username = ""
password = ""

reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent, username = username, password = password)


def clean_text(text):
    text = re.sub('[/(){}\[\]#\|@,"".?'':;*!$]', '', text)
    text = re.sub('[^0-9A-Za-z #+_]', '', text)
    return text

def prediction(url):
    submission = reddit.submission(url = url)
    data = {}

    data["Title"] = str(submission.title)
    data["Content"] = str(submission.selftext)
    data["URL"] = str(submission.url)


    data['Title'] = clean_text(str(data['Title']))
    data['Content'] = clean_text(str(data['Content']))
    data['URL'] = str(data['URL'])

    combined_features = data["Title"] + data["Content"] + data["URL"]

    return model.predict([combined_features])


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction_page():
	if request.method == 'GET':
		return render_template('prediction.html')

	if request.method == 'POST':
		text = request.form['url']
		flair = prediction(str(text))
		return render_template('prediction.html', original_input={'url':str(text)}, result=flair[0])

@app.route("/automated_testing",methods=['POST'])
def test():
	if request.files:
			file = request.files["upload_file"]
			texts = file.read()
			texts = str(texts.decode('utf-8'))
			links = texts.split('\n')
			pred = {}
			for link in links:
				pred[link] =  prediction(str(link))[0]
			return jsonify(pred)
	else:
			return 400

if __name__ == '__main__':
	app.run()
