import requests
import os
import base64


class SpotifyToken:

    def __init__(self):
        print("init")
        self.API_ENDPOINT = "https://accounts.spotify.com/api/token"
        self.CLIENT_SECRET = ""
        self.CLIENT_ID = ""

    def __get_env_vars(self):
        print("__get_env_ars")
        self.CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
        print("value 1 = ", self.CLIENT_SECRET)
        self.CLIENT_ID = os.environ.get("CLIENT_ID")
        print("value 2 = ", self.CLIENT_ID)

    def __get_encoded_credentials(self):
        print("__get_encoded_credentials")
        self.__get_env_vars()
        credentials = f'{self.CLIENT_ID}:{self.CLIENT_SECRET}'
        ascii_credentials = credentials.encode('utf-8')
        encoded_credentials = base64.b64encode(ascii_credentials).decode("utf-8")
        return encoded_credentials

    def __request_token(self):
        print("__request_token")
        encoded_creds = self.__get_encoded_credentials()
        headers = {'authorization': f'Basic {encoded_creds}', 'Content-Type': 'application/x-www'
                                                                              '-form-urlencoded'}
        data = {'grant_type': 'client_credentials'}

        response = requests.post(url=self.API_ENDPOINT, data=data, headers=headers)
        return response.content.decode("utf-8")

    def get_spotify_token(self):
        print("get_spotify_token")
        print("sadsadasdsad")
        # print("***", os.environ.get('CLIENT_ID'))
        return self.__request_token()
