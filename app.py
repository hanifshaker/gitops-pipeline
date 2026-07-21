from flask import Flask, request
from datetime import datetime
from zoneinfo import ZoneInfo
import requests

app = Flask(__name__)

@app.route("/")
def main():

    current_time = datetime.now(
        ZoneInfo("Asia/Kuala_Lumpur")
    ).strftime("%Y-%m-%d %H:%M:%S")

    # Tailscale/client IP
    client_ip = request.headers.get(
        "X-Forwarded-For",
        request.remote_addr
    ).split(",")[0].strip()

    geo = {}

    try:
        # Actual public internet IP
        public_ip = requests.get(
            "https://api.ipify.org",
            timeout=3
        ).text.strip()

        geo = requests.get(
            f"https://ip-api.com/json/{public_ip}",
            timeout=3
        ).json()

    except Exception as e:
        print("Geo error:", e)
        public_ip = "Unknown"

    return f"""
    <h2>GitOps Pipeline App</h2>

    <b>Current Time:</b> {current_time}<br><br>

    <b>Client IP (Tailscale):</b> {client_ip}<br>

    <b>Public IP:</b> {public_ip}<br>

    <b>City:</b> {geo.get('city','Unknown')}<br>

    <b>Region:</b> {geo.get('regionName','Unknown')}<br>

    <b>Country:</b> {geo.get('country','Unknown')}<br>

    <b>ISP:</b> {geo.get('isp','Unknown')}
    """