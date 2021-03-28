# File: final_project.py
# Name: Jingru Zhang
# Date: 2/27/2020
# Assignment: 12.1 Final Project
# Course: DSC510 - Introduction to Programming
# Desc: This program interacts with the OpenWeatherMap service, and print out
#       the weather information for the city based ZipCode or city name.
# Usage: This program provides an option for a user whether or not to
#        look up the weather information for a city by input 'Yes' or 'No'.
#        If the input is 'Yes', the program will further asks the user for the
#        ZipCode or city name he/she wants to loop up. This information will be
#        combined with the api key and base url to generate the url for the city
#        in the weather service website. Requests is used to collect the
#        information, the corresponding weather information is then converted
#        to JSON format, and be displayed. The general weather information
#        including current, feels-like， min/max temperature, and wind speed and
#        direction is displayed.

# Import libraries.
import requests

# Set api keys and base url.
api_key = '50a3a3b615f4e4de5a151ac52c64abed'
base_url = 'https://api.openweathermap.org/data/2.5/weather?'


# Return a url for a city query.
def query_by_name(city):
    return base_url + 'q=' + city + ',us&APPID=' + api_key


# Return a url for a zipcode query.
def query_by_zip(zipcode):
    return base_url + 'zip=' + zipcode + ',us' + '&APPID=' + api_key


# Get the wind direction from the degrees, and return a corresponding string.
def wind(speed, degree):
    if degree >= 348.75 or degree <= 11.25:
        return 'N ' + str(speed)
    elif 11.25 < degree <= 33.75:
        return 'NNE ' + str(speed)
    elif 33.75 < degree <= 56.25:
        return 'NE ' + str(speed)
    elif 56.25 < degree <= 78.75:
        return 'ENE ' + str(speed)
    elif 78.75 < degree <= 101.25:
        return 'E ' + str(speed)
    elif 101.25 < degree <= 123.75:
        return 'ESE ' + str(speed)
    elif 123.75 < degree <= 146.25:
        return 'SE ' + str(speed)
    elif 146.25 < degree <= 168.75:
        return 'SSE ' + str(speed)
    elif 168.75 < degree <= 191.25:
        return 'S ' + str(speed)
    elif 191.25 < degree <= 213.75:
        return 'SSW ' + str(speed)
    elif 213.75 < degree <= 236.25:
        return 'SW ' + str(speed)
    elif 236.25 < degree <= 258.75:
        return 'WSW ' + str(speed)
    elif 258.75 < degree <= 281.25:
        return 'W ' + str(speed)
    elif 281.25 < degree <= 303.75:
        return 'WNW ' + str(speed)
    elif 303.75 < degree <= 326.25:
        return 'NW ' + str(speed)
    else:
        return 'NNW ' + str(speed)


if __name__ == '__main__':
    # Print a welcome message.
    print("Hello, welcome to weather forecast application using "
          "OpenWeatherMap's API.")
    # Ask user to loop up the weather condition for a city or not.
    while True:
        is_query = input('Do you want to look up weather condition for a city,'
                         ' Yes or No?\n')
        # Use lower() function for flexibility.
        if is_query.lower() == 'yes':
            # Use try/except to check the connections.
            try:
                # Ask user to input a zip code or city name.
                user_input = input('What is your city name or ZipCode?\n')
                # If the input is numeric, I use the zip code method.
                if user_input.isnumeric():
                    url = query_by_zip(user_input)
                # Otherwise, use the city name method.
                else:
                    url = query_by_name(user_input.lower())
                # Use requests to get the response and convert it to json.
                response = requests.get(url)
                json_response = response.json()
                # Print the weather information, including general, current,
                # feels like, min/max temperature,and wind direction and speed.
                # Temperatures are converted from Kelvin to Celsius.
                print("The weather condition in {} is {}.\nThe current "
                      "temperature is {:.2f} \u2103, " "feels like {:.2f} "
                      "\u2103.\nThe lowest temperature is {:.2f} \u2103, and "
                      "the highest temperature is {:.2f} \u2103.\nThe wind "
                      "speed is {} m/s.\n".format(json_response['name'],
                                                  json_response['weather'][0]['main'], json_response['main']
                                                  ['temp'] - 273.15, json_response['main']['feels_like']
                                                  - 273.15, json_response['main']['temp_min'] - 273.15,
                                                  json_response['main']['temp_max'] - 273.15,
                                                  wind(float(json_response['wind']['speed']),
                                                       float(json_response['wind']['deg']))))
            # Output an message if try is not successful.
            except:
                print('Invalid connection, please double check your city name '
                      'or ZipCode.')
                pass
        # If input is No, exit the loop.
        elif is_query.lower() == 'no':
            break
        # Output a message if input is neither Yes nor No.
        else:
            print("Please tell me 'Yes' or 'No'")
