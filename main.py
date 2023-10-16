import requests
from datetime import datetime

APP_ID = "YOUR APP ID"
API_KEY = "YOUR API KEY"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

text = input("Exercise u did: ")

# ENTER YOUR DETAILS BELOW
params = {
    "query": text,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 180,
    "age": 19
}

response = requests.post(url=URL, json=params, headers=HEADER)
today = datetime.now()
now_date = today.strftime("%d|%m|%Y")
now_time = today.strftime("%H:%M:%S")

SHEETY_HEADER = {"Authorization": "Bearer TOKEN"}
SHEETY_URL = "YOUR SHEETY URL"
for exercise in response.json()["exercises"]:
    SHEETY_PARAMS = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=SHEETY_URL, json=SHEETY_PARAMS, headers=SHEETY_HEADER)
    print(sheety_response.text)
