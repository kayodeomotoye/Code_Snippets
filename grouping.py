from itertools import groupby

cars = [
    # need mock data? -> https://www.mockaroo.com == awesome
    ('Mercedes-Benz', '300D'), ('Mercedes-Benz', '600SEL'),
    ('Toyota', 'Avalon'), ('Ford', 'Bronco'),
    ('Chevrolet', 'Cavalier'), ('Chevrolet', 'Corvette'),
    ('Mercedes-Benz', 'E-Class'), ('Hyundai', 'Elantra'),
    ('Volkswagen', 'GTI'), ('Toyota', 'Highlander'),
    ('Chevrolet', 'Impala'), ('Nissan', 'Maxima'),
    ('Ford', 'Mustang'), ('Kia', 'Optima'),
    ('Volkswagen', 'Passat'), ('Nissan', 'Pathfinder'),
    ('Volkswagen', 'Routan'), ('Hyundai', 'Sonata'),
    ('Kia', 'Sorento'), ('Kia', 'Sportage'),
    ('Ford', 'Taurus'), ('Nissan', 'Titan'),
    ('Toyota', 'Tundra'), ('Hyundai', 'Veracruz'),
]
sorted_cars = sorted(cars, key = lambda x : x[0]) 

def group_cars_by_manufacturer(cars):
    """Iterate though the list of (manufacturer, model) tuples
       of the cars list defined above and generate the output as described
       in the Bite description (see the tests for the full output).
       
       No return here, just print to the console. We use pytest > capfd to
       validate your output :)
    """
    key_func = lambda x: x[0]
    for key, group in groupby(sorted_cars, key_func):
        print('\n' + key.upper())
        for model in group:
            print('- ' + model[1])
            

#pybites      

def group_cars_by_manufacturer(cars):
    """Iterate though the list of (manufacturer, model) tuples
       of the cars list defined above and generate the output as described
       in the Bite description (see the tests for the full output).

       No return here, just print to the console. We use pytest > capfd to
       validate your output :)
    """
    cars.sort()  # groupby only works if data is sorted!
    for manufacturer, models in groupby(cars, key=itemgetter(0)):
        print(manufacturer.upper())
        for model in models:
            print(f'- {model[1]}')
        print()



    my_iter = key, group in groupby(cars, key_func)
  




for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))