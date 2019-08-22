import requests

class FoodCompositionDBAdapter:
    
    def __init__(self, api_key):
        self.key = api_key
        self.base_url = 'https://api.nal.usda.gov/ndb/'
    
    def search_foods(self, keyword, limit):
        params = {'api_function': 'search',
                  'format': 'json',
                  'q': keyword,
                  'max': limit,
                  'api_key': self.key}
        return requests.get(self.base_url, params=params).json()
    
    def search_nutrients(self, food_group, limit):
        params = {'api_function': 'nutrients',
                  'format': 'json',
                  'fg': food_group,
                  'max': limit,
                  'api_key': self.key}
        return requests.get(self.base_url, params=params).json()
