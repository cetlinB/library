import json

class Application():
    def __init__(self,id,name,icon,link,schema):
        self.id = id
        self.name = name
        self.icon = icon
        self.link = link
        self.schema = schema

    def __repr__(self):
        dictionary = dict
        dictionary['id'] = self.id
        dictionary['name'] = self.name
        dictionary['icon'] = self.icon
        dictionary['link'] = self.link
        dictionary['schema'] = self.schema
        return json.dumps(dictionary)
