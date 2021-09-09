def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""

    
    with open(file_, 'r') as f:
        data = f.read()
        line_count = len(data.splitlines())
        num_words = len(data.split())
        num_xters = len(data)
    

    output = f'{line_count}    {num_words}    {num_xters}     {f.name}'
    return f'{output}'

    
result = wc('test_file.txt')
print(result)
type(result)


#if __name__ == '__main__':
    # make it work from cli like original unix wc
    #import sys
    #print(wc(sys.argv[1]))