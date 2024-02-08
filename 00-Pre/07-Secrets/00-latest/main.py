from db.database import Database

from flask import Flask
from flask import render_template

import os
import socket

DB_Name = os.environ.get('DB_Name') 
DB_Host = os.environ.get('DB_Host')
DB_User = os.environ.get('DB_User')
DB_Password = os.environ.get('DB_Password')
DB_Port = os.environ.get('DB_Port')


app = Flask(__name__)

@app.route("/")
def default():
    db_connect_result = False
    err_message = ""
    
    try:
        
        db_handler = Database(DB_Name, DB_User, DB_Host, DB_Password, DB_Port)
        db_handler.connect()
        color = '#39b54b'
        db_connect_result = True
        db_handler.close()
    except Exception as e:
        color = '#ff3f3f'
        err_message = str(e)
    
    return render_template("default.html", debug="Enviroment Variables: DB_Host: "+ (os.environ.get('DB_Host') or "Not Set")+" DB_Name: "+ (os.environ.get('DB_Name') or "Not Set")+" DB_User: "+ ((os.environ.get('DB_User')or "Not Set") or "Not Set")+" DB_Password: "+ (os.environ.get('DB_Password')or "Not Set")+" DB_Port: "+(os.environ.get('DB_Port')or "Not Set") + "; "+ err_message, db_connect_result=db_connect_result, name=socket.gethostname(), color=color)
       

if __name__:
    app.run("0.0.0.0", 8080)
    

















# from db.db import Database


# if __name__ == "__main__":
#     try:
#         db = Database("tracker-issue-own-3", "postgres", "192.168.1.172", "1234", "5432")
#         db.connect()
#         rows = db.execute_query("""SELECT * FROM "Issue";""")
#         if rows:
#             for row in rows:
#                 print(row)
#     except Exception as e:
#         print(e)
