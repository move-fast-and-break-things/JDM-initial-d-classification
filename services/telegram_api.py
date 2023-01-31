import requests
import json


class TelegramApi():
    def __init__(self, token):
        self.TOKEN = token
        self.BASEURL = "https://api.telegram.org/bot{TOKEN}/"
        self.http = requests.Session()
        self.auth()

    def auth(self):
        self.BASEURL = self.BASEURL.format(TOKEN=self.TOKEN)

    def method(self, method, data, files = {}):
        url = self.BASEURL + method + '?'
        query_string = ''

        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):
                valuest = json.dumps(value, ensure_ascii=False)
            else:
                valuest = value
            query_string += key + '=' + str(valuest) + '&'

        url += query_string
        response = self.http.get(url, files=files).json()
        return response
