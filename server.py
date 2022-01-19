from lib2to3.pgen2.token import NEWLINE
from os import name
from urllib import request
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     return 'Form submitted successfully!'


def write_csv(data):
    with open('database.csv', mode='a', newline='') as my_csv_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(my_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

def write_data(data):
    with open('database.txt', mode='a') as myfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        myfile.write(f'\n {email} {subject} {message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'failed to be saved into the database.'
    else:
        return 'Someting went wrong.    '