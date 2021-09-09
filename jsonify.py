import json
import re
import pandas as pd
from io import StringIO


members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""

#kayode's
def convert_to_json(members=members):
    new_members = re.sub(r"[;|]", ',', members).strip()
    csv_file = pd.read_csv(StringIO(new_members), index_col= False, dtype= str)
    result= csv_file.to_json(orient = "records", date_format = "epoch", double_precision = 10, 
    force_ascii = True, date_unit = "ms", default_handler = None)
    return result


#pybites
def convert_to_json(members=members):
    lines = members.strip().splitlines()
    keys = lines[0].split(',')

    output = []
    for line in lines[1:]:
        vals = re.split(r'[|,;]', line)
        row = dict(zip(keys, vals))
        output.append(row)

    return json.dumps(output)