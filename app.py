from flask import Flask, render_template_string
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>GitOps Pipeline App</title>
</head>

<body>

<h2>GitOps Pipeline App</h2>

<b>Current Time:</b> {{ current_time }}<br><br>

<b>Public IP:</b> <span id="ip">Loading...</span><br>
<b>City:</b> <span id="city">Loading...</span><br>
<b>Region:</b> <span id="region">Loading...</span><br>
<b>Country:</b> <span id="country">Loading...</span><br>
<b>ISP:</b> <span id="isp">Loading...</span><br>

<script>
async function loadGeo() {
    try {

        // Get visitor public IP
        const ipResponse = await fetch(
            "https://api.ipify.org?format=json"
        );

        const ipData = await ipResponse.json();

        const publicIp = ipData.ip;

        document.getElementById("ip").textContent = publicIp;


        // Get visitor geolocation
        const geoResponse = await fetch(
            "https://ipwho.is/" + publicIp
        );

        const geoData = await geoResponse.json();


        if (!geoData.success) {
            throw new Error("Geo lookup failed");
        }


        document.getElementById("city").textContent =
            geoData.city || "Unknown";

        document.getElementById("region").textContent =
            geoData.region || "Unknown";

        document.getElementById("country").textContent =
            geoData.country || "Unknown";

        document.getElementById("isp").textContent =
            geoData.connection?.isp || "Unknown";


    } catch (error) {

        console.error("Error:", error);

        document.getElementById("ip").textContent = "Unavailable";
        document.getElementById("city").textContent = "Unavailable";
        document.getElementById("region").textContent = "Unavailable";
        document.getElementById("country").textContent = "Unavailable";
        document.getElementById("isp").textContent = "Unavailable";
    }
}


loadGeo();

</script>

</body>
</html>
"""


@app.route("/")
def main():

    current_time = datetime.now(
        ZoneInfo("Asia/Kuala_Lumpur")
    ).strftime("%Y-%m-%d %H:%M:%S")


    return render_template_string(
        HTML,
        current_time=current_time
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )