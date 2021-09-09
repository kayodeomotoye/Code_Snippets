
def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath, 'r') as f:
        data = f.read()
        new_list=[]
        for i in data.splitlines()[-n:]:
           new_list.append(i)
        return new_list


asd= tail('test_file.txt', 1)