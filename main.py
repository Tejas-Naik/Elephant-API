from flask import Flask,redirect,url_for,render_template,request
import requests

response = requests.get('https://elephant-api.herokuapp.com/elephants')
elephants = response.json()

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/all')
def load_all_elephants():
   return render_template('all_elephants.html', elephant=elephants)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)