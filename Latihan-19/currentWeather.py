import requests


def get_current_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    try:
        resp = requests.get(url, params=params, timeout=6)
        resp.raise_for_status()
        data = resp.json()
        current = data.get("current_weather")
        if not current:
            return None
        # current contoh: {"temperature": 28.3, "windspeed": 5.4, ...}
        return current
    except requests.exceptions.RequestException as e:
        print("Gagal mengambil cuaca:", e)
        return None


if __name__ == "__main__":

    cw = get_current_weather(-6.2, 106.8)  # contoh: Jakarta
    if cw:
        print(" Cuaca saat ini:")
        print(f" Suhu       : {cw.get('temperature')} derajat C")
        print(f"Angin       : {cw.get('windspeed')} km/h")
