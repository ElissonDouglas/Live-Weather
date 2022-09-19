import requests
from convert import to_F, to_C

API_KEY = "fdd952eb370af336694b25838dd529fe"

city = input('Enter a city:')
print("Type 'F' for Fahrenheit, 'C' for Celsius or 'K' for Kelvin.")
scale = input('Choose a scale: ')
print('-' * 30)


url_base = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID="+API_KEY

weather_data = requests.get(url_base).json()


if scale.upper() == 'C':
    try:
        print(f"City: {weather_data['name'].title()}\nCountry: {weather_data['sys']['country']}\nTemperature: {round(to_C(weather_data['main']['temp']), 2)}⁰C\n"
              f"Max. Temperature: {round(to_C(weather_data['main']['temp_max']), 2)}⁰C\nMin. Temperature: {round(to_C(weather_data['main']['temp_min']), 2)}⁰C\n"
              f"Humidity: {weather_data['main']['humidity']}%\nPressure: {weather_data['main']['pressure']}")

    except KeyError as err2:
        print('Error: city not found')

elif scale.upper() == 'F':
    try:
        print(
            f"City: {weather_data['name'].title()}\nCountry: {weather_data['sys']['country']}\nTemperature: {round(to_F(weather_data['main']['temp']), 2)}⁰F\n"
            f"Max. Temperature: {round(to_F(weather_data['main']['temp_max']), 2)}⁰F\nMin. Temperature: {round(to_F(weather_data['main']['temp_min']), 2)}⁰F\n"
            f"Humidity: {weather_data['main']['humidity']}%\nPressure: {weather_data['main']['pressure']}")

    except KeyError as err2:
        print('Error: city not found')
elif scale.upper() == 'K':
    try:
        print(
            f"City: {weather_data['name'].title()}\nCountry: {weather_data['sys']['country']}\nTemperature: {round(weather_data['main']['temp'], 2)}⁰K\n"
            f"Max. Temperature: {round(weather_data['main']['temp_max'], 2)}⁰K\nMin. Temperature: {round(weather_data['main']['temp_min'], 2)}⁰K\n"
            f"Humidity: {weather_data['main']['humidity']}%\nPressure: {weather_data['main']['pressure']}")

    except KeyError as err2:
        print('Error: city not found')

print('-' * 30)
