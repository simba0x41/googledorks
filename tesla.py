import requests,re
from urllib.parse import unquote
from bs4 import BeautifulSoup
from docopt import docopt
from time import time as timer
from functools import partial
from multiprocessing import Pool
from random import choice

def proxies():
        file = 'proxies.txt'
        proxies = []
        with open(file, "r") as p:
            proxies = [line.strip() for line in p]
        proxy = random.choice(proxies)
        start = 0
        end = proxy.index(":")
        st = proxy[start:end]
        e = proxy[end+1:]
        proxie = {"http":"{}:{}".format(st, e)}
        return proxie

def user_agents():
        file = 'ua.txt'
        ua = []
        with open(file, "r") as txt:
            ua = [line.strip() for line in txt]
        user = choice(ua)
        header = {"User-Agent":"{}".format(user)}
        return header

def get_urls(search_string, start):
    temp = []
    url='https://www.google.com/search'
    payload = {'q' : search_string,'start' : start}
    my_headers = {'User-Agent' : 'Megamind/ Tesla: revision', 'Cookie' : 'Megamind'}
    #my_headers = user_agents()
    #my_proxies = proxies()
    r = requests.get(url,params=payload,headers=my_headers)

    soup = BeautifulSoup(r.text,'html.parser')
    divtags = soup.find_all('div',class_='kCrYT')

    for div in divtags:
        try:
            temp.append(unquote(re.search('url\?q=(.+?)\&sa', div.a['href']).group(1)))
        except:
            continue
    return temp 

def dorks(search, pages, processes):
    result = []
    make_request = partial( get_urls, search )
    pagelist     = [ str(x*10) for x in range( 0, int(pages) ) ]
    with Pool(processes) as p:
        tmp = p.map(make_request, pagelist)
    for x in tmp:
        result.extend(x)
    result=list(set(result))
    return result

