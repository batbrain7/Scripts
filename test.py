import os
import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/start/<browser>/<url>")
def startBrowser( browser , url):
    url = "http://{}".format(url)
    os.system("open -a " + browser + " " + url)
    return "Opened the browser"

@app.route("/getURL")
def getURL():
    os.system("osascript -e\'tell application \"Google Chrome\" to get URL of tab 24 of window 1\'")
    return "Check your terminal"

@app.route("/stop/<browser>")
def stop(browser):
    if browser == "Firefox":
        os.system("kill 2403")
    else:
        os.system("kill 4428")
    return "Killed the process"

if __name__ == '__main__':
    app.run(debug=True)


