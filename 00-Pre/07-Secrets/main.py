from db.database import DatabaseHandler
from flask import Flask
from flask import render_template

import os
import socket

DB_Name = os.environ.get('DB_Name')
DB_User = os.environ.get('DB_User')
DB_Password = os.environ.get('DB_Password')
DB_Host = os.environ.get('DB_Host')
DB_Port = os.environ.get('DB_Port')


app = Flask(__name__)

@app.route("/")
def default():
    db_connect_result = False
    err_message = ""
    try:
        db_handler = DatabaseHandler(DB_Name, DB_User, DB_Password, DB_Host, DB_Port)
        db_handler.connect()
        color = '#39b54b'
        db_connect_result = True
        db_handler.close()
    except Exception as e:
        print(f"Connection to DB has failed. Error: ${e}")
        db_connect_result = False
        err_message = str(e)
        color = '#ff3f3f'

    return render_template("default.html",color=color, err_message=err_message, connected=db_connect_result, debug = f"Environment Variables: DB_Name: {DB_Name or 'NOT SET'} - hostname {socket.gethostname()}" )


if __name__:
    app.run("0.0.0.0",8080)

# if __name__:
#     db_handler = DatabaseHandler("tracker-issue-own-3", "postgres", "1234","192.168.1.172", "5432")
#     db_handler.connect()
#     rows = db_handler.execute_query("""SELECT * FROM "Issue";""")
#     if rows:
#         for row in rows:
#             print(row)
#     db_handler.close()