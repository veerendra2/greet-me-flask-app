#!/usr/bin/env python3
'''
Author: Veerendra Kakumanu
Description: A simple flask application that greets you according to the time of day.
'''

from flask import Flask, render_template, request, jsonify
import logging
from waitress import serve
from datetime import datetime

__author__ = "Veerendra.Kakumanu"

PORT = 8080
APP_VERSION = "0.2"

def greet_client(client_time):
    '''
    returns greeting message to client depends on client's time

    :param client_time: client's time
    :type game_name: string
    :return: string
    '''
    datetime_obj = datetime.strptime(client_time, "%Y-%m-%dT%H:%M:%S.%fZ").time()
    if datetime_obj < datetime.strptime('12:00', '%H:%M').time():
        return "Good morning!"
    elif datetime_obj < datetime.strptime('18:00', '%H:%M').time():
        return "Good afternoon!"
    else:
        return "Good evening!"

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template("index.html", version=APP_VERSION)

@app.route('/datetime', methods=["POST"])
def get_datetime():
    client_datetime = request.json["datetime"]
    greet_msg = greet_client(client_datetime)
    print("Client date and time:", client_datetime)
    return jsonify(greet_msg=greet_msg)

def main():
  logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
  serve(app, host="0.0.0.0", port=PORT)

if __name__ == '__main__':
    main()