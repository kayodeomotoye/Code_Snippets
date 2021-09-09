
def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    #('#{:02x}{:02x}{:02x}'.format( 120, 0 , 255 )).upper
  
    for line in rgb:
        if line < 0 or line > 255:
            raise ValueError
    
    return ('#{:02x}{:02x}{:02x}'.format( rgb[0], rgb[1], rgb[2] )).upper()


#pybites
def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all(0 <= val <= 255 for val in rgb):
        raise ValueError(f'rgb {rgb} not in range(256)')

    return '#' + ''.join([f'{val:02x}' for val in rgb]).upper()

rgb_to_hex((0, 0, 0))
rgb_to_hex((100, 200, 256))
rgb_to_hex((255, 0, 255)) 
rgb_to_hex((-1, 100, 100))


0 > line > 255