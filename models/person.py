import json as json

class Person(object):
    def __init__(self, name = None, age = None, country = None):
        self.name = name
        self.age = age
        self.country = country

    def get_name(self):
        return self.name

    def get_country(self):
        return self.country

    def getAllData():
        data = '[{"name": "Souza", "age": 35, "country": "Mexico"}, {"name": "Andrade", "age": 35, "country": "Chile"}, {"name": "Felipe", "age": 35, "country": "Colombia"}, {"name": "Sérgio", "age": 35, "country": "Colombia"}, {"name": "Lisboa", "age": 35, "country": "Colombia"}, {"name": "Souza Lima", "age": 35, "country": "Brazil"}, {"name": "Philip", "age": 35, "country": "USA"}, {"name": "Antony", "age": 35, "country": "United Kingdom"}]'
        return data


