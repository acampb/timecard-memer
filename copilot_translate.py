# define a function to accept a string of text
# convert the text from english to portuguese
# return the translated text

import json
import os

import requests


def translate(text):
    # build the url
    api_key = ""
    url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}&q={text}&target=pt"
    # query the api
    response = requests.get(url)
    # convert the response to json
    data = json.loads(response.text)
    # return the translated text
    return data['data']['translations'][0]['translatedText']

def main(text):
    # get the text from the command line
    # translate the text
    translated = translate(text)
    # print the translated
    print(translated)

if __name__ == "__main__":
    main("Hello World")
