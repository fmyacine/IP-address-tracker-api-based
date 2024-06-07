from flask import Flask, redirect, render_template,request
from ipaddress import is_global
from api import apiFirst, apiSearch
app = Flask(__name__)

@app.route("/")
def index():
    ip = request.args.get("ip")
    if not ip:
        ip1st = apiFirst()
        ipRes = apiSearch(ip1st["ip"])
        return render_template("layout.html",api = ipRes)
    else:
        return render_template("layout.html")