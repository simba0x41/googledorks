"""Tesla Google Scrapper

Usage:
  tesla.py <search> <pages> <processes>
  tesla.py (-h | --help)

Arguments:
  <search>        String to be Searched
  <pages>         Number of pages
  <processes>     Number of parallel processes

Options:
  -h, --help     Show this screen.

"""

import requests,re
from urllib.parse import unquote
from bs4 import BeautifulSoup
from docopt import docopt
from time import time as timer
from functools import partial
from multiprocessing import Pool

def get_urls(search_string, start):
    temp = []
    url='https://www.google.com/search'
    payload = {'q' : search_string,'start' : start}
    my_headers = {'User-Agent' : 'Mozilla/11.0'}
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

