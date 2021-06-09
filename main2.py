import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT = 51
HEIGHT = 165
AGE = 19
APP_ID = os.environ("APP_ID")

API_KEY = os.environ("API_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me what exercises you did today?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

authorization_header = {
    "Authorization": "Basic c2hvYmhhOnNob2JoYUAxMjM"
}

sheety_endpoint = "https://api.sheety.co/2e91ce3e363b0cb3be82c8d4f11d2542/workoutTracking/workouts"

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']

        }
    }

    sheet_response  = requests.post(sheety_endpoint, json=sheet_inputs, headers=authorization_header)
    print(sheet_response.text)
