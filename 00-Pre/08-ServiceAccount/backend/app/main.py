from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

SA_TOKEN = None
SA_TOKEN_FROM_PATH = None
SA_TOKEN_PATH = '/var/run/secrets/kubernetes.io/serviceaccount/token'

class Data(BaseModel):
    token: str

@app.post("/api/pods")
def default(data: Data):
    fetch_status = False
    err_message = ""
    pods = []
    global SA_TOKEN
    SA_TOKEN = data.token or SA_TOKEN_FROM_PATH
    
    if SA_TOKEN is not None:
        result = requests.get("https://kubernetes.default.svc/api/v1/namespaces/default/pods", headers={'Authorization':'Bearer '+ str(SA_TOKEN)}, verify=False)
        if(result.status_code == 200):
            fetch_status = True
            pods = result.json()
        else:
            print(f"An error occurred while fetching the data - error_code = {result.status_code}")
            err_message = f"An error occurred while fetching the data - error_code = {result.status_code}"
        
        # https://kubernetes.default.svc/api/v1/namespaces/default/pods
    print(f"'status': {fetch_status}, 'data': pods, 'error': {err_message}")
    return {'status': fetch_status, 'data': pods, 'error': err_message}

if __name__:
    if(os.path.exists(SA_TOKEN_PATH)):
        f =  open(SA_TOKEN_PATH,"r")
        SA_TOKEN_FROM_PATH = f.read()
