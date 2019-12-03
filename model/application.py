import json

class Application():
    def __init__(self,app_dict):
        self.id = str(app_dict['id'])
        self.name = str(app_dict['name'])
        self.icon = str(app_dict['icon'])
        self.description = str(app_dict['description'])
        self.schema = str(app_dict['schema'])

    def __repr__(self):
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['name'] = self.name
        dictionary['description'] = self.description
        dictionary['icon'] = self.icon
        dictionary['schema'] = self.schema
        return dictionary
