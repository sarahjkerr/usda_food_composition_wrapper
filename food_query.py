import requests
import pandas as pd
import json

class Food:
    
    def __init__(self, api_key, keword, limit):
        self.key = api_key
        self.keyword = keyword
        self.limit = limit
    
    def search_foods(self):
        base_url = 'https://api.nal.usda.gov/ndb/search/?format=json'
        params = {'q': self.keyword,
                  'max': self.limit,
                  'api_key': self.key}
        self.response = requests.get(base_url, params=params)
        return self.response.text