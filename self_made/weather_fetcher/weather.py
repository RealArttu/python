import requests

#   from weather import y_or_no, fooling around with imports
import time

API_KEY = "enter_api_key_from_https://home.openweathermap.org/api_keys" # Enter your API-key inside the quotes
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Wanna see weather or not
def y_or_no():
    while True:
        yn = input("\nWould you like to see the weather in the city that you have chosen? (y/n)\n").lower()

        if yn == "y":
            see_weather()
        elif yn == "n":
            print("\nQuitting, bye!\n")
            break
        else:
            print("\nPlease type only y or n.")

# Weather city asking and fetching
def see_weather():
    
    city = input("\nEnter a city name: ")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        city_open = data['name']
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2)
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        #print(request_url)
        print("\nCity:", city_open)
        print("Weather:", weather)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Wind speed:", wind_speed, "m/s")
        # Some day add temp min-max and feels like. Add matplotlib.
    else:
        er_data = response.json()
        code = er_data['cod']
        msg = er_data['message']

        #print(request_url)
        print("\nAn error occurred, error information below:")
        print("Error code:", code)
        print("Error message:", msg)
        
        if msg == "city not found":
            y_or_no()
        else:
            print("\nQuitting in 2 seconds...\n")
            time.sleep(2)
            quit()


# Y/N loop
y_or_no()