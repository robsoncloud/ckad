from flask import Flask
from flask import render_template

import os
import socket
import random
import argparse


color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

COLOR = random.choice(list(color_codes.keys()))
COLOR_FROM_ENV = os.environ.get("APP_COLOR")
SUPPORTED_COLORS = ", ".join(color_codes.keys())

app = Flask(__name__)

@app.route("/")
def default():
    return render_template("hello.html",name=socket.gethostname(), color=color_codes[COLOR])

if(__name__):
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--color", required=False)    
    args = parser.parse_args()
    
    if(args.color):
        print("The color has been set via command-line - {0}".format(args.color))
        COLOR = args.color
        if(COLOR_FROM_ENV):
            print("The color has been also set via environemnt variable however the command-line takes precedence.")
    elif COLOR_FROM_ENV:
            print("The color has been set via environment variable - {0}".format(COLOR_FROM_ENV))
            COLOR = COLOR_FROM_ENV
    else:
        print("The color hasn't been set - one color has been set randomly - {0}".format(COLOR))
        
    if(COLOR not in color_codes):
        print("The color {0} is not available! Choose a different one from the list [{1}]".format(COLOR,SUPPORTED_COLORS))
        exit(1)
    
    app.run("0.0.0.0",8080)
