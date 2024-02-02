import argparse, os
from flask import Flask, request, render_template

parser = argparse.ArgumentParser(description="Just an example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--color", help="Source location")

args = parser.parse_args()
config = vars(args)
print(config['color'])


app = Flask(__name__)

@app.route('/')
def hello_world():
    USERNAME = os.environ.get('USERNAME',"NOT DEFINED")
    if(USERNAME != 'NOT DEFINED'):
        print('ENV HAS BEEN DEFINED {0}'.format(USERNAME))
    return render_template('home.html', user=USERNAME, color=config['color'])

@app.route('/about')
def about():
    return render_template('about.html', organization='TestDriven.io')


if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')

    try:
        PORT = int(os.environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)
    