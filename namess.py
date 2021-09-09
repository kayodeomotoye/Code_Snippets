from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""

#kayode's code
def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    list5 = [x.split(',') for x in data.splitlines()]
    for l, f, c in list5:
        countries[c].append(f + ' ' + l)
    countries.pop('country_code')
    return countries

#pybites code
def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    for line in data.splitlines()[1:]:
        last_name, first_name, country = line.split(',')
        name = f'{first_name} {last_name}'
        countries[country].append(name)
    return countries

#result
group_names_by_country(data)
defaultdict(<class 'list'>, {'ID': ['Husain Watsham', 'Sula Wasielewski'], 'BR': ['Alphonso Harrold'],
 'CN': ['Margo Apdell', 'Ines Parrett', 'Davie Halbard'], 'RU': ['Deerdre Tomblings'], 
 'TD': ['Rudolph Jeffry'], 'SE': ['Luke Brenston'], 'PL': ['Kermit Braunle']})


    
    
