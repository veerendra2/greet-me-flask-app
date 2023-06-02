#!/usr/bin/env python3
'''
Author: Veerendra Kakumanu
Description: A simple application greets clients according to time
'''

from flask import Flask, request, render_template
import os
import requests
import logging
from waitress import serve
from datetime import datetime

__author__ = "Veerendra.Kakumanu"

PORT = 8080

def greet_client(client_time):
    '''
    returns greeting message to client depends on client's time

    :param client_time: client's time
    :type game_name: string
    :return: string
    '''
    if client_time < datetime.strptime('12:00', '%H:%M').time():
        return "Good morning!"
    elif client_time < datetime.strptime('18:00', '%H:%M').time():
        return "Good afternoon!"
    else:
        return "Good evening!"

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/datetime', methods=['POST'])
def get_datetime():
    datetime = request.json['datetime']
    print('Client date and time:', datetime)
    return datetime

def main():
  logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
  serve(app, host='0.0.0.0', port=PORT)

if __name__ == '__main__':
    main()