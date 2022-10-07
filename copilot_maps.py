# build a function that accepts a street address starting point and destination
# query google maps api for directions
# return turn by turn directions

import json
import os

import requests


def get_directions(start, end):
    # build the url
    api_key = ""
    url = f"https://maps.googleapis.com/maps/api/directions/json?key={api_key}&origin={start}&destination={end}"
    # query the api
    response = requests.get(url=url, timeout=5)
    # convert the response to json
    data = json.loads(response.text)
    # return the directions
    #print(data)
    return data['routes'][0]['legs'][0]['steps']

def main(start, end):
    # get the start and end points from the command line
    # get the directions
    directions = get_directions(start, end)
    # print the directions
    for step in directions:
        print(step['html_instructions'])
        print(step['distance']['text'])

if __name__ == "__main__":
    main("2160 Thames Ave, York, PA 17408",
         "1175 North Service Rd W, Oakville, ON L6M 2W2, Canada")
