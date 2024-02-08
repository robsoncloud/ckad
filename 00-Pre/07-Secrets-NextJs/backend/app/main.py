from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import requests
import os 
import socket 

SA_TOKEN = None
SA_TOKEN_FROM_PATH = None
SA_TOKEN_PATH = '/var/run/secrets/kubernetes.io/serviceaccount/token'
APP_NAME = "APP_NAME" in os.environ and os.environ.get("APP_NAME") or "My Kubernetes Dashboard"

app = FastAPI()

class Data(BaseModel):
    token: str

@app.get("/api/pods")
def default():
    return {"Hello": "World"}

@app.post("/api/pods")
def default(data: Data):
    global SA_TOKEN 
    err_message = ""
    load_result = False
    pods = []
    
    SA_TOKEN = data.token or SA_TOKEN_FROM_PATH
    print(f"SA_TOKEN={SA_TOKEN}")
    try:
        response = requests.get('https://kubernetes.default.svc/api/v1/namespaces/default/pods',headers={'Authorization':'Bearer ' + str(SA_TOKEN)}, verify=False)
        if response.status_code == 200:
            pods = response.json()
            load_result = True
        else:
            err_message = f"Request failed with status code {response.status_code}"
            
    except Exception as e:
        err_message = str(e)
        
    return {"success": load_result,"err_message": err_message, "data": pods}

if __name__:
    if(os.path.exists(SA_TOKEN_PATH)):
        f = open(SA_TOKEN_PATH, "r")
        SA_TOKEN_FROM_PATH = f.read()

