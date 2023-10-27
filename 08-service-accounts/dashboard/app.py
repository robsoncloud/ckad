
from flask import Flask, request
from flask import render_template
from datetime import datetime
import requests
import os.path


app = Flask(__name__)
app.debug = True
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.use_reloader=True

SA_TOKEN = None
SA_TOKEN_FROM_PATH = None
SA_TOKEN_PATH = '/var/run/secrets/kubernetes.io/serviceaccount/token'

APP_NAME = "APP_NAME" in os.environ and os.environ.get(
    'APP_NAME') or "KUBE-DASH"


@app.route("/", methods=['GET'])
def main():
    try:

        SA_TOKEN =  SA_TOKEN_FROM_PATH
        # GET THE CLUSTER CONTROLE IP FROM os.env KUBERNETES_SERVICE_HOST=10.2.0.1
        test_results = requests.get('https://controller:6443/api/v1/namespaces/prod/pods', headers={'Authorization': 'Bearer ' + str(SA_TOKEN)},
                                            verify=False)
        result_data = test_results.json()

        items = []

        for item in result_data['items']:
            name = item['metadata']['name']
            phase = item['status']['phase']
            ip = item['status']['podIP']
            sa = item['spec']['serviceAccountName']
            node = item['spec']['nodeName']
            containers = item['spec']['containers']
            items.append({'name': name, 'phase': phase, 'ip': ip, 'sa': sa, 'node': node, 'containers': len(containers)})

        # for key, value in result_data.items():
        #  print(value.item)
       
        return render_template('index.html', data=items, app_name=APP_NAME, background_color='2980b9')
    except Exception as ex:
        print(str(ex))


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/test")
def teste():
    global SA_TOKEN
    json_data = request.get_json(silent=True)
    SA_TOKEN =  SA_TOKEN_FROM_PATH

    #print("SA_TOKEN=" + str(SA_TOKEN))
    
    test_results = requests.get('https://controller:6443/api/v1/namespaces/prod/pods', headers={'Authorization': 'Bearer ' + str(SA_TOKEN)},
                                        verify=False)
    print(test_results.json())

    return (test_results.text, test_results.status_code, test_results.headers.items())


if __name__ == "__main__":
    if os.path.exists(SA_TOKEN_PATH):
        f = open(SA_TOKEN_PATH, "r")
        SA_TOKEN_FROM_PATH = f.read()
    else:
        SA_TOKEN_FROM_PATH = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjFha2I0Q0J6SXFTeVo2UXNLMjJ3TndkZWpyeFNRZlFlZDJDdnl0RnBwaW8ifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzIwNDU4NzQzLCJpYXQiOjE2ODg5MjI3NDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJwcm9kIiwicG9kIjp7Im5hbWUiOiJ0ZXN0IiwidWlkIjoiNzRmMjIyMjEtNzM5Yi00MDY0LWEyMmMtOTFkMTc4YTJkMjQyIn0sInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJyb2Jzb24tMDEiLCJ1aWQiOiIyZDU3MzAzMy01ZDk4LTQ3NDEtYmU5OS00ODEzZGQ4MmU3Y2YifSwid2FybmFmdGVyIjoxNjg4OTI2MzUwfSwibmJmIjoxNjg4OTIyNzQzLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6cHJvZDpyb2Jzb24tMDEifQ.WLqdAGz9_1BC7e-pPRQhwnhDmKqPNIspOgGMe_iZVE0yt-AE9IdqhE6GHplwQ54nXj9gZIofL99XqhoHVFyljPQz2A7lB75o8z4gsPKE222L7yI_wG9y2RXiFARf8FfQghb6J5TxFs1dFKNZ7v9bt8TedzGf1STC0zZ1YBPQpC9cBhE2NcSJOR2ECMOgFCMdNWcf2-zdoiG_CuZ5eZtrFK4KTaOf6lTwNLnpnR8DNt6plZRbTVz3un4m1PK_zdn1OvlF1jVyCJKu3lVo6hqJXHJiZcfUzp4FNMB_dAkpTN80rShf2E271WJpmVfSofTjkszHOrHYE3UWB5JUjbvXyg'
    print(SA_TOKEN_FROM_PATH)    
    from livereload import Server, shell
    server = Server(app.wsgi_app)

    server.watch('static/*.stylus', 'make static')
    def alert():
        print('foo')
    server.watch('/home/robson/CKAD/08-service-accounts/dashboard/templates/index.html', alert)
    server.watch("/home/robson/CKAD/08-service-accounts/dashboard/templates/*.*")
    server.watch("static/*.*")
    server.serve()
    # app.run(host="0.0.0.0", port=8080, debug=True)
