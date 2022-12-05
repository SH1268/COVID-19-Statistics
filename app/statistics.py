import requests
import os
from app.inputs import selected_region, insert_date, insert_city
from dotenv import load_dotenv



def fetch_data(selected_region):
    requesturl = "https://covid-19-statistics.p.rapidapi.com/reports"
    querystring = {"iso": "USA","region_province": selected_region,"date": insert_date, "city_name": insert_city}
    
    headers = {
        "X-RapidAPI-Key": {API_KEY},
        "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
        }
        
    response = requests.request("GET", requesturl, headers=headers, params=querystring)
    
    print(response.text)

    category = response.text

    for category, matches in category:
        if any(match in text for match in matches):
            return category
        return None
