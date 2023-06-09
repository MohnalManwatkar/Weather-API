import requests

def fetch_weather_data(api_key, location):
    base_url = "https://api.weatherstack.com/current"
    params = {
        "key": api_key,
        "q": location
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather_data(data):
    if data is not None:
        print(data)
    else:
        print("Unable to fetch weather data.")

def main():
    api_key = "1cd42ea3ed29c282de420b852f644880"
    location = input("Enter your location: ")
    weather_data = fetch_weather_data(api_key, location)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
