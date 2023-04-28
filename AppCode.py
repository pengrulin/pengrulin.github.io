# Your API KEYS (you need to use your own keys - very long random characters)

import requests

url = "https://mashvisor-api.p.rapidapi.com/rental-rates"


def average_rate(staeName,cityName,zipCode,numRoom):
    
    querystring = {"state":staeName,"source":"airbnb","city":cityName,"zip_code":zipCode}


    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "0a2679a9c0mshe4760d5ee1ce0dcp15c64ejsn38f0ead0c686",
        "X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()

    studio_value = response["content"]["retnal_rates"]["studio_value"]
    one_room_value = response["content"]["retnal_rates"]["one_room_value"]
    two_room_value = response["content"]["retnal_rates"]["two_room_value"]
    three_room_value = response["content"]["retnal_rates"]["three_room_value"]
    four_room_value = response["content"]["retnal_rates"]["four_room_value"]

    if numRoom == "Studio":
        return studio_value
    elif numRoom == "1":
        return one_room_value
    elif numRoom == "2":
        return two_room_value
    elif numRoom == "3":
        return three_room_value
    else:
        return four_room_value

print(average_rate("MA", "Boston","02215",1))




