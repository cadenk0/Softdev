'''Caden Khuu, Aditya Anand, Danny Huang
  CAD
  SoftDev
  Flask and HTML
  2024-9-26
  time spent: 0.5 hours
'''

import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

@app.route("/static/foo.html")
def hello():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(random.random())

'''
@app.route("/static/fixie.html")
def yeah():
    print("the __name__ of this module is... ")
    print(__name__)
    return "<h1>Team Name: CAD</h1><br><h2>Roster: Caden, Aditya, Danny</h2>"
'''
    
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
