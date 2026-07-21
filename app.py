from flask import Flask, request
from datetime import datetime
from zoneinfo import ZoneInfo
import requests

app = Flask(__name__)

@app.route("/")
def main():

    # Change timezone accordingly
    current_time = datetime.now(ZoneInfo("Asia/Kuala_Lumpur")).strftime("%Y-%m-%d %H:%M:%S")

    # Get client IP
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    # If behind proxy/load balancer
    ip = ip.split(",")[0].strip()

    geo = {}

    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=3
        )

        geo = response.json()

    except Exception:
        pass

    return f"""
    <h2>GitOps Pipeline App</h2>

    <b>Current Time:</b> {current_time}<br><br>

    <b>Public IP:</b> {ip}<br>

    <b>City:</b> {geo.get('city','Unknown')}<br>

    <b>Region:</b> {geo.get('regionName','Unknown')}<br>

    <b>Country:</b> {geo.get('country','Unknown')}<br>

    <b>ISP:</b> {geo.get('isp','Unknown')}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)