import requests, re
from bs4 import BeautifulSoup, SoupStrainer

# Manually Auth to codingbat.com and get the JSESSIONID cookie value:
jsessionid = '86209FC75C2CC858D881AB72559E7517'
url = 'http://codingbat.com/prob/p115413'

def get_chapter_links(url, cookie):
    cookies = dict(JSESSIONID=jsessionid)
    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text)
    links = SoupStrainer('a', href=re.compile('/prob/'))
    [tag for tag in BeautifulSoup(r.text, parseOnlyThese=links)]
    

def get_solution(url, cookie):
    cookies = dict(JSESSIONID=jsessionid)
    r = requests.get(url, cookies=cookies)
    #print(r.text)
    soup = BeautifulSoup(r.text)
    
    # URL of excercise
    print url
    
    # Name of excercise (the docs suck)
    #soup.find('span', 'h2').text
    #print soup.body.span.text
    #print soup.p['class'] == 'h2'
    
    # Code of excercise
    print soup.textarea.text


print get_chapter_links(url, jsessionid)