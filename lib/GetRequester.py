import requests
import json

class GetRequester:

    # Initialize with URL
    def __init__(self, url):
        self.url = url

    # Send GET request and return raw bytes
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Returns bytes (b"...")

    # Send GET request and return parsed JSON as Python data
    def load_json(self):
        response = requests.get(self.url)
        return response.json()  # Returns list/dict