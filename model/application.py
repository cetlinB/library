import json

class Application():
    def __init__(self,app_dict):
        self.id = app_dict['id']
        self.name = app_dict['name']
        self.icon = app_dict['icon']
        self.description = app_dict['description']
        self.schema = app_dict['schema']

    def __repr__(self):
        dictionary = dict
        dictionary['id'] = self.id
        dictionary['name'] = self.name
        dictionary['description'] = self.description
        dictionary['icon'] = self.icon
        dictionary['schema'] = self.schema
        return json.dumps(dictionary)
