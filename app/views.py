from flask import Flask, render_template, redirect, request, url_for, make_response
import random
import string

app = Flask(__name__)

file="1.txt"


url =' '

@app.route("/")
def home():
	return render_template('index.html')







@app.route("/nice", methods=["POST"])
def new_url():
	url = request.form['long_url']
	short_url = Makeurl()
	newurl = "http://" + request.headers['Host'] + '/' + short_url
	with open(file, "w") as f:
		f.write(short_url + ' ' + url + '\n')
	resp = make_response(redirect(url_for('home')))
	return render_template('index.html', url=url, newurl=newurl)




def Makeurl():
	#s = "http://" + request.headers['Host'] + randomword(9)
	s = randomword(9)
	return s

def randomword(length):
	return ''.join(random.choice(string.lowercase) for i in range(length))	


def get_url(sh_url):

	with open(file, "r") as fl:
		for line in fl:
			if line.split(' ')[0]==sh_url:
				return line.split(' ')[1].rstrip('\n')



@app.route("/<generated_link>")
def follow(generated_link):
	return redirect(get_url(generated_link))

if __name__ == "__main__":
	app.run(debug=True)