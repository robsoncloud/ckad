from flask import Flask
from flask import render_template

import os # to get the env variable
import socket # to get the name of the host
import argparse # to get the arguments
import random # to randomly choose a color

color_codes = {
      "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

COLOR = random.choice(list(color_codes.keys()))
SUPPORTED_COLORS = ", ".join(color_codes.keys())
COLOR_FROM_ENV = os.environ.get("APP_COLOR")

app = Flask(__name__)

@app.route("/")
def default():
    return render_template("hello.html",name=socket.gethostname(),color=color_codes[COLOR])


if(__name__):
    parser = argparse.ArgumentParser()
    parser.add_argument("--color", required=False)
    args = parser.parse_args()
    if(args.color):
        COLOR=args.color
        print("Color set by the command-line --color {0}".format(args.color))
        if(COLOR_FROM_ENV):
            print("Color defined by environment variable will be ignored due to the precedence")
    elif COLOR_FROM_ENV:
        COLOR=COLOR_FROM_ENV
        print("Color set by the env variables COLOR_FROM_ENV {0}".format(COLOR_FROM_ENV))
    else:
        print("Color picked up automatically - {0}".format(COLOR))
    
    if(COLOR not in color_codes):
        print("COLOR NOT VALID - {0} - Select on from the list [{1}]".format(COLOR,SUPPORTED_COLORS))
        exit(1)
        
    app.run("0.0.0.0",8080)
    
    



