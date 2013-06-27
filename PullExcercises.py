# Data structure for the site.
# codingbat.com
# |
# -- python sections
#    |
#    -- problems
#
#

import requests, re, time
import pprint
from bs4 import BeautifulSoup

jsessionid = 'DDF207B498934A8E06F3134D0EB66A9D'
base_url = 'http://codingbat.com'
python_sections = base_url + '/python'
    
def get_links(url, cookie, url_contains):
    print('> Getting Links for ' + url)
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
    print('> Getting solution for problem ' + url)
    time.sleep(1)
    cookies = dict(JSESSIONID=jsessionid)
    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text)
    
    solution = '\n# =======================\n'
    solution = solution + '# ' + url + '\n'
    solution = solution + soup.textarea.text[1:]
    return solution

# get list of python section links
section_urls = get_links(python_sections, jsessionid, '/python/')

# get list of problems for each section and populate a dictionary object
i = 0
n = 0
for i in range(len(section_urls)):
#for i in range(0,1):
    # we want to create a new file here
    file_name = section_urls[i].replace('/python/', '') + '.py'
    print('Opening file ' + file_name + ' ==================')
    fo = open('solutions/' + file_name, "wb")

    fo.write("=============================================\n")
    fo.write(file_name)
    problem_list = get_links(base_url+section_urls[i], jsessionid, '/prob/')
    for n in range(len(problem_list)):
        print('+ Writing problem ' + str(n+1))
        fo.write(get_solution(base_url+problem_list[n], jsessionid))
        n =+ 1
    print('Closing file ' + file_name + '\n') 
    fo.close()
    i =+ 1
    # For dev purposes, lets set a limit to not overwhelm server
    if i == 1:
        break
