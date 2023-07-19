# import json
# import requests
# from bs4 import BeautifulSoup
# import flask 

# def get_weather():

#     def get_soup(TARGET_URL):
#         page = requests.get(TARGET_URL)
#         soup = BeautifulSoup(page.text, 'html.parser')
#         return soup


#     variable = input("Hava durumu gösterilmek istenen ilin adını girin: ")

#     URL = f'https://www.timeanddate.com/weather/turkey/{variable.lower()}'

#     soup = get_soup(URL)

#     exam = soup.find(name='div', class_='h2')
#     print(exam.text)

#     weather_data = [{'city': variable, 'weather_info': exam.text}]

#     try:
#         with open('hava_durumu.json', 'r') as f:
#             existing_data = json.load(f)
#             if isinstance(existing_data, list):
#                 weather_data += existing_data
#     except (FileNotFoundError, json.JSONDecodeError):
#         pass

#     with open('hava_durumu.json', 'w') as f:
#         json.dump(weather_data, f, indent=4, ensure_ascii=False)
        
# get_weather()


import requests
from bs4 import BeautifulSoup

def get_soup(TARGET_URL):
    page = requests.get(TARGET_URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def get_weather(city):
    URL = f'https://www.timeanddate.com/weather/turkey/{city.lower()}'
    soup = get_soup(URL)
    exam = soup.find(name='div', class_='h2')
    weather_info = exam.text
    weather_data = {'city': city, 'weather_info': weather_info}
    return weather_data

