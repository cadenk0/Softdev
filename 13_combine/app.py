# Yinwei Zhang, Aditya Anand, Caden Khuu
# CAY
# SoftDev
# K13 <Occupations table format with links>
# 2024-9-30
# Time Spent : 1.2 Hour

import random
import csv
from flask import Flask

app = Flask(__name__)

def readfile(f):
    d = {}
    with open (f, 'r') as listfile:
        reader = csv.reader(listfile)
        next(reader)
        for row in reader:
            job = row[0]
            if job == "Total":
                continue
            percent = float(row[1])
            d[job] = percent
    return d
        
        
def sel(d):
    return random.choices(list(d.keys()), weights=d.values(), k=1)[0]

@app.route("/")

def page():
    occ = sel(readfile("data/occupations.csv"))
    code = """
    <!DOCTYPE html>
    <html>
      <body>
            <p>CAY with Caden, Yinwei, Aditya.</p>
            <h1>This time: """ + occ + """
            </h1><h2>Occupations</h2>
    """
    for a, b, c in readfile("data/occupations.csv").items():
        code += "<li>" + a + ": " + str(b) + ", Link: " + str(c) + "</li>"

    code += "</body></html>"
    return code

if __name__ == "__main__":
    app.debug = True
    app.run()
