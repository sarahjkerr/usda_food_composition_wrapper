import requests

class Food:
    
    def __init__(self, api_key):
        self.key = api_key
        self.base_url = 'https://api.nal.usda.gov/ndb/search/?format=json'
    
    def search_foods(self, keyword, limit):
        params = {'q': keyword,
                  'max': limit,
                  'api_key': self.key}
        response = requests.get(self.base_url, params=params).json()
        return response
