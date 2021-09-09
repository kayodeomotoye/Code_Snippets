NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}

def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    new_name = str(name).lower()
    all_dict = [group3, group2, group1]
    
    try:
        return [i[new_name] for i in all_dict if new_name in i.keys()][0]

    except:
        return NOT_FOUND

#from collections import ChainMap
#m = ChainMap(group3, group2, group1)
#m.get('tim')

          

get_person_age('tim')
get_person_age('-1')
get_person_age(None)

#else: 
#return(max([i[new_name] for i in all_dict if new_name in i.keys()]))
        

    

        