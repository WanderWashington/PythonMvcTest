import pycountry_convert as pc
import json as json
from num2words import num2words

'''
 Não entendi o motivo de limitar a 2 o contador de pessoas, mas como fazia parte
 do que já estava implementado e no enunciado citava que deveria funcionar como o
 exemplo, mantive.
'''
def getPeopleSouthAmericaAndMexico(data):

    """Reads a json and returns the quantity of people per country in South America and Mexico
       When the maximum people quantity is not higher than two
    """
    # Simulação de uma conexão com banco de dados SQL
    # db_ engine = create_engine(*args)
    # db = session()
    
    # db.query("SELECT * FROM table1 WHERE name age = 35")
    # Data é o resultado da query acima, colocamos como json para ficar mais fácil de você usar!

    data = json.loads(data)
    country = {}
    for x in data:
        country_code = pc.country_name_to_country_alpha2(x["country"], cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        if continent_name in ('SA') or country_code =='MX':
            country[x["country"]] = country.get(x["country"], 0) +1
    r = {}
    for x,y  in country.items():
        if y <= 2:
            r[x] = num2words(y, lang='pt-br').capitalize()
    return r

'''
  Returns a quantity of people for each country in south america
'''
def getPeopleQuantityInSouthAmerica(data):
    """Reads a json and returns the quantity of people per country in South America
       When the maximum people quantity is not higher than two"""
    country = {}
    data = json.loads(data)
    for x in data:
        country_code = pc.country_name_to_country_alpha2(x["country"], cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        if continent_name == 'SA':
            country[x["country"]] = country.get(x["country"], 0) +1
    for x in list(country.keys()):
        if country[x] > 2:
            del country[x]
    return country


def countContinent(data):
    """Reads a json and returns the quantity of people by continent."""
    continents = {}
    data = json.loads(data)
    for x in data:
        country_code = pc.country_name_to_country_alpha2(x["country"], cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        continents[continent_name] = continents.get(continent_name, 0) +1
    for x in continents:
        if continents.get(x) > 2:
            continents.pop()
    return continents;

if __name__ == "__main__":
    action_1()
