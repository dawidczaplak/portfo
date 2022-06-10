from flask import Flask, render_template, url_for, request, flash, redirect
app = Flask(__name__)
import csv

@app.route('/')
def hello_world():
    return render_template('index.html')
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'thankyou.html' #trzeba stworzyc strone
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again'