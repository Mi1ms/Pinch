import json
import requests
import pprint

class ConnectData():

    def connect(self):

        response = requests.get('http://localhost:3000/api/v1/')
        if response.status_code == 200 :
            # print(response.content)
            return response.content
            pass
        else:
            print('no')
            print(response.status_code)

get = ConnectData()
get.connect()   
