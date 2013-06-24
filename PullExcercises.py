# Data structure for the site.
# codingbat.com
# |
# -- python sections
#    |
#    -- problems
#
#

import requests, re
import pprint
from bs4 import BeautifulSoup, SoupStrainer, Tag

jsessionid = 'FED996EDB1994ED2C0E76A6A49F6DF2A'
base_url = 'http://codingbat.com'
#url = base_url + '/prob/p115413'
python_sections = base_url + '/python'
chapter_url = base_url + '/python/String-1'
    
def get_links(url, cookie, url_contains):
    cookies = dict(JSESSIONID=cookie)
    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text)
    
    count = 0
    links_list = []
    for link_tag in soup.findAll('a'):
        #print link_tag
        if link_tag['href'] and len(link_tag['href']) > 0:
            if url_contains in link_tag['href']: 
                links_list.append(link_tag['href'])
                #print link_tag['href']
            count += 1
    return list(set(links_list))

def get_solution(url, cookie):
    cookies = dict(JSESSIONID=jsessionid)
    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text)
    
    # URL of excercise
    print '# =========================================='
    print '# ' + url
    print soup.textarea.text[1:]
    

# get list of python section links
section_urls = get_links(python_sections, jsessionid, '/python/')

# get list of problems for each section and populate a 
i = 0
n = 0
#for i in range(len(section_urls)):
for i in range(0,3):
    # we want to create a new file here
    print("=======================")
    print section_urls[i]
    problem_list = get_links(base_url+section_urls[i], jsessionid, '/prob/')
    for n in range(len(problem_list)):
        get_solution(base_url+problem_list[n], jsessionid)
        n =+ 1
    i =+ 1
    if i == 2:
        break
    # we can close the file here
