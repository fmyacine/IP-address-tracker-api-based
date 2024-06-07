from flask import Flask, redirect, render_template,request,flash
import ipaddress
from api import apiFirst, apiSearch
app = Flask(__name__)

@app.route("/")
def index():
    ip = request.args.get("ip")
    if not ip:
        ip1st = apiFirst()
        ipRes = apiSearch(ip1st["ip"])
        ipRes["offset"] = int(ipRes["offset"] / 3600)
        return render_template("layout.html",api=ipRes)
    else:
        try:
            ip_obj = ipaddress.ip_address(ip)
            ipRes = apiSearch(ip)
            return render_template("layout.html",api = ipRes)
        except(ValueError):
            flash("ip address invalid!")
            return redirect("/")
        
if __name__ == '__main__':
    app.run(debug=True)