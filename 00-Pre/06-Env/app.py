from flask import Flask
from flask import render_template

import socket
import os
import random
import argparse


colors_code = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}


COLOR = random.choice(list(colors_code.keys()))
SUPPORTED_COLORS = ", ".join(colors_code.keys())

COLOR_FROM_ENV = os.environ.get("APP_COLOR")

app = Flask(__name__)

@app.route("/")
def default():
    return render_template("hello.html",name = socket.gethostname(), color = colors_code[COLOR])

if(__name__):
    parser = argparse.ArgumentParser()
    parser.add_argument("--color",required=False)
    args = parser.parse_args()
    if(args.color):
        COLOR = args.color
        print("COLOR has been set from the command-line - {0}".format(args.color))
        if(COLOR_FROM_ENV):
            print("COLOR set from COLOR_FROM_ENV - {0} can't be used due to the --color command-line".format(COLOR_FROM_ENV))
    elif COLOR_FROM_ENV:
        COLOR = COLOR_FROM_ENV
        print("COLOR has been set from the enviroment variable APP_COLOR - {0}".format(COLOR_FROM_ENV))        
    else:
        print("COLOR HAS BEEN SET RANDOMLY - {0}".format(COLOR))
        
    if(COLOR not in colors_code):
        print("COLOR {0} not supported, please choose one of the following [{1}]".format(COLOR, SUPPORTED_COLORS))
        exit(1)
    
    app.run("0.0.0.0", 8080)
