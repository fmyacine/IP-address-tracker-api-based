from flask import Flask, redirect, render_template,request
from ipaddress import is_global
app = Flask(__name__)

@app.route("/")
def index():
    ip = request.args.get("ip")
    if not ip:
        return render_template("layout.html")
    elif is_global(ip):
        return render_template("layout.html")