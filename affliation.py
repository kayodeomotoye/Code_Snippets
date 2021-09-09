def generate_affiliation_link(url):
    bhu = url.split('/')
    pre_link = 'http://www.amazon.com/dp/'
    post_link = '/?tag=pyb0f-20'
    mid_link = bhu[-2]
    mid_link_short = bhu[-1]
    
    if len(bhu) == 7:
        return f'{pre_link}{mid_link}{post_link}'
        
    else:
        return f'{pre_link}{mid_link_short}{post_link}'



#PYBITES_LINK = 'http://www.amazon.com/dp/{}/?tag=pyb0f-20'


#def generate_affiliation_link(url):
    #asin = url.split('dp/')[-1].split('/')[0]
    #return PYBITES_LINK.format(asin)

link1 = 'https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234'
link2 = 'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X'
link3 = 'https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art'  


generate_affiliation_link(link3)
'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20'
generate_affiliation_link(link1)
'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20'
generate_affiliation_link(link2)
'http://www.amazon.com/dp/020161622X/?tag=pyb0f-20'
