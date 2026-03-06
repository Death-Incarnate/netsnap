import os
import json



class ProfiltStore:
    '''
    Хранилище
    '''

    def __init__(self, filepath: str = 'profiles.json'):

        self.filepath = filepath

        self._data: dict = self._load()

    
    def _load(self):
        if os.path.exists(self.filepath):
            with open (self.filepath, enconding='utf-8') as file:
                return json.load(file)
            
        return {}
        