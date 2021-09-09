def fizzbuzz(num):
    if num % 15 == 0: 
        return 'Fizz Buzz'
        
    elif num % 5 == 0: 
        return 'Buzz'
    
    elif num % 3 == 0: 
        return 'Fizz'
        
    else: 
        return num


fizzbuzz(2)
fizzbuzz(30)
fizzbuzz(10)


import string
def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    for i in string.punctuation:
        input_string = input_string.replace(i, '')
    return str(input_string)


remove_punctuation('Hello, I am Tim.')