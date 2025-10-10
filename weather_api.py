import json
from urllib import request, parse

def huidige_temp_utrecht():
    """
    Haalt de huidige temperatuur (°C) in Utrecht op via Open-Meteo.
    Geeft float terug, of werpt een Exception bij fout.
    """
    base = "https://api.open-meteo.com/v1/forecast"
    qs = parse.urlencode({
        "latitude": 52.0907,    # Utrecht
        "longitude": 5.1214,
        "current_weather": "true"
    })
    url = f"{base}?{qs}"

    with request.urlopen(url, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return float(data["current_weather"]["temperature"])